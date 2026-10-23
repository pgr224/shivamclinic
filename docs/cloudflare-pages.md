# Cloudflare Pages deployment

Deployed on 22 October 2026.

- Project: `shivamclinic-com`
- Production URL: https://shivamclinic-com.pages.dev
- Deployment URL: https://9d68047b.shivamclinic-com.pages.dev
- Deployment ID: `9d68047b-cb64-4bb2-8ebb-39542dc10305`
- Production branch: `main`
- Upload directory: `dist/shivamclinic.com/`
- Uploaded files: 33
- Custom domain: `shivamclinic.com`, attached to the project

The production homepage, monsoon skin-care article, contact page, stylesheet,
and physician image returned HTTP 200 after deployment.

Cloudflare's custom-domain API currently reports **pending: CNAME record not
set**, including after the user reported adding the record and a Pages
validation retry. The authorized Wrangler connection supports Pages deployment
and zone lookup, but DNS and DNSSEC API calls return HTTP 403.

Add this record in the existing `shivamclinic.com` Cloudflare zone:

| Field | Value |
| --- | --- |
| Type | CNAME |
| Name | `@` |
| Target | `shivamclinic-com.pages.dev` |
| Proxy | On |
| TTL | Auto |

DNS settings: https://dash.cloudflare.com/56280198e3630dc2d4f49f0e97241748/shivamclinic.com/dns/records

After the record is added, verify the project's custom-domain status becomes
active and `https://shivamclinic.com` serves the clinic website. The working
`pages.dev` deployment is available while domain validation completes.

## DNSSEC blocker found during domain verification

Both Google and Cloudflare recursive resolvers return `SERVFAIL` for the domain.
Google's extended error is `No DNSKEY matches DS RRs of shivamclinic.com`.
Querying with DNSSEC validation disabled succeeds, confirming a DNSSEC chain
problem. The `.com` DS record uses algorithm 5, while Cloudflare's current
authoritative DNSKEY records use algorithm 13.

RDAP identifies the registrar as **BigRock Solutions Ltd**. In BigRock's domain
Order Information → DNSSEC panel, update the DS record to match the current
values displayed in Cloudflare's DNSSEC settings. The registrar DS must match
Cloudflare's active signing key; leaving the old record in place prevents
validating resolvers from resolving the website.

A direct authoritative A query also returned no address during verification,
so the requested apex record is not yet confirmed at the authoritative servers.
Confirm the apex CNAME in the existing Cloudflare zone as well as correcting
the DNSSEC chain.

References:

- https://developers.cloudflare.com/dns/dnssec/troubleshooting/
- https://www.bigrock.in/help/article/Adding-DS-Records

Use the deployment instructions in the repository README for future uploads.
