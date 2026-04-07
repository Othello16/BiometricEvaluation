MINEX III Nbis Reference Envelope
=================================

Purpose
-------

This is a reference container-envelope pattern around the public
`nbisminexiii` artifact. It exists to demonstrate how a native MINEX III
library set can be carried in a container without redefining the MINEX
interface.

Important limitation
--------------------

This reference envelope is not proof of official MINEX III validation. It is
only an envelope around a public reference build.

Use
---

 * build the native `nbisminexiii` libraries first
 * copy the built libraries into the local `artifacts/` directory
 * build the image

Reference commands
------------------

Build the public upstream `nbisminexiii` libraries:

```bash
git clone https://github.com/usnistgov/nbisminexiii.git /tmp/nbisminexiii-upstream
cd /tmp/nbisminexiii-upstream
make -j
```

Stage the built libraries into this envelope directory:

```bash
mkdir -p artifacts
cp /tmp/nbisminexiii-upstream/lib/libminexiii_nbisminexiii_5002.so artifacts/
cp /tmp/nbisminexiii-upstream/lib/libmindtct.so artifacts/
cp /tmp/nbisminexiii-upstream/lib/libincits.so artifacts/
cp /tmp/nbisminexiii-upstream/lib/libbozorth3.so artifacts/
```

Build the envelope image:

```bash
docker build -t minexiii-nbis-envelope:latest -f Containerfile .
```

Smoke-check the image:

```bash
docker run --rm minexiii-nbis-envelope:latest
```

Expected staged files
---------------------

 * `artifacts/libminexiii_nbisminexiii_5002.so`
 * `artifacts/libmindtct.so`
 * `artifacts/libincits.so`
 * `artifacts/libbozorth3.so`

Design notes
------------

 * non-root runtime user
 * no development toolchain inside the runtime image
 * libraries stored under `/opt/minex/lib`
 * container carries the native library set, not a web wrapper
