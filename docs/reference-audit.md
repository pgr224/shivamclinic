# Reference-site comparison and redesign

Reviewed and implemented locally on **23 October 2026** using the `reverse-engineer-anything` skill, fresh REA browser scenarios, reference HTML/CSS inspection and local browser verification.

## Current outcome

The site now has **24 static HTML pages**, with one shared header, footer, typography system and appointment CTA. The design combines the serif headings, warm colours, decorative framing and image-led presentation observed at [shivamclinik.com](https://www.shivamclinik.com/) with the service categories and consultation pathways observed at [shivamclinic.org](https://shivamclinic.org/). The implementation keeps the project's rose/plum identity and owner-documented clinic details.

The original 17 pages had no broken local links or fragments. The missing-page findings were gaps in standalone content and discoverability, rather than existing links returning missing pages.

| Finding | Implemented change |
| --- | --- |
| Five modern pages and twelve legacy pages used different layouts | All 24 pages now use `styles.css`, consistent navigation, mobile menu, booking CTA, footer, skip link and page metadata |
| Service categories existed mainly as sections on a long overview | Added [general physician](../general-physician.html), [skin and hair care](../skin-hair-care.html), [aesthetic care](../aesthetic-treatments.html), [facials](../facials.html) and [surgical dermatology](../surgical-dermatology.html) pages; linked them from the services overview |
| No suitable reference-inspired image gallery | Added [treatment gallery](../gallery.html) with ten illustrative images, five accessible filters and related care links; every image remains visible without JavaScript |
| Consultation preparation was scattered | Added [patient guide](../patient-guide.html) covering booking, preparation, discussion and follow-up |
| Main navigation hid the journal, FAQ and website information | Added journal/gallery to the common header and patient guide, FAQ, privacy, terms and sitemap to the common footer |
| Homepage relied on generic remote stock images | Rebuilt it with a treatment-photo composition, care cards, facial-care feature, consultation steps, doctors, journal previews and useful FAQs; images are hosted locally |
| Reference email/social identities remained in contact details and clinic schema | Removed unverified reference email and Instagram details from public pages; retained only the clinic identity documented in `clinic-update.md` |
| Booking categories did not consistently carry visitor intent | Category and treatment links select valid services; physician selections choose Dr Prashant, aesthetic selections choose Dr Krishna; uncertain service leaves doctor preference open |
| Sitemap omitted booking and new pages; canonical domains were inconsistent | Rebuilt both sitemaps for all 23 indexable pages, unified apex-domain canonicals and social metadata, marked 404 noindex |
| Nested 404 links could resolve to incorrect locations | All 404 assets and recovery links now use root-relative paths |
| Privacy text did not describe the website's actual behaviour | Documented editable WhatsApp drafts, no website form storage, and Google Fonts/Maps requests |
| FAQ and blog metadata included unsupported details | Removed unsupported paediatric-service wording and unverified exact blog publication dates |

## Image and content boundaries

Seven additional original image files were selected from both reference sites: four from shivamclinik.com and three from shivamclinic.org. All seven appear in relevant care content and the gallery. Sources and SHA-256 hashes are in [the image provenance record](../assets/images/SOURCES.md).

Reference phone numbers, emails, addresses, doctors, logos, social accounts, salon services, patient testimonials and before/after claims were not imported into public content. Existing owner-documented clinic details were retained. Photos are labelled as illustrations; they are not represented as photographs of this clinic, its doctors or verified outcomes. No offers, prices, equipment certifications or clinical result claims were invented to imitate reference sections.

## Verification

- All **24 pages** passed document-structure, duplicate-attribute/ID, image-alt, JSON-LD, local-file and fragment validation: **971 local references** checked.
- All 23 intended public pages are reachable from the homepage. The 404 page is intentionally outside the sitemap.
- All 92 booking links have valid service values matching the appointment form.
- **120 browser page/viewport checks**: all 24 pages at 320, 375, 768, 1024 and 1440px, with decoded images and loaded fonts. No horizontal overflow, broken images, navigation collision or JavaScript page errors.
- All five gallery filters return their expected counts; the gallery remains readable with JavaScript disabled.
- Mobile navigation opens and closes with Escape, restoring focus to its toggle.
- Physician and aesthetic links select matching services and doctors; an uncertain-service request leaves doctor preference open.
- Appointment submission was intercepted locally: a correct editable WhatsApp draft was generated for the existing clinic number. **No message was sent.**
- Nested-path 404 rendering was simulated: shared assets load and recovery links resolve to the root pages.
- The static layout synchroniser produces identical files on repeated runs.
- `node --check script.js`, `git diff --check`, and `python3 scripts/prepare-pages.py` pass. The prepared deployment contains **48 public files** in `dist/shivamclinic.com/` and excludes internal audit/provenance documents.

See the retained [browser validation summary](browser-validation-2026-10-23.json), [desktop preview](previews/home-desktop.png) and [mobile preview](previews/home-mobile.png).

## Fresh REA evidence

| Scope | Evidence | Observed result |
| --- | --- | --- |
| shivamclinik.com homepage, 1440px | `ev_66bc7558dafbd3cca35db08109438a8bcb87f1abf60954020795ea8f5fb89870` | Rendered DOM/accessibility, image-led treatment layout, serif headings and reference navigation |
| shivamclinic.org homepage, 1440px | `ev_9afa23d923bea027ce036a1ede103751f2ab5fc9015c76cbf641a7c99ecda861` | Rendered DOM/accessibility and care-category navigation |
| Local gallery → facial guide → appointment, 375px | `ev_9c84f8088a93c2a9b6185da48366c4bea7ba6b9095ba28692187433549399abb` | REA clicked the facial filter, opened its guide and followed the category booking CTA; all steps completed without page errors |

REA-owned browsers reported `terminated-owned-process`. The reference observations cover the declared homepage visits, supplemented by downloaded HTML, styles and selected images. They do not establish exhaustive reference-site coverage, clinical effectiveness, reference asset licensing, or ownership of the photographed clinic equipment. Visual choices and newly written consultation copy are implementation decisions; the local checks verify the current site's rendering and interactions.

**Publication status:** these changes are local. The deployment folder has been refreshed; no new deployment was performed in this task.

---

## Historical review — 22 October 2026

Reviewed on 22 October 2026 using REA browser scenarios. The scope was the home page and aesthetic, facial and surgical service pages, compared with the local static site.

## Findings and changes

| Gap observed in the local site | Implementation | Status |
| --- | --- | --- |
| WhatsApp available only through the appointment form | Added an accessible, responsive WhatsApp link to all 17 HTML pages, using the live site's configured number `917575826155`; added a direct contact-page link | Complete |
| Broad cosmetology copy without treatment images | Added a three-card home section and an eight-treatment services gallery, using locally hosted reference-site photos | Complete |
| Missing detailed service categories | Added surgical dermatology and specialty facials sections, expanded aesthetic and laser services, and added category navigation | Complete |
| Treatment links did not carry the selected service into booking | Added validated service preselection and matching appointment options | Complete |
| No link to the live site's Instagram account | Added the observed Instagram account to the main-page footers | Complete |
| Two complete HTML documents concatenated in four main pages | Removed the obsolete first document from home, about, services and contact pages | Complete |

The WhatsApp link opens an editable message; it does not automatically send a message. Treatment descriptions describe services listed by the reference site and do not promise outcomes. Photos are illustrative service imagery from that site, not evidence of patient outcomes. See [image sources](../assets/images/SOURCES.md).

## Verification

- All 17 pages return HTTP 200 and have one HTML document, one title and one main element.
- Every local link, fragment, image, script and stylesheet checked successfully.
- One visible WhatsApp link on each page, pointing to the configured clinic number.
- The five main pages checked at 320, 375, 768 and 1440 pixels: no horizontal overflow.
- Local images decoded after scrolling to lazy-loaded content.
- Mobile navigation opens; a HydraFacial card selects HydraFacial in the appointment form.
- Form submission was intercepted locally: the encoded WhatsApp draft includes the selected treatment; no message was sent.
- No browser JavaScript errors. `node --check script.js` and `git diff --check` pass.
- REA independently replayed the service-to-appointment journey at a 375px viewport and observed the selected option.

## Evidence ledger

- [Home](https://shivamclinic.org/): `ev_923d2f44db27901fc6cd70778e0d94b1c70dce2963b12f32a8a3589804c650d4`.
- [Aesthetic and laser services](https://shivamclinic.org/service/aesthetic-laser-dermatology/): `ev_ddf3fdd0b88f4e5fa43a22bea84d5b733565d0e62233065aab595d5f3b27ddc0`.
- [Specialty facials](https://shivamclinic.org/service/specialty-facials-skin-care/): `ev_e72ac9b7b546139ec43f2667127a4bd0de5e22c18ce55467356b09e37e652e9b`.
- [Surgical dermatology](https://shivamclinic.org/service/surgical-dermatology/): `ev_477c9b062d07d8253daab6fd5468ef3ed22a4fe00e7c469e3f488ca76ad0d06e`.
- [Local mobile appointment flow](http://127.0.0.1:8765/services.html): `ev_7ba91381237d986d6a30c26bbcd7410b51ce9f269e0b669e4b1f9c9e5f8c6a39`.

All REA-owned temporary browsers reported `terminated-owned-process`. Captures establish the DOM and accessibility state during the declared visits; they do not verify clinical results or complete coverage of every reference-site page.

## Remaining source discrepancies

The reference site showed inconsistent opening times and a different doctor name. The clinic owner subsequently supplied authoritative details on 22 October 2026: Dr Krishna Kapadiya and Dr Prashant Rabadia, phone +91 98246 10611, and Monday–Saturday 9:00 AM–7:30 PM with Sunday by appointment only. These now supersede the reference-site details across the website and booking links. The original reference capture and its phone-number finding above remain historical evidence. Patient testimonials and before/after result images were not transferred as verified clinical outcomes. Legacy blog and legal pages still contain placeholder canonical domains; choosing the new site's deployment domain is outside this comparison.

