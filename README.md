NIST Compatibility Kit for Jupiter
==================================

This repository is a compatibility kit for running vendor biometric submissions
against NIST evaluation interfaces under a hardened deployment model.

Primary goal:

 * make vendor implementations plug into the correct NIST evaluation interface
 * surface incompatibilities before containerization hides them
 * use containers only as delivery and runtime envelopes around native
   NIST-compatible binaries

Start here:

 * [PRD.md](./PRD.md)
 * [COMPATIBILITY_MATRIX.md](./COMPATIBILITY_MATRIX.md)
 * [RUNBOOK.md](./RUNBOOK.md)

Repo usage note:

 * this repository is the durable instruction and compatibility repo
 * temporary upstream clones of public NIST repos may be used during local
   verification, but they are disposable working copies and are not part of the
   deliverable

Supported Phase 1 targets:

 * Face:
   * [FRVT 1:1](./targets/face/frvt-11/README.md)
   * [FRVT 1:N](./targets/face/frvt-1n/README.md)
   * [FRVT Age Estimation](./targets/face/frvt-age/README.md)
   * [FRVT Morph](./targets/face/frvt-morph/README.md)
   * [FRVT Quality](./targets/face/frvt-quality/README.md)
   * [FRVT Five](./targets/face/frvt-five/README.md)
   * [FRVT Twins](./targets/face/frvt-twins/README.md)
 * Iris:
   * [IREX 10 Identification](./targets/iris/irex10/README.md)
 * Fingerprint:
   * [MINEX III](./targets/fingerprint/minex-iii/README.md)
   * [PFT III](./targets/fingerprint/pft-iii/README.md)

Fingerprint routing note for Jupiter:

 * standardized or interoperable `10-print` minutiae-template workflows start in
   [MINEX III](./targets/fingerprint/minex-iii/README.md)
 * proprietary `10-print` extractor or matcher library workflows start in
   [PFT III](./targets/fingerprint/pft-iii/README.md)

Hardening references:

 * [Common Hardened Build Profile](./profiles/hardening/common.md)
 * [FRVT Build Profile](./profiles/hardening/frvt-family.md)
 * [IREX 10 Build Profile](./profiles/hardening/irex10.md)
 * [MINEX III Build Profile](./profiles/hardening/minex-iii.md)
 * [PFT III Build Profile](./profiles/hardening/pft-iii.md)

Containerization references:

 * [NIST Envelope Container Pattern](./packaging/nist-envelope/README.md)
 * [Vendor Submission Manifest Template](./packaging/templates/vendor-submission-manifest.yaml)

Archived prototype REST scaffolds were moved out of the main path:

 * [archive/prototype-rest](./archive/prototype-rest)
