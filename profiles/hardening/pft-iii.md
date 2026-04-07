PFT III Hardened Build Profile
==============================

PFT III is distinct from MINEX III and should stay on a separate path.

Public PFT III result pages show submitted library inventories and runtime
metadata, including API versioning and tested Linux baselines.

Profile notes
-------------

 * preserve separate feature extractor and matcher deliverables where required
 * capture every shipped shared object and checksum in the manifest
 * validate image-format and runtime-library assumptions early

Primary risks
-------------

 * accidental mixing of PFT and MINEX assumptions
 * untracked auxiliary shared libraries
 * runtime behavior changing when moved into a hardened envelope
