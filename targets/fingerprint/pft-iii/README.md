PFT III Target Brief
====================

Official public sources:

 * `https://pages.nist.gov/pft/results/pftiii/`
 * public result pages show API versioning, shipped library inventories, and
   tested Linux baselines for participant submissions

Target model:

 * proprietary fingerprint template evaluation
 * vendor must conform to the PFT III API and package expectations
 * this is not the default starting path for standardized 10-print template
   interoperability work

Use this path when:

 * the vendor delivers proprietary fingerprint templates
 * the vendor packages separate proprietary extractor and matcher libraries
 * the target is explicitly a PFT-style proprietary-template submission

Jupiter tasks:

 * preserve extractor and matcher library packaging expected by the target
 * capture all auxiliary libraries and checksums in the manifest
 * validate natively before building the container envelope
