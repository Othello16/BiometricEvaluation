import base64
import binascii
from io import BytesIO
from typing import Optional

import face_recognition
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from PIL import Image


app = FastAPI(title="matcher-face", version="0.1.0")


class MatchRequest(BaseModel):
    gallery_image_b64: str = Field(..., description="Base64-encoded gallery image")
    probe_image_b64: str = Field(..., description="Base64-encoded probe image")
    detection_model: str = Field(default="hog", pattern="^(hog|cnn)$")
    threshold: Optional[float] = Field(default=None, ge=0.0, le=1.0)


class MatchResponse(BaseModel):
    distance: float
    similarity: float
    matched: Optional[bool]


def decode_image(image_b64: str) -> np.ndarray:
    try:
        raw = base64.b64decode(image_b64, validate=True)
    except binascii.Error as exc:
        raise HTTPException(status_code=400, detail="invalid base64 image") from exc
    try:
        image = Image.open(BytesIO(raw)).convert("RGB")
    except Exception as exc:  # pragma: no cover
        raise HTTPException(status_code=400, detail="invalid image payload") from exc
    return np.array(image)


def extract_single_encoding(image: np.ndarray, detection_model: str) -> np.ndarray:
    locations = face_recognition.face_locations(image, model=detection_model)
    if not locations:
        raise HTTPException(status_code=422, detail="no face detected")
    encodings = face_recognition.face_encodings(image, known_face_locations=locations)
    if len(encodings) != 1:
        raise HTTPException(status_code=422, detail="expected exactly one face")
    return encodings[0]


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "face"}


@app.post("/match", response_model=MatchResponse)
def match(request: MatchRequest) -> MatchResponse:
    gallery_image = decode_image(request.gallery_image_b64)
    probe_image = decode_image(request.probe_image_b64)

    gallery_encoding = extract_single_encoding(gallery_image, request.detection_model)
    probe_encoding = extract_single_encoding(probe_image, request.detection_model)

    distance = float(face_recognition.face_distance([gallery_encoding], probe_encoding)[0])
    similarity = max(0.0, 1.0 - distance)
    matched = distance <= request.threshold if request.threshold is not None else None

    return MatchResponse(distance=distance, similarity=similarity, matched=matched)
