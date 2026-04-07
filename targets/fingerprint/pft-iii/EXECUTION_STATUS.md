PFT III Execution Status
========================

Purpose
-------

This file records what was actually attempted locally against the public PFT III
materials and what blocked full end-to-end execution.

What was completed
------------------

 * Cloned the public `usnistgov/pft` repository into a temporary working copy.
 * Built the public `pftiii/nullimpl` reference library successfully using:
   * `cmake 3.28.3`
   * `g++ 13.3.0`
 * Produced these native reference artifacts:
   * `libpftiii_nullimpl_0001.so`
   * `libpftiii.so`
 * Staged those libraries into the official `pftiii/validation/lib/` directory.
 * Ran the official `./validate` script on the host and captured the first
   blocker.

Observed blockers
-----------------

Host run blocker:

 * The validator failed immediately because `gawk` was not installed.

Containerized run blockers:

 * A temporary Docker container was used to avoid changing host packages.
 * The available public `ubuntu:24.04` image resolves to `Ubuntu 24.04.4 LTS`,
   while the official PFT III validation package requires
   `Ubuntu 24.04.3 LTS`.
 * Package installation inside the temporary container stalled while contacting
   Ubuntu mirrors, so the validation prerequisites were not fully installed.

Unavoidable public-data blocker:

 * The official PFT III validation imagery is not in GitHub.
 * NIST requires it to be requested separately from:
   `https://nigos.nist.gov/datasets/pftiii_validation/request`

What this means
---------------

The public reference library was built successfully, but full official PFT III
validation was not completed in this environment because:

 * the host was missing required validation packages
 * the disposable container did not match the exact validator OS baseline
 * the required validation imagery was not available locally

Current recommendation
----------------------

To complete official PFT III validation, use this order:

1. exact Ubuntu Server `24.04.3 LTS` validation environment
2. install the validator's required Ubuntu packages
3. obtain the official validation imagery from NIST
4. run `./validate` natively
5. only after that, package the validated artifact into the container envelope
