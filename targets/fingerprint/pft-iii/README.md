PFT III Target Brief
====================

Official public sources:

 * `https://pages.nist.gov/pft/results/pftiii/`
 * `https://github.com/usnistgov/pft`
 * `https://github.com/usnistgov/pft/tree/master/pftiii`
 * public result pages show API versioning, shipped library inventories, and
   tested Linux baselines for participant submissions
 * public API and test plan:
   `https://pages.nist.gov/pft/doc/pftiii/testplan.pdf`

Target model:

 * proprietary fingerprint template evaluation
 * vendor must conform to the PFT III API and package expectations
 * this is not the default starting path for standardized 10-print template
   interoperability work

Use this path when:

 * the vendor delivers proprietary fingerprint templates
 * the vendor packages separate proprietary extractor and matcher libraries
 * the target is explicitly a PFT-style proprietary-template submission

Public technical anchors
------------------------

 * official validation package path:
   `pftiii/validation/`
 * official API header:
   `pftiii/include/pftiii.h`
 * starter implementation examples:
   `pftiii/nullimpl/` and `pftiii/mineximpl/`

Jupiter tasks:

 * preserve extractor and matcher library packaging expected by the target
 * capture all auxiliary libraries and checksums in the manifest
 * validate natively before building the container envelope
 * keep PFT assumptions separate from MINEX assumptions
 * use the official `pftiii/validation` package as the native validation anchor
