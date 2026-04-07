MINEX III Done Criteria
=======================

Jupiter may mark `MINEX III` complete and move to `PFT III` only when every
item below is satisfied.

1. Official source pinning is complete
--------------------------------------

 * exact `usnistgov/minex` source reference recorded
 * exact `MINEX III Validation (201907011032)` reference recorded
 * exact `usnistgov/nbisminexiii` reference recorded if used
 * checksums recorded for all public artifacts used

2. Official interface is identified
-----------------------------------

 * `minexiii/validation/minexiii.h` reviewed
 * required API functions identified:
   * `get_pids`
   * `create_template`
   * `match_templates`
 * official library naming convention identified
 * official `lib/` and `config/` layout identified

3. Vendor intake is complete
----------------------------

 * [VENDOR_QUESTIONNAIRE.md](./VENDOR_QUESTIONNAIRE.md) completed
 * [VENDOR_INTAKE_CHECKLIST.md](./VENDOR_INTAKE_CHECKLIST.md) completed
 * [VENDOR_ARTIFACT_MANIFEST_TEMPLATE.yaml](./VENDOR_ARTIFACT_MANIFEST_TEMPLATE.yaml) completed

4. MINEX fit decision is explicit
---------------------------------

 * vendor is confirmed to be interoperable-template oriented
   or
 * vendor is explicitly rejected from MINEX and rerouted to `PFT III`

5. Native build is reproducible
-------------------------------

 * build commands are recorded
 * compiler and runtime versions are recorded
 * dependencies are known and checksummed
 * produced artifacts are identified precisely

6. Official validation runs successfully
----------------------------------------

 * validation performed with the official `./validate` flow
 * expected logs are generated:
   * `compile.log`
   * `cbeff.log`
   * `create.log`
   * `match.log`
 * templates are generated
 * submission archive is generated
 * exit code and logs are preserved

7. Validation findings are captured
-----------------------------------

 * all interface mismatches are listed
 * all runtime-library issues are listed
 * all nondeterminism or environment issues are listed
 * final recommendation is one of:
   * `proceed`
   * `hold`
   * `reject`

8. Runtime artifact set is frozen
---------------------------------

 * validated binaries are frozen
 * dependent shared libraries are frozen
 * config files are frozen
 * mutable runtime assumptions are eliminated or documented

9. Handoff decision is made
---------------------------

Move to `PFT III` only if one of the following is true:

 * `MINEX III` is complete and documented
 * vendor is clearly proprietary-template oriented and should be evaluated
   through `PFT III` instead

10. Containerization is deferred until after native proof
---------------------------------------------------------

 * no container envelope is treated as proof of MINEX compatibility
 * the native MINEX result is the source of truth
 * any later container envelope does not change the MINEX-facing behavior
