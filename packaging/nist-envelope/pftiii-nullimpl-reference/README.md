PFT III Nullimpl Reference Envelope
===================================

Purpose
-------

This is a reference container-envelope pattern around the public
`pftiii/nullimpl` artifact. It exists to demonstrate how a native PFT III
library can be carried in a container without redefining the PFT interface.

Important limitation
--------------------

This reference envelope is not proof of official PFT III validation. It is only
an envelope around a public reference build.

Use
---

 * build the native `nullimpl` library first
 * copy the built libraries into the local `artifacts/` directory
 * build the image

Reference commands
------------------

Build the public upstream `nullimpl` library:

```bash
git clone https://github.com/usnistgov/pft.git /tmp/pft-upstream
cd /tmp/pft-upstream/pftiii/nullimpl
mkdir -p build
cd build
cmake ..
make -j
```

Stage the built libraries into this envelope directory:

```bash
mkdir -p artifacts
cp /tmp/pft-upstream/pftiii/nullimpl/build/libpftiii_nullimpl_0001.so artifacts/
cp /tmp/pft-upstream/pftiii/nullimpl/build/libpftiii/libpftiii.so artifacts/
```

Build the envelope image:

```bash
docker build -t pftiii-nullimpl-envelope:latest -f Containerfile .
```

Smoke-check the image:

```bash
docker run --rm pftiii-nullimpl-envelope:latest
```

Expected staged files
---------------------

 * `artifacts/libpftiii_nullimpl_0001.so`
 * `artifacts/libpftiii.so`

Design notes
------------

 * non-root runtime user
 * no development toolchain inside the runtime image
 * libraries stored under `/opt/pft/lib`
 * container carries the native library, not a web wrapper
