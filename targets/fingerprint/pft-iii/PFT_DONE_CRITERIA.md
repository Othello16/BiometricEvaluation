PFT III Done Criteria
=====================

Jupiter may mark `PFT III` complete only when every item below is satisfied.

1. Official source pinning is complete
--------------------------------------

 * exact `usnistgov/pft` source reference recorded
 * exact validation package version recorded
 * checksums recorded for all public artifacts used

2. Official interface is identified
-----------------------------------

 * `pftiii/include/pftiii.h` reviewed
 * required interface methods identified:
   * `getIdentification`
   * `createProprietaryTemplate`
   * `compareProprietaryTemplates`
   * `getImplementation`
 * official shared-library naming convention identified
 * official `lib/`, `config/`, and imagery layout identified

3. Vendor intake is complete
----------------------------

 * [VENDOR_QUESTIONNAIRE.md](./VENDOR_QUESTIONNAIRE.md) completed
 * [VENDOR_INTAKE_CHECKLIST.md](./VENDOR_INTAKE_CHECKLIST.md) completed
 * [VENDOR_ARTIFACT_MANIFEST_TEMPLATE.yaml](./VENDOR_ARTIFACT_MANIFEST_TEMPLATE.yaml) completed

4. PFT fit decision is explicit
-------------------------------

 * vendor is confirmed to be proprietary-template oriented
   or
 * vendor is explicitly rejected from PFT and rerouted elsewhere

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
   * `id.log`
   * `createProprietaryTemplate.log`
   * `compareProprietaryTemplates.log`
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

9. Containerization is deferred until after native proof
--------------------------------------------------------

 * no container envelope is treated as proof of PFT compatibility
 * the native PFT result is the source of truth
 * any later container envelope does not change the PFT-facing behavior
