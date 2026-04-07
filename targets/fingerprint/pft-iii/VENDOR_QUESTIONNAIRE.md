PFT III Vendor Questionnaire
============================

Instructions for Jupiter
------------------------

Send this questionnaire to the vendor with minimal edits. The goal is to
determine whether the deliverable can map cleanly to the PFT III target.

Template
--------

Subject: PFT III intake for proprietary fingerprint template evaluation

We are preparing a controlled compatibility path for a PFT III style
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

4. Interface compatibility

 * Can the software be delivered as a shared library implementing the PFT III
   API?
 * Can it provide a `PFTIII::Interface` implementation?
 * Can it support:
   * `getIdentification()`
   * `createProprietaryTemplate()`
   * `compareProprietaryTemplates()`
   * `getImplementation(configurationDirectory)`
 * Can it link with `g++` / `mpicxx` under Ubuntu Server 24.04.3 LTS?

5. Template and image behavior

 * Does the product generate proprietary templates?
 * Can it process raw 8-bit grayscale fingerprint images?
 * Which resolutions are supported?
 * Can it handle variable resolutions without resampling?
 * Can it handle unknown metadata values?
 * Can it handle contact, rolled, swipe, and contactless imagery?

6. Runtime dependencies

 * List every required shared library and version.
 * Are any license files required?
 * Is any license server required?
 * Are any daemons or background services required?
 * Is any network access required at runtime?

7. Filesystem and execution constraints

 * Can the software run in batch, non-interactive mode?
 * Does it write to stdout, stderr, or arbitrary files during normal operation?
 * Can it avoid reading or writing outside a provided read-only configuration
   directory?
 * Can it run without GUI, terminal interaction, or sockets?

8. Build and install

 * Provide controlled Linux build instructions if source is provided.
 * Provide controlled Linux install instructions if binaries are provided.
 * Identify any environment variables required at build time or runtime.
 * Identify any hard-coded paths.

9. Validation and compatibility

 * Has this deliverable been tested against PFT III or a PFT-like interface?
 * If yes, provide details.
 * Are there known limitations for atypical resolutions or contactless imagery?
 * Are there known issues with deterministic output or comparison behavior?

10. Security and operational constraints

 * Can the software run without outbound internet access?
 * Can the software run without privileged execution?
 * Can the software run with a read-only root filesystem and explicit writable
   mounts only?
 * Does the software require host-specific activation or hardware dongles?

11. Supporting attachments requested

 * checksum manifest
 * dependency manifest
 * build or install guide
 * release notes
 * sample config files
 * sample license-handling instructions if applicable

Decision note
-------------

If the vendor is actually interoperable-template oriented rather than
proprietary-template oriented, route the discussion back toward `MINEX III`
instead of `PFT III`.
