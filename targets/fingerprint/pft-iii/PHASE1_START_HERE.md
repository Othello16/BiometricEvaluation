PFT III Phase 1 Start Here
==========================

Jupiter should treat `PFT III` as the fingerprint path for proprietary template
submissions.

Why
---

 * `PFT III` is the proprietary-template evaluation path.
 * It is distinct from `MINEX III`, which is the interoperable-template path.
 * Vendors that cannot map cleanly to the MINEX template interface should be
   evaluated here instead.

Immediate Phase 1 tasks
-----------------------

1. Pull the official `usnistgov/pft` materials.
2. Pin the exact `pftiii/validation` package version and API version.
3. Send or complete [VENDOR_QUESTIONNAIRE.md](./VENDOR_QUESTIONNAIRE.md).
4. Fill out [VENDOR_INTAKE_CHECKLIST.md](./VENDOR_INTAKE_CHECKLIST.md).
5. Follow [NATIVE_VALIDATION_PLAYBOOK.md](./NATIVE_VALIDATION_PLAYBOOK.md).
6. Define the native build assumptions before any container packaging.
7. Record every mismatch between vendor deliverables and the PFT III interface.
8. Close the target only when [PFT_DONE_CRITERIA.md](./PFT_DONE_CRITERIA.md) is
   satisfied.

What makes PFT different from MINEX
-----------------------------------

 * proprietary templates are expected
 * the interface is C++20 and object-oriented
 * images can have variable resolutions, including 500 PPI and 1000 PPI
 * the library must not require terminal interaction, network access, or
   machine-specific licensing controls
