MINEX III Vendor Questionnaire
==============================

Instructions for Jupiter
------------------------

Send this questionnaire to the vendor with minimal edits. The goal is to
determine whether the deliverable can map cleanly to the MINEX III target.

Template
--------

Subject: MINEX III intake for interoperable 10-print fingerprint template evaluation

We are preparing a controlled compatibility path for a MINEX III style
evaluation. Please answer the questions below as precisely as possible and
attach supporting files where applicable.

1. Product identity

 * Product name:
 * Product version:
 * Internal build or release identifier:
 * Primary technical contact:

2. Artifact inventory

 * Provide the full file list for the deliverable.
 * For each file, provide:
   * filename
   * role
   * version
   * SHA-256 checksum

3. Platform assumptions

 * Supported CPU architectures:
 * Supported Linux distributions:
 * Required glibc or libc version:
 * Required compiler or runtime version:

4. Interface and standards

 * Does the product generate interoperable minutiae templates?
 * Which standards are supported?
   Examples: ANSI INCITS 378, ISO 19794-2.
 * Is the deliverable intended for standardized 10-print template generation?
 * Can the product operate at the template level, not only as an end-to-end
   closed matcher?
 * Does the product expose separate extraction and matching functions?

5. Input assumptions

 * Expected image resolution:
 * Assumptions about tenprint source imagery:
 * Any preprocessing required before extraction:
 * Any unsupported image conditions:

6. Runtime dependencies

 * List every required shared library and version.
 * Are any license files required?
 * Is any license server required?
 * Are any daemons or background services required?
 * Is any network access required at runtime?

7. Build and install

 * Provide controlled Linux build instructions if source is provided.
 * Provide controlled Linux install instructions if binaries are provided.
 * Identify any environment variables required at build time or runtime.
 * Identify any hard-coded paths.

8. Validation and compatibility

 * Has this deliverable been tested against MINEX III or a MINEX-like interface?
 * If yes, provide details.
 * Are there any known limitations relative to interoperable minutiae-template
   generation or matching?
 * Are there any known issues with 500 ppi or tenprint workflows?

9. Security and operational constraints

 * Can the software run without outbound internet access?
 * Can the software run without privileged execution?
 * Can the software run in a read-only-root filesystem with explicit writable
   mounts only?
 * Does the software write outside its working directory?

10. Supporting attachments requested

 * checksum manifest
 * dependency manifest
 * build or install guide
 * release notes
 * sample config files
 * sample license-handling instructions if applicable

Decision note
-------------

If the vendor cannot map the deliverable to interoperable minutiae-template
generation and matching, route the discussion toward `PFT III` instead of
`MINEX III`.
