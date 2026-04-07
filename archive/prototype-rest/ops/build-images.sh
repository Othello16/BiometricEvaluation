#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

podman build \
  -t matcher-fingerprint:latest \
  -f "$ROOT_DIR/services/fingerprint/Containerfile" \
  "$ROOT_DIR/services/fingerprint"

podman build \
  -t matcher-face:latest \
  -f "$ROOT_DIR/services/face/Containerfile" \
  "$ROOT_DIR/services/face"

podman build \
  -t matcher-iris:latest \
  -f "$ROOT_DIR/services/iris/Containerfile" \
  "$ROOT_DIR/services/iris"
