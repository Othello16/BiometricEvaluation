MINEX III Native Validation Workflow
====================================

Purpose
-------

Validate the vendor deliverable against the native MINEX III path before any
container envelope is built.

Public anchors
--------------

 * `https://github.com/usnistgov/minex`
 * public release anchor: `MINEX III Validation (201907011032)`
 * reference wrapper example: `https://github.com/usnistgov/nbisminexiii`
 * official validation package path:
   `minexiii/validation/`
 * official API header:
   `minexiii/validation/minexiii.h`

Workflow
--------

1. Pull and pin the official public MINEX materials.
2. Record the exact release tag, archive name, or commit used.
3. Pull and inspect `nbisminexiii` as a reference for the wrapping pattern.
4. Compare the vendor deliverable against the MINEX interface expectations.
5. Build the vendor implementation natively in a controlled Linux environment.
6. Run the official `./validate` flow from the pinned `minexiii/validation/`
   package tied to the chosen release anchor.
7. Capture logs, exit codes, generated artifacts, and any interface mismatches.
8. Freeze the validated binary set before container packaging.

Expected outputs
----------------

Jupiter should leave behind:

 * exact upstream MINEX source reference
 * exact vendor artifact manifest and checksums
 * validation command transcript
 * pass or fail result
 * precise list of interface mismatches or runtime failures

Stop conditions
---------------

Do not proceed to a container envelope if:

 * the vendor artifact does not map cleanly to the MINEX interface
 * validation cannot be reproduced
 * required runtime libraries are unknown
 * runtime depends on uncontrolled host state

Environment notes
-----------------

Preferred native validation order:

1. controlled Linux build host matching the official validation baseline
2. pinned compiler and dependency versions
3. official validation package execution
4. RHEL 9 compatible runtime envelope only after native validation succeeds

Important compatibility note
----------------------------

The public MINEX III validation package explicitly requires `CentOS 7.6.1810`
and `yum` for its validation flow. That is a validation baseline, not the final
hardened runtime target.

For this project, Jupiter should treat the process as two-stage:

 * Stage A: prove native MINEX III compatibility using the official validation
   baseline
 * Stage B: package the validated native artifact into the hardened RHEL 9
   compatible container envelope without changing the MINEX-facing behavior

Security notes
--------------

For a hardened deployment path:

 * do not allow runtime package downloads
 * do not rely on mutable internet sources after intake
 * collect checksums before promotion
 * preserve a read-only copy of the validated native artifact set
