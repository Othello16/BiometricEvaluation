# MINEX III 10-Print Evaluation — File Index & Implementation Summary

> Generated: 2026-04-07 | Source: `Othello16/BiometricEvaluation`

---

## 1. Files Related to MINEX III 10-Print Evaluation

### Primary MINEX III Target Files
| File | Purpose |
|------|---------|
| `targets/fingerprint/minex-iii/README.md` | Target brief — when to use MINEX III vs PFT III, routing rules |
| `targets/fingerprint/minex-iii/PHASE1_START_HERE.md` | Phase 1 entry point — immediate tasks, vendor questions, stop conditions |
| `targets/fingerprint/minex-iii/NATIVE_VALIDATION_PLAYBOOK.md` | Step-by-step executable playbook: pin sources → build → validate → capture evidence |
| `targets/fingerprint/minex-iii/NATIVE_VALIDATION_WORKFLOW.md` | High-level workflow: 8-step sequence from source pinning to artifact freeze |
| `targets/fingerprint/minex-iii/MINEX_DONE_CRITERIA.md` | 10-point completion gate — every item must pass before closing MINEX III |
| `targets/fingerprint/minex-iii/VENDOR_INTAKE_CHECKLIST.md` | Pre-build checklist — confirms vendor can map to MINEX III interface |
| `targets/fingerprint/minex-iii/VENDOR_QUESTIONNAIRE.md` | Questionnaire template to send to vendors (10 sections) |
| `targets/fingerprint/minex-iii/VENDOR_ARTIFACT_MANIFEST_TEMPLATE.yaml` | YAML manifest for tracking vendor artifacts, checksums, dependencies, validation status |

### Supporting / Cross-Cutting Files
| File | Relevance |
|------|-----------|
| `PRD.md` | Master PRD — defines MINEX III as a Phase 1 target, security posture, design principles |
| `RUNBOOK.md` | Execution runbook — MINEX III is the **first path** for 10-print work |
| `COMPATIBILITY_MATRIX.md` | Defines what "plug-compatible" means; routes interoperable templates → MINEX III |
| `README.md` | Repo entry point with links to all targets and profiles |
| `profiles/hardening/minex-iii.md` | MINEX-specific hardening profile — template semantics, isolation from PFT III |
| `profiles/hardening/common.md` | Common hardened build profile — non-root, read-only FS, SBOM, pinned deps |
| `packaging/nist-envelope/README.md` | Container envelope pattern — wraps validated native binaries, no toolchain |
| `packaging/templates/vendor-submission-manifest.yaml` | Generic vendor submission manifest template (YAML) |
| `DISCLAIMER.md` | Legal disclaimer |
| `LICENSE.md` | License |

### External NIST Resources (Upstream — Not in This Repo)
| Resource | URL |
|----------|-----|
| Official MINEX repo | `https://github.com/usnistgov/minex` |
| MINEX III API header (`minexiii.h`) | `usnistgov/minex/minexiii/validation/minexiii.h` |
| Validation driver source | `usnistgov/minex/minexiii/validation/minexiii_validation.cpp` |
| Validation script (`./validate`) | `usnistgov/minex/minexiii/validation/validate` |
| Reference wrapper (NBIS) | `https://github.com/usnistgov/nbisminexiii` |
| MINEX III participation page | `https://www.nist.gov/itl/iad/image-group/participation-minex-iii` |
| MINEX III test plan PDF | `usnistgov/minex/minexiii/testplan.pdf` |

---

## 2. High-Level Understanding of the MINEX III 10-Print Evaluation

### What MINEX III Actually Is
MINEX III (Minutia Interoperability Exchange III) is a NIST evaluation that tests whether a fingerprint algorithm can:

1. **Extract** standardized minutiae templates from raw 500 PPI fingerprint images (all 10 fingers)
2. **Match** those templates against other interoperable templates — not just its own
3. Produce templates conforming to **ANSI/INCITS 378-2004** (the interoperability standard)

The key word is **interoperable** — templates from vendor A must be matchable by vendor B. This is fundamentally different from PFT III, which tests proprietary template stacks.

### The Three API Functions
The entire MINEX III interface is defined in `minexiii.h` and consists of exactly **three C functions**:

```c
int32_t get_pids(uint32_t *template_generator, uint32_t *template_matcher);
int32_t create_template(const uint8_t *raw_image, ...params..., uint8_t *output_template);
int32_t match_templates(const uint8_t *verification_template, const uint8_t *enrollment_template, float *similarity);
```

- **`get_pids`** — Returns CBEFF Product Identifiers (who made this generator/matcher)
- **`create_template`** — Takes a raw 8-bit grayscale image at 500 PPI → produces a 32–800 byte interoperable minutiae template
- **`match_templates`** — Takes two templates → outputs a similarity score (float)

### Template Constraints
- Image: 500 PPI, grayscale, 150–812 px wide, 166–1000 px tall
- Template output: 32–800 bytes, max 128 minutiae
- Must produce a valid zero-minutiae template even on failure
- All 10 finger positions supported (right thumb through left little)

### The Validation Process (What NIST Requires)
1. **Environment**: CentOS 7.6.1810 specifically (not latest CentOS, not Ubuntu, not RHEL 9)
2. **Library naming**: Must be `libminexiii_<company>_<CBEFF>.a` or `.so`
3. **Placement**: Library in `lib/`, config files in read-only `config/`
4. **Run `./validate`**: This script compiles the validation driver against your library, then:
   - Runs `minexiii_validation pid` — checks CBEFF info
   - Runs `minexiii_validation create <seed>` — generates templates from validation imagery
   - Runs `minexiii_validation match <seed>` — matches templates pairwise
5. **Outputs**: `compile.log`, `cbeff.log`, `create.log`, `match.log`, `templates/`, submission archive
6. **Sign + encrypt** the archive and upload to NIST

### This Repo's Two-Stage Approach
- **Stage A**: Prove native MINEX III compatibility on CentOS 7.6.1810 (the validation baseline)
- **Stage B**: Package the validated native binaries into a hardened RHEL 9 container envelope for production deployment — without changing any MINEX-facing behavior

---

## 3. How I Would Stand Up the Matcher (Implementation Plan)

### Phase 1: Source Pinning & Environment Setup
1. Clone `usnistgov/minex` and `usnistgov/nbisminexiii`
2. Record exact commit SHAs and checksums
3. Obtain the validation imagery from NIST (requires contacting the MINEX team)
4. Set up a CentOS 7.6.1810 build environment for native validation

### Phase 2: Vendor Integration or Custom Implementation
For a 10-print matcher serving a 10,000-template gallery, you need both:
- **Template Generator**: Extracts minutiae from raw fingerprint images
- **Template Matcher**: Compares templates and returns similarity scores

Options:
- Integrate a vendor's MINEX-compatible library
- Use NBIS (NIST's open-source reference) via `nbisminexiii` as a starting point (public domain, but not state-of-the-art accuracy)

### Phase 3: Native Validation
1. Build on CentOS 7.6.1810 with required packages
2. Name library correctly: `libminexiii_<company>_<CBEFF>.so`
3. Run `./validate` — capture all logs
4. Verify deterministic template generation and matching

### Phase 4: Production Deployment on AWS

This is where the 10,000-template gallery comes in. Here's the architecture:

---

## 4. AWS Architecture for a 10,000-Template MINEX III Gallery

### Scale Context
- **10,000 templates** × 800 bytes max = **~8 MB** total gallery (fits entirely in RAM)
- This is a **small** gallery — no need for distributed search or sharding
- 10-print = 10 templates per person = **~1,000 individuals**

### Recommended Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     API Gateway                          │
│              (REST or WebSocket endpoint)                 │
└──────────────────────┬──────────────────────────────────┘
                       │
              ┌────────▼────────┐
              │   ALB (optional) │
              └────────┬────────┘
                       │
         ┌─────────────▼──────────────┐
         │     ECS Fargate Service     │
         │  ┌───────────────────────┐  │
         │  │  MINEX III Container  │  │
         │  │  (RHEL 9 envelope)    │  │
         │  │                       │  │
         │  │  • Validated native   │  │
         │  │    .so library        │  │
         │  │  • Thin API wrapper   │  │
         │  │  • Gallery in memory  │  │
         │  └───────────────────────┘  │
         └─────────────┬──────────────┘
                       │
              ┌────────▼────────┐
              │    S3 Bucket     │
              │  (template store │
              │   + raw images)  │
              └─────────────────┘
```

### Compute: ECS Fargate

| Resource | Spec | Why |
|----------|------|-----|
| **Service** | ECS Fargate | No EC2 management, scales to zero, FISMA-friendly |
| **Task CPU** | 1 vCPU | MINEX matching is single-threaded per comparison; 1 vCPU handles ~1,000+ matches/sec for this gallery size |
| **Task Memory** | 2 GB | Gallery is ~8 MB; rest for the OS, wrapper process, and template creation buffers |
| **Container Image** | RHEL 9 UBI minimal + validated native .so | Hardened, non-root, read-only rootfs |
| **Desired Count** | 1 (scale to 2–3 for availability) | 10K templates is trivially small |

**Estimated cost**: ~$30–50/month for a single always-on task

### Storage

| Resource | Purpose | Cost |
|----------|---------|------|
| **S3** | Persistent template gallery storage, raw image archive, audit logs | < $1/month for 8 MB + images |
| **EFS** (optional) | Shared config/gallery mount if multiple tasks need it | ~$3/month |
| **DynamoDB** (optional) | Enrollment metadata (subject ID → template mapping, enrollment timestamp, finger position index) | < $5/month on-demand for 10K items |

### API Layer

| Component | Choice | Why |
|-----------|--------|-----|
| **API Gateway** | REST API (API Gateway v2) | Auth, throttling, request validation |
| **Auth** | Cognito or API keys | Depends on who's calling |
| **Endpoints** | `POST /enroll`, `POST /verify`, `POST /identify`, `GET /health` | Core matcher operations |

### Operation Mapping

| Operation | What Happens | MINEX API Used |
|-----------|-------------|----------------|
| **Enroll** | Raw image → `create_template()` → store template in gallery (S3 + in-memory) | `create_template` |
| **Verify (1:1)** | Raw image → `create_template()` → `match_templates()` against one enrollment | `create_template` + `match_templates` |
| **Identify (1:N)** | Raw image → `create_template()` → `match_templates()` against all 10K gallery templates → return ranked candidates | `create_template` + `match_templates` (×10,000) |

### 1:N Search Performance Estimate
- `match_templates()` is a lightweight comparison (~microseconds per call)
- 10,000 brute-force comparisons: **< 100ms** on a single vCPU
- No indexing structure needed at this gallery size
- For 10-print identification: compare probe against all 10 fingers per subject → 10K comparisons per probe finger, 100K total for full 10-print → still **< 1 second**

### Network & Security

| Control | Implementation |
|---------|----------------|
| **No internet egress** | Fargate task in private subnet, NAT only for ECR pull (or VPC endpoint) |
| **Non-root** | Container runs as UID 1000 |
| **Read-only rootfs** | `readonlyRootFilesystem: true` in task definition |
| **Writable temp** | Bind mount `/tmp` only |
| **No SSH/shell** | No sshd, no shell in container |
| **Encryption at rest** | S3 SSE-S3, DynamoDB encryption, EFS encryption |
| **Encryption in transit** | TLS via ALB/API Gateway |
| **Audit** | CloudTrail + container stdout → CloudWatch Logs |

### Gallery Lifecycle

```
Startup:
  1. Task starts → loads all 10K templates from S3 into memory (~8 MB)
  2. Builds in-memory index (simple array — no fancy data structure needed at 10K)
  3. Health check passes → ALB routes traffic

Enrollment:
  1. Receive raw image via API
  2. create_template() → MINEX template (32-800 bytes)
  3. Store template: S3 (durable) + in-memory array (fast)
  4. Update DynamoDB metadata

Identification:
  1. Receive probe image
  2. create_template() → probe template
  3. Brute-force match_templates() against all gallery entries
  4. Sort by similarity score → return top-N candidates
```

### Total Estimated Monthly Cost (10K Gallery)

| Component | Monthly Cost |
|-----------|-------------|
| ECS Fargate (1 task, 1 vCPU, 2 GB) | ~$35 |
| S3 (templates + images, < 1 GB) | < $1 |
| DynamoDB (on-demand, 10K items) | < $5 |
| API Gateway (low traffic) | < $5 |
| CloudWatch Logs | < $3 |
| ALB (if used) | ~$18 |
| **Total** | **~$50–67/month** |

### Scaling Notes
- **10K → 100K templates**: Still fits in memory (80 MB). Bump to 4 GB RAM. Brute-force still works (< 1 sec). ~Same cost.
- **100K → 1M templates**: Consider indexing (locality-sensitive hashing or binning by finger position). Bump to 2 vCPU / 8 GB. Cost ~$120/month.
- **1M+**: Move to multi-task with partitioned gallery segments. Consider GPU-accelerated matching or dedicated EC2 instances.

---

## 5. Summary Decision Tree

```
Is the vendor delivering interoperable minutiae templates?
  ├── YES → MINEX III path (this document)
  │         ├── Pin NIST sources
  │         ├── Native validation on CentOS 7.6.1810
  │         ├── Hardened container envelope (RHEL 9)
  │         └── Deploy on AWS Fargate
  └── NO (proprietary stack) → PFT III path (separate target)
```

The MINEX III 10-print evaluation is fundamentally about proving **template interoperability** — that your extracted minutiae play nicely with the standard. The gallery and matching infrastructure is actually the easy part; the hard part is getting the native validation to pass cleanly on NIST's exact CentOS environment with deterministic, standards-compliant output.
