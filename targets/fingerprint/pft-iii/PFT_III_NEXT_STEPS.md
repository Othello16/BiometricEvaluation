PFT III Next Steps After MINEX
==============================

Enter `PFT III` when one of these is true:

 * `MINEX III` has been fully completed and documented
 * the vendor does not fit the interoperable-template model and belongs in the
   proprietary-template path

What Jupiter should carry forward from MINEX
--------------------------------------------

 * vendor identity and version
 * artifact manifest and checksums
 * dependency inventory
 * build and runtime assumptions
 * any evidence showing the vendor is proprietary-template oriented
 * any evidence showing the vendor cannot map cleanly to the MINEX interface

Immediate PFT III tasks
-----------------------

1. Pull the public PFT III materials and record the exact source references.
2. Identify the exact PFT III API and packaging expectations.
3. Determine whether the vendor provides separate extractor and matcher
   libraries as expected by the PFT path.
4. Create the PFT-specific vendor intake checklist and native validation path.
5. Keep all PFT assumptions separate from MINEX assumptions.

Do not carry over from MINEX without confirmation
-------------------------------------------------

 * template format assumptions
 * interoperability assumptions
 * MINEX API signatures
 * MINEX validation scripts
 * MINEX log-file semantics
