MINEX III Hardened Build Profile
================================

MINEX III is a separate fingerprint target and must not be merged with PFT III.

Profile notes
-------------

 * treat the MINEX API and interoperability rules as target-specific
 * preserve minutiae-template semantics exactly
 * isolate any fingerprint image pre-processing from the MINEX interface unless
   the official target package explicitly allows it

Primary risks
-------------

 * confusing template interoperability with proprietary matching interfaces
 * hidden assumptions about template encoding or record formats
 * non-portable dynamic library packaging
