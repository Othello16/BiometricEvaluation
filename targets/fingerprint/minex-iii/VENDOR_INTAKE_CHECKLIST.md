MINEX III Vendor Intake Checklist
=================================

Purpose
-------

Use this checklist before any build or packaging work. The goal is to determine
whether a vendor deliverable can plausibly map to the MINEX III interface.

Authoritative public references
-------------------------------

 * `https://github.com/usnistgov/minex`
 * public release anchor: `MINEX III Validation (201907011032)`
 * reference wrapper example: `https://github.com/usnistgov/nbisminexiii`

Required vendor inputs
----------------------

The vendor must provide:

 * exact product name and version
 * exact library names and file list
 * target CPU architecture
 * required operating system and runtime assumptions
 * compiler and standard library assumptions
 * dependency inventory, including transitive shared libraries
 * checksums for every shipped binary
 * build or install instructions for controlled Linux
 * configuration files required for the MINEX path

MINEX-specific compatibility questions
--------------------------------------

Jupiter should ask and record:

 * Does the deliverable generate interoperable minutiae templates?
 * Which template standards are claimed or supported?
 * Is the deliverable intended for ANSI or ISO style minutiae-template output?
 * Can the deliverable participate at the template level rather than only as an
   opaque end-to-end matcher?
 * Does the deliverable expose separate extractor and matcher behavior?
 * Are there hard assumptions about 500 ppi input or tenprint source imagery?
 * Are there image preprocessing steps that alter interoperability semantics?
 * Does the vendor rely on licenses, daemons, or network calls at runtime?

Reject or escalate if
---------------------

 * the vendor cannot describe the template format
 * the vendor can only provide a proprietary end-to-end stack
 * the vendor requires uncontrolled internet access at runtime
 * the vendor requires privileged container execution
 * the vendor cannot provide dependency and checksum inventory

Record of evidence
------------------

Create and retain:

 * vendor artifact manifest
 * dependency manifest
 * checksums
 * build notes
 * exact answers to the compatibility questions above
