# Clinic update — 22 October 2026

The clinic-owner details supplied in this conversation supersede the earlier reference-site capture.

## Current details

- **Address:** 19, Sky Sol, Ground Floor, Aarohi Club Road, Opposite Bhagwat Bunggalows, South Bopal.
- **Phone and WhatsApp:** +91 98246 10611.
- **Dr Krishna Kapadiya:** BAMS, CCCH, CCACC; Clinical Cosmetician & Aesthetician.
- **Dr Prashant Rabadia:** MBBS, DCP, CCCH; General & Industrial Physician, Consultant Pathologist.
- **Monday–Saturday:** 9:00 AM–7:30 PM.
- **Sunday:** Appointment only.

These details appear in the clinic pages, doctor profiles, footers, maps and structured clinic metadata. All 17 page-level WhatsApp links and the appointment draft use the new phone number.

## Physician services

Eight detailed cards cover fever management, diabetes care, blood pressure measurement and monitoring, ECG, general consultations, preventive health checks, industrial and occupational health, and pathology/report review. Booking links preselect the corresponding service and Dr Prashant Rabadia. Visitors can change their preferred doctor before opening the draft in WhatsApp.

The general physician section includes an illustrative [generated consultation photo](../assets/images/physician-consultation.png). It was created with the built-in image generation tool; its [complete final prompt and provenance](../assets/images/physician-consultation.md) are recorded alongside the asset. It is not a portrait of a clinic doctor.

## Visual update

Replaced green/teal styling across modern and legacy pages with blush and rose gradients, dark plum text and footers, rose buttons, matching doctor cards and physician service icons. Text and button contrast samples meet AA contrast thresholds. Responsive navigation and existing cosmetic treatment sections are preserved.

## Verification

- All 17 HTML pages, local links, fragment destinations, scripts, stylesheets and images checked successfully.
- The five main pages checked at 320, 375, 768 and 1440 pixels without horizontal overflow.
- Mobile navigation works; local images decode, including the generated physician image.
- Both doctors and qualifications checked against the supplied details.
- All eight physician service links select their matching option and Dr Prashant Rabadia.
- Appointment submission intercepted locally: draft targets `919824610611` and includes the selected service and preferred doctor. No WhatsApp message was sent.
- Contact address, map query and structured Monday–Saturday opening times checked.
- No JavaScript page errors, stale phone numbers, old doctor name or old daily opening hours found in HTML/JavaScript.
- `node --check script.js` and `git diff --check` pass.

Changes are local and have not been published.
