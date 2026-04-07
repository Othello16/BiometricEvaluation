NIST Compatibility Kit for Jupiter
==================================

This repository is the durable instruction and compatibility repo for preparing
vendor biometric submissions against public NIST evaluation interfaces under a
hardened deployment model.

Issues Found
------------

These are the main issues surfaced while turning this repo into an execution
kit:

 * There is no single universal "NIST harness" for all modalities. Actual
   submission interfaces are target-specific.
 * `MINEX III` and `PFT III` are not interchangeable:
   * `MINEX III` is for interoperable minutiae-template work, including
     standardized or interoperable `10-print` template workflows.
   * `PFT III` is for proprietary fingerprint template submissions.
 * Official native validation baselines are older and stricter than the final
   hardened deployment target:
   * `MINEX III` validation expects `CentOS 7.6.1810`.
   * `PFT III` validation expects `Ubuntu Server 24.04.3 LTS`.
 * The target validation environments do not line up cleanly with a final
   `RHEL 9` compatible hardened runtime, so validation and packaging must be
   treated as separate stages.
 * Public reference builds can be created, but full official validation is still
   gated by target-specific system assumptions:
   * `PFT III` additionally requires NIST-provided validation imagery that is
     not included in GitHub.
   * `MINEX III` validation is tightly tied to a CentOS/yum workflow.
 * Containers are useful only as runtime envelopes around already validated
   native binaries. They are not proof of NIST compatibility by themselves.

What This Repo Is
-----------------

Use this repo to:

 * choose the exact NIST evaluation target
 * understand the native submission contract for that target
 * intake vendor artifacts in a controlled way
 * validate the native implementation first
 * package the validated native artifact into a hardened container envelope

Do not use this repo as:

 * a generic biometric matcher host
 * a REST-first integration layer
 * proof that a vendor is NIST-compatible without native validation

How To Navigate This Repo
-------------------------

Read the repo in this order:

1. Start with the overall scope:
   * [PRD.md](./PRD.md)
   * [COMPATIBILITY_MATRIX.md](./COMPATIBILITY_MATRIX.md)
   * [RUNBOOK.md](./RUNBOOK.md)

2. Read the common hardening rules:
   * [profiles/hardening/common.md](./profiles/hardening/common.md)

3. Choose the exact target path, not just the modality:
   * Face:
     * [targets/face/frvt-11/README.md](./targets/face/frvt-11/README.md)
     * [targets/face/frvt-1n/README.md](./targets/face/frvt-1n/README.md)
     * [targets/face/frvt-age/README.md](./targets/face/frvt-age/README.md)
     * [targets/face/frvt-morph/README.md](./targets/face/frvt-morph/README.md)
     * [targets/face/frvt-quality/README.md](./targets/face/frvt-quality/README.md)
     * [targets/face/frvt-five/README.md](./targets/face/frvt-five/README.md)
     * [targets/face/frvt-twins/README.md](./targets/face/frvt-twins/README.md)
   * Iris:
     * [targets/iris/irex10/README.md](./targets/iris/irex10/README.md)
   * Fingerprint:
     * [targets/fingerprint/minex-iii/README.md](./targets/fingerprint/minex-iii/README.md)
     * [targets/fingerprint/pft-iii/README.md](./targets/fingerprint/pft-iii/README.md)

4. For fingerprint, choose the correct path explicitly:
   * standardized or interoperable `10-print` minutiae-template workflows start
     in [targets/fingerprint/minex-iii/PHASE1_START_HERE.md](./targets/fingerprint/minex-iii/PHASE1_START_HERE.md)
   * proprietary `10-print` extractor or matcher library workflows start in
     [targets/fingerprint/pft-iii/PHASE1_START_HERE.md](./targets/fingerprint/pft-iii/PHASE1_START_HERE.md)

5. Inside a target directory, follow this order:
   * target `README.md`
   * `PHASE1_START_HERE.md`
   * `VENDOR_QUESTIONNAIRE.md`
   * `VENDOR_INTAKE_CHECKLIST.md`
   * `NATIVE_VALIDATION_WORKFLOW.md`
   * `NATIVE_VALIDATION_PLAYBOOK.md`
   * `*_DONE_CRITERIA.md`
   * `EXECUTION_STATUS.md` if present

6. Only after native validation is understood, use the container-envelope
   examples:
   * [packaging/nist-envelope/README.md](./packaging/nist-envelope/README.md)
   * [packaging/nist-envelope/pftiii-nullimpl-reference/README.md](./packaging/nist-envelope/pftiii-nullimpl-reference/README.md)
   * [packaging/nist-envelope/minexiii-nbis-reference/README.md](./packaging/nist-envelope/minexiii-nbis-reference/README.md)

Fingerprint Paths
-----------------

`MINEX III`

 * Use for interoperable minutiae-template work.
 * This is the correct default starting path for standardized or interoperable
   `10-print` fingerprint template work.
 * Main files:
   * [targets/fingerprint/minex-iii/PHASE1_START_HERE.md](./targets/fingerprint/minex-iii/PHASE1_START_HERE.md)
   * [targets/fingerprint/minex-iii/NATIVE_VALIDATION_PLAYBOOK.md](./targets/fingerprint/minex-iii/NATIVE_VALIDATION_PLAYBOOK.md)
   * [targets/fingerprint/minex-iii/MINEX_DONE_CRITERIA.md](./targets/fingerprint/minex-iii/MINEX_DONE_CRITERIA.md)
   * [targets/fingerprint/minex-iii/EXECUTION_STATUS.md](./targets/fingerprint/minex-iii/EXECUTION_STATUS.md)

`PFT III`

 * Use for proprietary fingerprint template submissions.
 * Main files:
   * [targets/fingerprint/pft-iii/PHASE1_START_HERE.md](./targets/fingerprint/pft-iii/PHASE1_START_HERE.md)
   * [targets/fingerprint/pft-iii/NATIVE_VALIDATION_PLAYBOOK.md](./targets/fingerprint/pft-iii/NATIVE_VALIDATION_PLAYBOOK.md)
   * [targets/fingerprint/pft-iii/PFT_DONE_CRITERIA.md](./targets/fingerprint/pft-iii/PFT_DONE_CRITERIA.md)
   * [targets/fingerprint/pft-iii/EXECUTION_STATUS.md](./targets/fingerprint/pft-iii/EXECUTION_STATUS.md)

What Was Actually Proven
------------------------

This repo now includes real execution findings for the public fingerprint
reference paths:

 * `PFT III`:
   * public `nullimpl` reference library built successfully
   * official validation was attempted and real blockers were captured
   * a reference envelope image was built successfully
 * `MINEX III`:
   * public `nbisminexiii` reference wrapper libraries built successfully
   * official validation was attempted and real blockers were captured
   * a reference envelope image was built successfully

What was not proven here:

 * official end-to-end validation success for `MINEX III`
 * official end-to-end validation success for `PFT III`
 * validation of a real vendor library

Operational Notes
-----------------

 * This repository is the deliverable.
 * Temporary upstream clones of public NIST repos may be used during local
   verification, but they are disposable working copies and are not part of the
   final artifact.
 * Archived prototype REST scaffolds were moved out of the main path:
   [archive/prototype-rest](./archive/prototype-rest)
