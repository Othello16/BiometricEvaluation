#!/usr/bin/env bash
set -euo pipefail

mkdir -p /srv/biometrics/fingerprint /srv/biometrics/face /srv/biometrics/iris

for name in matcher-fingerprint matcher-face matcher-iris; do
  if podman container exists "$name"; then
    podman rm -f "$name"
  fi
done

podman run -d \
  --name matcher-fingerprint \
  --restart=unless-stopped \
  --memory=2g \
  -p 8081:8081 \
  -v /srv/biometrics/fingerprint:/workspace \
  matcher-fingerprint:latest

podman run -d \
  --name matcher-face \
  --restart=unless-stopped \
  --memory=4g \
  -p 8082:8082 \
  -v /srv/biometrics/face:/workspace \
  matcher-face:latest

podman run -d \
  --name matcher-iris \
  --restart=unless-stopped \
  --memory=4g \
  -p 8083:8083 \
  -v /srv/biometrics/iris:/workspace \
  matcher-iris:latest
