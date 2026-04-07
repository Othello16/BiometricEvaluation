NIST-Compatible Phase 1 PRD
===========================

Objective
---------

Create a repository that lets Jupiter prepare, validate, and package vendor
submissions that conform to public NIST biometric evaluation interfaces.

This project is not a generic matcher host. It is a compatibility layer around
specific NIST evaluation targets.

Prime Directive
---------------

Everything created here must prioritize compatibility with:

 * the relevant NIST evaluation interface
 * hardened deployment in a FISMA High oriented environment
 * RHEL 9 compatible userspace
 * Ubuntu host operation
 * SELinux enforcing operation where applicable

Phase 1 Scope
-------------

Phase 1 supports these exact targets:

 * FRVT 1:1
 * FRVT 1:N
 * FRVT Age Estimation
 * FRVT Morph
 * FRVT Quality
 * FRVT Five
 * FRVT Twins
 * IREX 10 Identification
 * MINEX III
 * PFT III

Phase 1 does not support:

 * ad hoc REST-only wrappers as the main integration path
 * custom APIs that bypass the NIST interface
 * internet-dependent runtime behavior in the production path
 * benchmark claims beyond what the official NIST harness supports

Core Requirements
-----------------

1. Every target path must anchor to the official NIST evaluation interface.
2. Vendor binaries must remain native implementations of the NIST interface.
3. Containers must be used only as runtime envelopes around those binaries.
4. The repository must expose exact target requirements, not modality-level
   generalities.
5. The repository must include hardened build profiles per target family.
6. The repository must surface compatibility gaps before deployment.
7. The repository must separate PFT III and MINEX III completely.

Acceptance Criteria
-------------------

 * Each supported target has its own directory and target brief.
 * Each supported target has a compatibility checklist.
 * Each target family has a hardened build profile.
 * The repo includes a vendor compatibility matrix.
 * The repo includes a container envelope pattern that preserves the native
   submission interface.
 * Prototype REST scaffolds are removed from the main execution path.

Design Principles
-----------------

 * source of truth is always the official NIST target package
 * no substitution of REST APIs for native submission contracts
 * offline-capable builds are preferred
 * provenance, repeatability, and auditability are mandatory
 * target-specific differences are first-class, not hidden

Security Posture
----------------

The expected security model is closer to controlled deployment than developer
convenience. The design assumes:

 * no unrestricted outbound internet during production runtime
 * artifact pinning and checksum verification
 * non-root containers
 * read-only runtime filesystems where feasible
 * dropped Linux capabilities
 * signed or internally approved vendor artifacts
 * auditable build and validation logs

Authoritative Public Sources
----------------------------

 * `libbiomeval` moved from this repo and is shared framework infrastructure:
   https://github.com/usnistgov/libbiomeval
 * FRVT repository with public evaluation packages:
   https://github.com/usnistgov/frvt
 * IREX 10 public evaluation site:
   https://pages.nist.gov/IREX10/
 * IREX 10 public repository:
   https://github.com/JRMatey-NIST/IREX10
 * MINEX repository:
   https://github.com/usnistgov/minex
 * PFT III public results and submission metadata:
   https://pages.nist.gov/pft/results/pftiii/
