MINEX III Phase 1 Start Here
============================

Jupiter should treat `MINEX III` as the first fingerprint target when the work
is about `10-print` template compatibility.

Why
---

 * `MINEX III` is the interoperability path.
 * Standardized or interoperable 10-print minutiae-template workflows belong
   here first.
 * `PFT III` remains in scope, but only for proprietary-template stacks.

Immediate Phase 1 tasks
-----------------------

1. Pull the official `usnistgov/minex` materials.
2. Identify the exact public API, record format, and validation flow.
3. Send or complete [VENDOR_QUESTIONNAIRE.md](./VENDOR_QUESTIONNAIRE.md).
4. Fill out [VENDOR_INTAKE_CHECKLIST.md](./VENDOR_INTAKE_CHECKLIST.md).
5. Follow [NATIVE_VALIDATION_PLAYBOOK.md](./NATIVE_VALIDATION_PLAYBOOK.md).
6. Define the native build assumptions before any container packaging.
7. Record every mismatch between vendor deliverables and the MINEX interface.
8. Close the target only when [MINEX_DONE_CRITERIA.md](./MINEX_DONE_CRITERIA.md)
   is satisfied.

What Jupiter must ask of a vendor
---------------------------------

 * exact library or binary names
 * supported template formats
 * required compiler and runtime versions
 * dependency list and checksums
 * build instructions for a controlled Linux environment
 * any assumptions about 500 ppi or 10-print source imagery

Stop conditions
---------------

Do not move to container packaging until:

 * the MINEX interface is identified precisely
 * the vendor deliverable is mapped cleanly to that interface
 * native validation is understood and reproducible
