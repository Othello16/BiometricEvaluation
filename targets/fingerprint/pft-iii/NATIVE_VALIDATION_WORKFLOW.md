PFT III Native Validation Workflow
==================================

Purpose
-------

Validate the vendor deliverable against the native PFT III path before any
container envelope is built.

Public anchors
--------------

 * `https://github.com/usnistgov/pft`
 * `https://github.com/usnistgov/pft/tree/master/pftiii`
 * official validation package path:
   `pftiii/validation/`
 * official API header:
   `pftiii/include/pftiii.h`
 * official validation script:
   `pftiii/validation/validate`
 * public validation package version anchor:
   `202508280945`

Workflow
--------

1. Pull and pin the official public PFT materials.
2. Record the exact `pft` commit, API version, and validation package version.
3. Compare the vendor deliverable against the PFT III interface expectations.
4. Build the vendor implementation natively in a controlled Linux environment.
5. Run the official `./validate` flow from the pinned `pftiii/validation/`
   package.
6. Capture logs, exit codes, generated artifacts, and any interface mismatches.
7. Freeze the validated binary set before container packaging.

Environment notes
-----------------

Preferred native validation order:

1. controlled Linux build host matching the official validation baseline
2. pinned compiler and dependency versions
3. official validation package execution
4. RHEL 9 compatible runtime envelope only after native validation succeeds

Important compatibility note
----------------------------

The public PFT III validation package explicitly requires `Ubuntu Server 24.04.3
LTS`, `g++`, and package-level compatibility close to the NIST environment. That
is the validation baseline, not the final hardened runtime target.

For this project, Jupiter should treat the process as two-stage:

 * Stage A: prove native PFT III compatibility using the official validation
   baseline
 * Stage B: package the validated native artifact into the hardened RHEL 9
   compatible container envelope without changing the PFT-facing behavior
