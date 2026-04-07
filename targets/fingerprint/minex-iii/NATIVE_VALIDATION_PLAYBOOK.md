MINEX III Native Validation Playbook
====================================

Purpose
-------

This playbook is the executable companion to
`NATIVE_VALIDATION_WORKFLOW.md`. It is designed so Jupiter can run the MINEX III
path in a controlled way without improvising the validation sequence.

Public anchors
--------------

 * official MINEX repository: `https://github.com/usnistgov/minex`
 * official MINEX III materials live under `minexiii/` in that repository
 * official API reference pointer from `nbisminexiii`:
   `https://github.com/usnistgov/minex/blob/master/minexiii/testplan.pdf`
 * reference wrapper example: `https://github.com/usnistgov/nbisminexiii`
 * public validation release anchor:
   `MINEX III Validation (201907011032)`
 * official validation README:
   `https://github.com/usnistgov/minex/blob/master/minexiii/validation/README.md`
 * official validation script:
   `https://github.com/usnistgov/minex/blob/master/minexiii/validation/validate`
 * official API header:
   `https://github.com/usnistgov/minex/blob/master/minexiii/validation/minexiii.h`

Important boundary
------------------

Use this as a controlled execution template. Exact command names, script names,
and release-file layout must be confirmed from the pinned public MINEX III
release and recorded in the execution log before proceeding.

Validation-baseline note
------------------------

The public MINEX III validation package requires `CentOS 7.6.1810` and `yum`.
That requirement applies to native validation. It does not mean the final
hardened runtime envelope should remain on CentOS 7.

Expected working directories
----------------------------

Use a structure like:

```text
minex-work/
  official/
    minex/
    minex-validation/
    nbisminexiii/
  vendor/
    intake/
    build/
    artifacts/
  logs/
  manifests/
```

Pre-flight checklist
--------------------

Before running any build or validation command, Jupiter must confirm:

 * the exact `minex` commit, tag, or archive in use
 * the exact validation release archive name in use
 * the exact `nbisminexiii` commit in use, if used as a reference
 * the vendor artifact checksums
 * the target architecture
 * the compiler and standard-library versions
 * whether the vendor needs license files, daemons, or environment variables
 * whether the deliverable supports the MINEX III API functions `get_pids`,
   `create_template`, and `match_templates`
 * whether the deliverable respects MINEX constants such as 500 ppi and the
   32-800 byte template size constraints

Step 1: Pin public sources
--------------------------

Record in `logs/minex-source-record.txt`:

 * `minex` source URL
 * `minex` commit or release ID
 * validation release archive name and checksum
 * `nbisminexiii` commit ID if used

Minimum commands Jupiter should run or adapt:

```bash
git clone https://github.com/usnistgov/minex.git official/minex
git clone https://github.com/usnistgov/nbisminexiii.git official/nbisminexiii
```

Then record:

```bash
git -C official/minex rev-parse HEAD
git -C official/nbisminexiii rev-parse HEAD
sha256sum official/minex-validation/*
```

Step 2: Inspect the official MINEX III package layout
-----------------------------------------------------

Jupiter must identify and record:

 * validation scripts
 * build scripts or makefiles
 * API header files
 * shared-library naming expectations
 * config files
 * expected input and output directories
 * exact output archive behavior
 * exact log-file names

Recommended inspection commands:

```bash
find official/minex/minexiii -maxdepth 3 -type f | sort
find official/minex-validation -maxdepth 3 -type f | sort
```

Record the results in:

 * `logs/minexiii-official-layout.txt`

Step 3: Compare the vendor artifact to the MINEX III interface
--------------------------------------------------------------

Use:

 * `VENDOR_INTAKE_CHECKLIST.md`
 * `VENDOR_ARTIFACT_MANIFEST_TEMPLATE.yaml`

Jupiter must determine:

 * whether the vendor exposes extractor and matcher behavior in a form the
   MINEX III interface can use
 * whether the template output is interoperable rather than proprietary
 * whether the runtime dependency model is acceptable for controlled deployment
 * whether the core library can be named as required:
   `libminexiii_<company>_<CBEFF>.a` or `.so`
 * whether `get_pids`, `create_template`, and `match_templates` can be exported
   exactly as required by `minexiii.h`

Required evidence:

 * completed vendor questionnaire
 * manifest with checksums
 * explicit go/no-go decision on MINEX compatibility

Step 4: Build the vendor deliverable natively
---------------------------------------------

Use a controlled Linux environment first. Do not start in the container
envelope.

Jupiter should capture:

 * full build command
 * environment variables
 * compiler version
 * linker and runtime-library results

Minimum commands to record:

```bash
uname -a
gcc --version || true
g++ --version || true
ldd --version || true
env | sort
```

Vendor-specific build commands go into:

 * `logs/minexiii-vendor-build.txt`

Step 5: Map the build output into the official MINEX III validation layout
--------------------------------------------------------------------------

Jupiter must identify:

 * the exact library file names expected by the validation package
 * the exact config-file locations expected by the validation package
 * any wrapper or loader code required by the official interface
 * whether the submission is generator-only
 * whether marketing-name environment variables should be set

If `nbisminexiii` is used for comparison, use it only to understand:

 * library naming
 * API wrapping shape
 * likely build-output organization

Do not treat it as proof that a vendor deliverable is compliant.

Required official layout to prepare
-----------------------------------

Before running validation, Jupiter should prepare:

 * `official/minex-validation/lib/`
   Contains all required participant libraries.
 * `official/minex-validation/config/`
   Contains required config files only. If populated, it must not be writable.
 * exactly one core library matching the official naming convention:
   `libminexiii_<company>_<CBEFF>.a` or `libminexiii_<company>_<CBEFF>.so`

If a shared object is used:

 * its SONAME should match the core library filename

Optional environment variables from the official validation flow:

 * `MINEXIII_GENERATOR_MARKETING_NAME`
 * `MINEXIII_MATCHER_MARKETING_NAME`
 * `MINEXIII_GENERATOR_ONLY=TRUE`

Step 6: Execute the official validation flow
--------------------------------------------

This step must use the pinned public validation package.

Jupiter must record:

 * the exact command used
 * the working directory
 * all environment variables
 * stdout and stderr
 * exit code

Concrete command block based on the public validation package:

```bash
cd official/minex-validation
./validate 2>&1 | tee ../../logs/minexiii-validation-run.txt
echo $? > ../../logs/minexiii-validation-exit-code.txt
```

Before execution, Jupiter must first verify and write down:

 * `/etc/redhat-release` matches `CentOS Linux release 7.6.1810 (Core)`
 * required packages are installed:
   `binutils`, `centos-release`, `coreutils`, `curl`, `file`, `gawk`,
   `gcc-c++`, `grep`, `iputils`, `make`, `sed`, `which`, `yum`
 * no previous validation output directory exists
 * `lib/` and `config/` are prepared correctly

Expected validation behaviors from the public package:

 * builds `minexiii_validation`
 * runs `minexiii_validation pid`
 * runs `minexiii_validation create <seed>`
 * runs `minexiii_validation match <seed>`
 * creates a tarball named after the validation output directory

Step 7: Capture pass/fail evidence
----------------------------------

At minimum, preserve:

 * validation exit code
 * generated output files
 * report files
 * wrapper logs
 * copied library inventory
 * `ldd` output for all shipped shared libraries
 * generated `compile.log`
 * generated `cbeff.log`
 * generated `create.log`
 * generated `match.log`
 * generated `templates/`
 * generated submission archive

Suggested commands:

```bash
find vendor/artifacts -type f -exec sha256sum {} \; | sort > manifests/vendor-artifacts.sha256
find official/minex-validation -type f | sort > logs/minexiii-validation-output-files.txt
ldd vendor/artifacts/* > logs/minexiii-ldd.txt 2>&1 || true
find official/minex-validation -maxdepth 1 -type f -name '*.tar.gz' | sort > logs/minexiii-submission-archives.txt
```

Step 8: Decide whether to proceed to container envelope packaging
-----------------------------------------------------------------

Proceed only if:

 * the vendor build is reproducible
 * the MINEX III validation flow is reproducible
 * the interface mapping is explicit and documented
 * all runtime dependencies are known and pinned

Do not proceed if:

 * the validation flow is still partially guessed
 * the vendor requires uncontrolled host mutation
 * runtime libraries or licensing dependencies remain untracked

Phase 1 outputs Jupiter should commit
-------------------------------------

 * completed vendor questionnaire
 * completed vendor artifact manifest
 * source record
 * native build log
 * validation run log
 * interface mismatch notes
 * recommendation: `proceed`, `hold`, or `reject`

Submission-package note
-----------------------

The official validation flow expects the resulting tarball to be signed and
encrypted before submission to NIST. That signing and encryption step is part of
the native MINEX process and should be documented, even if the final project
does not automate it yet.
