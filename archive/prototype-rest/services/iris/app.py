import base64
import binascii
from io import BytesIO
from typing import Literal, Optional

import iris
import numpy as np
from fastapi import FastAPI, HTTPException
from iris.nodes.matcher.hamming_distance_matcher import HammingDistanceMatcher
from pydantic import BaseModel, Field
from PIL import Image


app = FastAPI(title="matcher-iris", version="0.1.0")
pipeline = iris.IRISPipeline()
matcher = HammingDistanceMatcher()


class MatchRequest(BaseModel):
    gallery_image_b64: str
    probe_image_b64: str
    gallery_eye_side: Literal["left", "right"] = "left"
    probe_eye_side: Literal["left", "right"] = "left"
    threshold: Optional[float] = Field(default=None, ge=0.0, le=1.0)


class MatchResponse(BaseModel):
    distance: float
    matched: Optional[bool]


def decode_grayscale(image_b64: str) -> np.ndarray:
    try:
        raw = base64.b64decode(image_b64, validate=True)
    except binascii.Error as exc:
        raise HTTPException(status_code=400, detail="invalid base64 image") from exc
    try:
        image = Image.open(BytesIO(raw)).convert("L")
    except Exception as exc:  # pragma: no cover
        raise HTTPException(status_code=400, detail="invalid image payload") from exc
    return np.array(image)


def extract_template(image: np.ndarray, eye_side: str, image_id: str):
    try:
        output = pipeline(iris.IRImage(img_data=image, image_id=image_id, eye_side=eye_side))
    except Exception as exc:  # pragma: no cover
        raise HTTPException(status_code=422, detail=f"iris pipeline failed: {exc}") from exc
    if "iris_template" not in output:
        raise HTTPException(status_code=422, detail="iris template missing from pipeline output")
    return output["iris_template"]


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "iris"}


@app.post("/match", response_model=MatchResponse)
def match(request: MatchRequest) -> MatchResponse:
    gallery_image = decode_grayscale(request.gallery_image_b64)
    probe_image = decode_grayscale(request.probe_image_b64)

    gallery_template = extract_template(gallery_image, request.gallery_eye_side, "gallery")
    probe_template = extract_template(probe_image, request.probe_eye_side, "probe")

    distance = float(matcher.run(template_probe=probe_template, template_gallery=gallery_template))
    matched = distance <= request.threshold if request.threshold is not None else None

    return MatchResponse(distance=distance, matched=matched)
