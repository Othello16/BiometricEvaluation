MINEX III Execution Status
==========================

Purpose
-------

This file records what was actually attempted locally against the public MINEX
III materials and what blocked full end-to-end execution.

What was completed
------------------

 * Cloned the public `usnistgov/minex` repository into a temporary working copy.
 * Cloned the public `usnistgov/nbisminexiii` wrapper into a temporary working
   copy.
 * Built the public `nbisminexiii` wrapper libraries successfully enough to
   produce:
   * `libminexiii_nbisminexiii_5002.so`
   * `libmindtct.so`
   * `libincits.so`
   * `libbozorth3.so`
 * Staged those libraries into the official `minexiii/validation/lib/`
   directory.
 * Ran the official `./validate` script on the host and captured the first
   blocker.
 * Attempted a temporary `centos:7` container path to avoid changing the host.

Observed blockers
-----------------

Host run blocker:

 * The validator failed immediately because it requires `which` and `yum`,
   which is consistent with its CentOS-oriented native baseline.

Containerized run blockers:

 * The public `centos:7` image resolves to `CentOS Linux release 7.9.2009`,
   while the official MINEX III validation package requires
   `CentOS Linux release 7.6.1810 (Core)`.
 * Attempting to install the required packages in the temporary container failed
   because the public CentOS 7 mirrorlist could not be resolved, so `yum`
   could not find a valid baseurl for `base/7/x86_64`.

Useful public observation
-------------------------

Unlike PFT III, the public `minex` repository already includes
`minexiii/validation/validation_imagery_raw/`, so missing imagery was not the
first blocker here.

What this means
---------------

The public reference wrapper was built successfully, but full official MINEX III
validation was not completed in this environment because:

 * the host is not a CentOS/yum validation baseline
 * the disposable CentOS path did not have a working package-install route
 * the validator expects an older exact OS baseline than the public image

Current recommendation
----------------------

To complete official MINEX III validation, use this order:

1. exact CentOS `7.6.1810` validation environment or an approved equivalent
2. install the validator's required packages
3. run `./validate` natively
4. only after that, package the validated artifact into the container envelope
