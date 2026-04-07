NIST Compatibility Matrix
=========================

This matrix defines the exact phase-1 submission targets and what a vendor must
provide to be considered plug-compatible with this repository.

| Target | Modality | Official public source | Expected vendor artifact shape | Native interface required | Phase 1 status |
| --- | --- | --- | --- | --- | --- |
| FRVT 1:1 | Face | `usnistgov/frvt` | compiled SDK/library plus target-specific validation package inputs | Yes | Supported |
| FRVT 1:N | Face | `usnistgov/frvt` | compiled SDK/library plus target-specific validation package inputs | Yes | Supported |
| FRVT Age Estimation | Face | `usnistgov/frvt` | compiled SDK/library plus target-specific validation package inputs | Yes | Supported |
| FRVT Morph | Face | `usnistgov/frvt` | compiled SDK/library plus target-specific validation package inputs | Yes | Supported |
| FRVT Quality | Face | `usnistgov/frvt` | compiled SDK/library plus target-specific validation package inputs | Yes | Supported |
| FRVT Five | Face | `usnistgov/frvt` | compiled SDK/library plus target-specific validation package inputs | Yes | Supported |
| FRVT Twins | Face | `usnistgov/frvt` | compiled SDK/library plus target-specific validation package inputs | Yes | Supported |
| IREX 10 Identification | Iris | `pages.nist.gov/IREX10` and `JRMatey-NIST/IREX10` | submitted library validated with official API and `validate.sh` flow | Yes | Supported |
| MINEX III | Fingerprint | `usnistgov/minex` | standardized or interoperable fingerprint template extractor/matcher implementation matching MINEX API, including 10-print minutiae-template workflows | Yes | Supported |
| PFT III | Fingerprint | `pages.nist.gov/pft/results/pftiii` | proprietary feature extractor and template matcher libraries matching PFT API, including proprietary 10-print stacks | Yes | Supported |

Interpretation
--------------

“Plug-compatible” in this repo means:

 * the vendor ships the exact native interface required by the target
 * the vendor artifact can be validated with the official public package or
   package pattern for that target
 * any container image wraps that native interface without replacing it

It does not mean:

 * any arbitrary matcher can be fronted with a REST service and treated as NIST
   compatible
 * a modality-level wrapper can stand in for a target-specific API
 * vendor installation instructions alone are sufficient for a hardened
   environment

Fingerprint routing note
------------------------

Use `MINEX III` first when the vendor delivers:

 * interoperable minutiae templates
 * standardized 10-print template generation
 * template-level extraction and matching intended to conform to MINEX rules

Use `PFT III` when the vendor delivers:

 * proprietary fingerprint templates
 * separate proprietary extractor and matcher libraries
 * a fingerprint stack intended for PFT-style proprietary-template evaluation
