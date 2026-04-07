MINEX III Target Brief
======================

Official public source:

 * `https://github.com/usnistgov/minex`
 * public release anchor: `MINEX III Validation (201907011032)`
 * reference implementation example: `https://github.com/usnistgov/nbisminexiii`

Target model:

 * minutiae interoperability evaluation
 * vendor must conform to the official MINEX III interface and interoperability
   rules
 * this is the default starting path for standardized or interoperable
   `10-print` fingerprint template work

Use this path when:

 * the vendor provides interoperable minutiae templates
 * the vendor refers to ANSI or ISO style template conformance
 * the deliverable is a 10-print template extractor or matcher intended to work
   at the template level rather than as a proprietary end-to-end stack

Do not use this path when:

 * the vendor provides a proprietary fingerprint template stack
 * the vendor ships separate proprietary extractor and matcher libraries for a
   PFT-style evaluation
 * the vendor cannot map its deliverables to the MINEX template interface

Jupiter tasks:

 * preserve template-level semantics exactly
 * keep this path separate from PFT III
 * do not reuse proprietary matching assumptions from PFT III here
 * start here first for 10-print template compatibility work
 * use the public MINEX validation release as the native validation anchor
 * use `nbisminexiii` only as a reference for API wrapping shape, not as a
   substitute for vendor deliverables
