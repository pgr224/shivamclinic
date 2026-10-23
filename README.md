# Shivam Clinic

A lightweight, responsive website for Shivam Clinic in South Bopal, Ahmedabad.

## Pages

- `index.html` — clinic overview and featured services
- `services.html` — general physician, dermatology and cosmetology
- `about.html` — clinic approach and care team
- `contact.html` — contact details, clinic hours and location map
- `appointment.html` — appointment request form that opens a prefilled WhatsApp message
- `general-physician.html`, `skin-hair-care.html`, `aesthetic-treatments.html`, `facials.html`, `surgical-dermatology.html` — dedicated care guides
- `gallery.html` — filterable illustrative treatment gallery
- `patient-guide.html` — appointment preparation and consultation guide
- `blog/`, `faq.html`, legal pages and sitemaps share the main site layout

Open `index.html` in a browser or serve this directory with any static web server. No build step or package installation is required.

## Cloudflare Pages deployment

Prepare the public deployment folder:

```sh
python3 scripts/prepare-pages.py
```

The output is `dist/shivamclinic.com/`. Preparation copies the site pages and
assets, checks local links, and excludes Git data, internal reports, and image
source documentation. `wrangler.jsonc` points to this directory.

Authorize Cloudflare and inspect existing projects before creating one:

```sh
npx --yes wrangler@4.152.0 login
npx --yes wrangler@4.152.0 pages project list
```

Use the existing Pages project associated with `shivamclinic.com` when present.
If none exists, create the `shivamclinic-com` project:

```sh
npx --yes wrangler@4.152.0 pages project create shivamclinic-com --production-branch main --force
```

Deploy the prepared directory to the selected project (substitute its name if
the existing project has a different name):

```sh
npx --yes wrangler@4.152.0 pages deploy dist/shivamclinic.com --project-name shivamclinic-com --branch main --commit-dirty=true
```

For new projects in this Wrangler version, the creation command's `--force`
selects Pages instead of delegating to the newer Workers flow. Once the Pages
project exists, subsequent deployment commands do not need this flag.

The production domain must also be associated with this project under
**Workers & Pages → project → Custom domains**. The apex `shivamclinic.com`
requires the domain's zone in the same Cloudflare account and Cloudflare
nameservers. A deployment's `pages.dev` URL can be verified independently of
custom-domain DNS activation.

Appointment requests are sent by the visitor through WhatsApp; the site does not store form data. Clinic contact information is displayed on the contact page.

## Service images and WhatsApp

Every HTML page includes a static WhatsApp link to the clinic number. Its shared responsive styling is in `contact-widget.css`. The home and services pages use locally hosted treatment photos in `assets/images`; sources and checksums are listed in `assets/images/SOURCES.md`. Treatment links preselect a recognised service on the appointment form.

See [the reference comparison and verification report](docs/reference-audit.md) for REA evidence, completed changes and details requiring confirmation from the clinic.

## Clinic details

Clinic owner details supplied on 22 October 2026:

- Address: 19, Sky Sol, Ground Floor, Aarohi Club Road, Opposite Bhagwat Bunggalows, South Bopal.
- Phone and WhatsApp: +91 98246 10611.
- Dr Krishna Kapadiya — BAMS, CCCH, CCACC; Clinical Cosmetician & Aesthetician.
- Dr Prashant Rabadia — MBBS, DCP, CCCH; General & Industrial Physician, Consultant Pathologist.
- Monday–Saturday: 9:00 AM–7:30 PM. Sunday: appointment only.

The clinic details override earlier reference-site captures. The site uses a rose/blush/plum palette. Physician service links preselect their service and Dr Prashant in the appointment form; visitors can change the doctor preference before opening WhatsApp. The generated physician photo and its prompt are documented in `assets/images/physician-consultation.md`.

## Shared design and checks

The 23 October 2026 redesign combines reference-inspired serif headings, rose and plum colours, image-led care cards and a clearer consultation journey. Seven additional photographs from both requested references are hosted locally and documented in `assets/images/SOURCES.md`. Images are illustrative; reference contact identities and salon content are excluded.

Each page contains static, accessible navigation and footer markup. After adding a page or changing the shared templates, refresh them with:

```sh
python3 scripts/sync-layout.py
python3 scripts/check_site.py
node --check script.js
python3 scripts/prepare-pages.py
```

`sync-layout.py` is idempotent and preserves page main content. `check_site.py` checks document structure, duplicate attributes/IDs, local files and fragments, image alt text and JSON-LD. Deployment preparation runs the same checks against the public output.

The [current audit](docs/reference-audit.md) records the 24-page review, new pages, image boundaries, REA evidence and 120 responsive browser checks. Changes in this redesign have not been deployed.
