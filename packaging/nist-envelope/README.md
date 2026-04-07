NIST Envelope Container Pattern
===============================

Purpose
-------

Use containers only as delivery and runtime envelopes around already validated
native NIST-compatible binaries.

Rules
-----

 * the container does not redefine the target interface
 * the container copies in vendor binaries and their pinned dependencies
 * the container entrypoint launches the native validation or runtime binary
 * the container contains no development toolchain unless strictly required

Recommended stages
------------------

1. Native build or vendor binary intake
2. Native target validation
3. Runtime envelope image creation
4. Envelope validation

Minimum contents
----------------

 * target-specific native library or executable
 * dependent shared libraries
 * immutable manifest with checksums
 * read-only config where possible
 * logs directed to mounted runtime storage
