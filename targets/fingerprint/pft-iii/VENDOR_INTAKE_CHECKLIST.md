PFT III Vendor Intake Checklist
===============================

Purpose
-------

Use this checklist before any build or packaging work. The goal is to determine
whether a vendor deliverable can plausibly map to the PFT III interface.

Authoritative public references
-------------------------------

 * `https://github.com/usnistgov/pft`
 * `https://github.com/usnistgov/pft/tree/master/pftiii`
 * `https://github.com/usnistgov/pft/blob/master/pftiii/validation/README.md`
 * `https://github.com/usnistgov/pft/blob/master/pftiii/include/pftiii.h`
 * public test plan:
   `https://pages.nist.gov/pft/doc/pftiii/testplan.pdf`

Required vendor inputs
----------------------

The vendor must provide:

 * exact product name and version
 * exact shared library file list
 * target CPU architecture
 * required operating system and runtime assumptions
 * compiler and standard library assumptions
 * dependency inventory, including transitive shared libraries
 * checksums for every shipped binary
 * build or install instructions for controlled Linux
 * configuration files required for the PFT III path

PFT-specific compatibility questions
------------------------------------

Jupiter should ask and record:

 * Does the deliverable produce proprietary templates rather than standardized
   interoperable minutiae templates?
 * Can the vendor implement the PFTIII::Interface contract in a shared library?
 * Can the deliverable support `getIdentification()`?
 * Can the deliverable support `createProprietaryTemplate()`?
 * Can the deliverable support `compareProprietaryTemplates()`?
 * Can the implementation be instantiated via
   `PFTIII::Interface::getImplementation(configurationDirectory)`?
 * Can the library link under `g++` / `mpicxx` on Ubuntu Server 24.04.3 LTS?
 * Can the software operate without network access?
 * Can the software operate without license servers, dongles, activation, or
   machine-bound rights management?
 * Can the software avoid reading or writing outside the provided read-only
   configuration directory?
 * Can the software handle variable-resolution and unknown-metadata images?
 * Can the software tolerate blank, gradient, contactless, and atypical images
   described by the validation package?

Reject or escalate if
---------------------

 * the vendor cannot provide a shared-library implementation of the PFT III API
 * the vendor requires network access at runtime
 * the vendor requires privileged execution
 * the vendor requires machine-specific license control
 * the vendor cannot provide dependency and checksum inventory
 * the vendor cannot support batch, non-interactive execution

Record of evidence
------------------

Create and retain:

 * vendor artifact manifest
 * dependency manifest
 * checksums
 * build notes
 * exact answers to the compatibility questions above
