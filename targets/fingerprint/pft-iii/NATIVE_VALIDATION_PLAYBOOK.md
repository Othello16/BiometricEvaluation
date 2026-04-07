PFT III Native Validation Playbook
==================================

Purpose
-------

This playbook is the executable companion to `NATIVE_VALIDATION_WORKFLOW.md`.
It is designed so Jupiter can run the PFT III path in a controlled way without
improvising the validation sequence.

Public anchors
--------------

 * official PFT repository: `https://github.com/usnistgov/pft`
 * official PFT III materials live under `pftiii/` in that repository
 * official validation README:
   `https://github.com/usnistgov/pft/blob/master/pftiii/validation/README.md`
 * official validation script:
   `https://github.com/usnistgov/pft/blob/master/pftiii/validation/validate`
 * official API header:
   `https://github.com/usnistgov/pft/blob/master/pftiii/include/pftiii.h`
 * public validation version anchor:
   `202508280945`
 * starter implementation examples:
   `pftiii/nullimpl/` and `pftiii/mineximpl/`

Validation-baseline note
------------------------

The public PFT III validation package requires `Ubuntu Server 24.04.3 LTS`.
That requirement applies to native validation. It does not mean the final
hardened runtime envelope should remain on Ubuntu.

Expected working directories
----------------------------

Use a structure like:

```text
pft-work/
  official/
    pft/
    pft-validation/
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

 * the exact `pft` commit, tag, or archive in use
 * the exact validation package version in use
 * the vendor artifact checksums
 * the target architecture
 * the compiler and standard-library versions
 * whether the vendor needs license files, daemons, or environment variables
 * whether the deliverable supports the PFT III API methods:
   * `getIdentification`
   * `createProprietaryTemplate`
   * `compareProprietaryTemplates`
   * `getImplementation`

Step 1: Pin public sources
--------------------------

Record in `logs/pft-source-record.txt`:

 * `pft` source URL
 * `pft` commit or release ID
 * validation package version and checksum
 * API version values if identified

Minimum commands Jupiter should run or adapt:

```bash
git clone https://github.com/usnistgov/pft.git official/pft
git -C official/pft rev-parse HEAD
```

Step 2: Inspect the official PFT III package layout
---------------------------------------------------

Jupiter must identify and record:

 * validation scripts
 * API headers
 * starter implementation examples
 * shared-library naming expectations
 * config files
 * expected input and output directories
 * exact output archive behavior
 * exact log-file names

Recommended inspection commands:

```bash
find official/pft/pftiii -maxdepth 3 -type f | sort
find official/pft/pftiii/validation -maxdepth 3 -type f | sort
```

Record the results in:

 * `logs/pftiii-official-layout.txt`

Step 3: Compare the vendor artifact to the PFT III interface
------------------------------------------------------------

Use:

 * `VENDOR_INTAKE_CHECKLIST.md`
 * `VENDOR_ARTIFACT_MANIFEST_TEMPLATE.yaml`

Jupiter must determine:

 * whether the vendor exposes proprietary template generation and comparison in
   a form the PFT III interface can use
 * whether the core library can be named as required:
   `libpftiii_<libraryIdentifier>_<VERSION>.so`
 * whether the implementation can link with the official validation driver
 * whether the runtime dependency model is acceptable for controlled deployment

Required evidence:

 * completed vendor questionnaire
 * manifest with checksums
 * explicit go/no-go decision on PFT compatibility

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
g++ --version || true
ldd --version || true
env | sort
```

Vendor-specific build commands go into:

 * `logs/pftiii-vendor-build.txt`

Step 5: Map the build output into the official PFT III validation layout
------------------------------------------------------------------------

Required official layout to prepare:

 * `official/pft/pftiii/validation/lib/`
   Contains all required participant libraries.
 * `official/pft/pftiii/validation/config/`
   Contains required config files only. It will be read-only at runtime.
 * validation imagery from NIST placed in the validation directory root as
   described by the validation README
 * exactly one core library matching the official naming convention:
   `libpftiii_<libraryIdentifier>_<VERSION>.so`

Jupiter must identify:

 * the exact shared-library file names expected by the validation package
 * the exact config-file locations expected by the validation package
 * the exact imagery package version required by the validation package
 * whether the library writes to stdout, stderr, files, or sockets

Step 6: Execute the official validation flow
--------------------------------------------

Concrete command block based on the public validation package:

```bash
cd official/pft/pftiii/validation
./validate 2>&1 | tee ../../../logs/pftiii-validation-run.txt
echo $? > ../../../logs/pftiii-validation-exit-code.txt
```

Before execution, Jupiter must first verify and write down:

 * `/etc/os-release` matches Ubuntu Server `24.04.3 LTS (Noble Numbat)`
 * required packages are installed:
   `base-files`, `binutils`, `cmake`, `coreutils`, `curl`, `dpkg`, `file`,
   `findutils`, `g++`, `gawk`, `grep`, `libc-bin`, `make`, `sed`, `tar`,
   `xz-utils`
 * no previous validation attempts exist
 * `lib/`, `config/`, and imagery are prepared correctly

Expected validation behaviors from the public package:

 * checks package and OS version
 * checks validation imagery version
 * builds the validation driver
 * checks API version compatibility
 * records identification information
 * tests `createProprietaryTemplate()`
 * tests `compareProprietaryTemplates()`
 * creates a tar.xz submission archive

Step 7: Capture pass/fail evidence
----------------------------------

At minimum, preserve:

 * validation exit code
 * generated output files
 * `compile.log`
 * `id.log`
 * `createProprietaryTemplate.log`
 * `compareProprietaryTemplates.log`
 * `run-createProprietaryTemplate.log`
 * `run-compareProprietaryTemplates.log`
 * `canary.log`
 * copied library inventory
 * copied config inventory
 * `templates/`
 * generated submission archive

Suggested commands:

```bash
find vendor/artifacts -type f -exec sha256sum {} \; | sort > manifests/vendor-artifacts.sha256
find official/pft/pftiii/validation -type f | sort > logs/pftiii-validation-output-files.txt
ldd vendor/artifacts/* > logs/pftiii-ldd.txt 2>&1 || true
find official/pft/pftiii/validation -maxdepth 1 -type f -name '*.tar.xz' | sort > logs/pftiii-submission-archives.txt
```

Step 8: Decide whether to proceed to container envelope packaging
-----------------------------------------------------------------

Proceed only if:

 * the vendor build is reproducible
 * the PFT III validation flow is reproducible
 * the interface mapping is explicit and documented
 * all runtime dependencies are known and pinned

Do not proceed if:

 * the validation flow is still partially guessed
 * the vendor requires uncontrolled host mutation
 * runtime libraries or licensing dependencies remain untracked
 * the vendor depends on network or machine-bound rights management

Phase 1 outputs Jupiter should commit
-------------------------------------

 * completed vendor questionnaire
 * completed vendor artifact manifest
 * source record
 * native build log
 * validation run log
 * interface mismatch notes
 * recommendation: `proceed`, `hold`, or `reject`
