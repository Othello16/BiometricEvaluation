Common Hardened Build Profile
=============================

Apply these controls to every target unless the target brief states otherwise.

Build-time requirements
-----------------------

 * use pinned package versions where internally possible
 * mirror dependencies internally for production use
 * record checksums for vendor artifacts and upstream target packages
 * produce build logs and keep them with the target record
 * prohibit silent dependency fetches during runtime

Runtime requirements
--------------------

 * non-root execution
 * read-only root filesystem where feasible
 * writable temp mounted explicitly
 * no SSH or shell service in container
 * explicit UID/GID
 * dropped Linux capabilities by default
 * no privileged containers
 * no host networking unless the target explicitly requires it
 * SELinux enforcing labeling on mounts where supported

Supply-chain requirements
-------------------------

 * signed base images or internally approved equivalents
 * SBOM generation
 * vulnerability scan before promotion
 * immutable image tags for approved builds

Operational requirements
------------------------

 * no direct internet egress from production runtime unless approved
 * audit logs for build, validation, and release
 * separate build and runtime stages
 * checksum manifest for all delivered libraries and config files
