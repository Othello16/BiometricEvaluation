Execution Runbook
=================

Execution Order
---------------

1. Choose the exact target, not just the modality.
2. Obtain the official public target package or reference repo.
3. Normalize vendor deliverables into the target-specific compatibility path.
4. Build and validate the native implementation first.
5. Only after native validation succeeds, package it into a hardened container
   envelope.

Jupiter Workflow
----------------

For any target:

1. Read the target brief in `targets/...`.
2. Read the family hardening profile in `profiles/hardening/...`.
3. Compare vendor deliverables against `COMPATIBILITY_MATRIX.md`.
4. Build the vendor implementation outside the container envelope if needed.
5. Run the official validation flow for that target.
6. Package the validated binary and dependencies into the container envelope.
7. Record any deviations or unresolved blockers.

MINEX III first path for 10-print work
--------------------------------------

If the request is for standardized or interoperable `10-print` fingerprint
template work:

1. Start in [targets/fingerprint/minex-iii/PHASE1_START_HERE.md](./targets/fingerprint/minex-iii/PHASE1_START_HERE.md).
2. Use [VENDOR_INTAKE_CHECKLIST.md](./targets/fingerprint/minex-iii/VENDOR_INTAKE_CHECKLIST.md).
3. Send or complete [VENDOR_QUESTIONNAIRE.md](./targets/fingerprint/minex-iii/VENDOR_QUESTIONNAIRE.md).
4. Follow [NATIVE_VALIDATION_WORKFLOW.md](./targets/fingerprint/minex-iii/NATIVE_VALIDATION_WORKFLOW.md).
5. Execute [NATIVE_VALIDATION_PLAYBOOK.md](./targets/fingerprint/minex-iii/NATIVE_VALIDATION_PLAYBOOK.md).
6. Close `MINEX III` only when [MINEX_DONE_CRITERIA.md](./targets/fingerprint/minex-iii/MINEX_DONE_CRITERIA.md) is satisfied.
7. Do not move to `PFT III` unless the vendor stack is proprietary-template
   oriented rather than interoperable-template oriented.

PFT III path for proprietary template work
------------------------------------------

If the request is for proprietary fingerprint template evaluation:

1. Start in [targets/fingerprint/pft-iii/PHASE1_START_HERE.md](./targets/fingerprint/pft-iii/PHASE1_START_HERE.md).
2. Use [VENDOR_INTAKE_CHECKLIST.md](./targets/fingerprint/pft-iii/VENDOR_INTAKE_CHECKLIST.md).
3. Send or complete [VENDOR_QUESTIONNAIRE.md](./targets/fingerprint/pft-iii/VENDOR_QUESTIONNAIRE.md).
4. Follow [NATIVE_VALIDATION_WORKFLOW.md](./targets/fingerprint/pft-iii/NATIVE_VALIDATION_WORKFLOW.md).
5. Execute [NATIVE_VALIDATION_PLAYBOOK.md](./targets/fingerprint/pft-iii/NATIVE_VALIDATION_PLAYBOOK.md).
6. Close `PFT III` only when [PFT_DONE_CRITERIA.md](./targets/fingerprint/pft-iii/PFT_DONE_CRITERIA.md) is satisfied.

Do Not Do This
--------------

 * Do not replace the native interface with a web API.
 * Do not let runtime containers fetch internet dependencies.
 * Do not install host packages unless the impact is understood and approved.
 * Do not assume one modality-level process supports every NIST target in that
   modality.
 * Do not assume vendor install docs satisfy hardened environment controls.

System-impact warning
---------------------

Before changing the host system, prefer this order:

1. disposable working directory
2. temporary container matching the official validation baseline
3. host package changes only if isolation is not feasible

Python virtual environments are useful for Python-only tooling, but they do not
solve the OS-package and exact-runtime requirements of NIST native validation
packages.

Validation Order
----------------

1. Native compile and dependency resolution
2. Official target validation package execution
3. Controlled runtime smoke check
4. Container envelope validation
5. Audit log and manifest capture

Issue Capture
-------------

If Jupiter finds a blocker, capture:

 * target name
 * exact upstream package used
 * vendor artifact version and checksum
 * host OS and compiler/runtime versions
 * failing command
 * exact stderr/stdout excerpt
 * whether the problem is interface, build, runtime, or hardening related
