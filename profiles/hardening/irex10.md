IREX 10 Hardened Build Profile
==============================

Public references indicate that IREX 10 uses an official API and CONOPS
document, a validation flow, and public submission guidance.

Profile notes
-------------

 * treat the official IREX 10 API and validation flow as binding
 * preserve the submitted-library model end to end
 * do not swap the interface for a service wrapper
 * pin the runtime base image and toolchain after validation succeeds

Primary risks
-------------

 * eye-image modality mismatch
 * hidden dynamic library dependencies
 * drift from the officially documented validation environment
