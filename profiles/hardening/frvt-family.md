FRVT Family Hardened Build Profile
==================================

Applies to:

 * FRVT 1:1
 * FRVT 1:N
 * FRVT Age Estimation
 * FRVT Morph
 * FRVT Quality
 * FRVT Five
 * FRVT Twins

Profile notes
-------------

 * treat the target-specific package under `usnistgov/frvt` as the source of
   truth for API, packaging, and validation
 * normalize vendor deliverables to the exact FRVT target package before any
   container work
 * freeze compiler, libc, and dependent library versions once validation passes
 * ensure the container envelope does not replace the FRVT-facing binary

Primary risks
-------------

 * target-specific FRVT differences being hidden behind one internal wrapper
 * incompatible vendor shared-library dependencies
 * glibc or compiler drift between validation and hardened runtime images
