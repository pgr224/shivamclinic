#!/usr/bin/env python3
"""Sync the static shared navigation, footer, fonts and page metadata.

Run after editing these templates or adding pages; content stays in each HTML file.
"""
from pathlib import Path
import re
from html import escape, unescape
ROOT = Path(__file__).resolve().parents[1]
FONT = 'https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,500;1,600&family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap'

def brand(prefix, light=''):
    return f'<a class="brand {light}" href="{prefix}index.html" aria-label="Shivam Clinic home"><span class="brand-mark" aria-hidden="true">S<span>+</span></span><span class="brand-name">shivam<span>CLINIC · SOUTH BOPAL</span></span></a>'

def header(prefix, page):
    items=[('index.html','Home'),('services.html','Our care'),('about.html','About'),('gallery.html','Gallery'),('blog/index.html','Journal'),('contact.html','Contact')]
    links=''.join(f'<a href="{prefix}{href}"'+(' aria-current="page"' if page==href or page.startswith('blog/') and href=='blog/index.html' or page in {'general-physician.html','skin-hair-care.html','aesthetic-treatments.html','facials.html','surgical-dermatology.html'} and href=='services.html' else '')+f'>{label}</a>' for href,label in items)
    return f'''<a class="skip-link" href="#main-content">Skip to content</a>
<div class="topbar"><div class="container topbar-inner"><span>General health. Skin care. A little more personal.</span><a href="tel:+919824610611">+91 98246 10611 <span aria-hidden="true">↗</span></a></div></div>
<header class="site-header"><div class="container nav-wrap">{brand(prefix)}<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open navigation"><span></span><span></span><span></span></button><nav id="site-nav" class="site-nav" aria-label="Main navigation">{links}<a class="button button-small nav-cta" href="{prefix}appointment.html"{' aria-current="page"' if page=='appointment.html' else ''}>Book a visit <span aria-hidden="true">↗</span></a></nav></div></header>'''

def footer(prefix):
    return f'''<footer class="site-footer"><div class="container footer-main"><div class="footer-brand">{brand(prefix,'brand-light')}<p>For your health.<br>For your skin. <em>For you.</em></p><a class="text-link footer-appointment" href="{prefix}appointment.html">Let’s plan your visit <span aria-hidden="true">↗</span></a></div><div class="footer-col"><h2>Explore</h2><a href="{prefix}services.html">Our care</a><a href="{prefix}about.html">Meet your doctors</a><a href="{prefix}gallery.html">Treatment gallery</a><a href="{prefix}blog/index.html">Health journal</a></div><div class="footer-col"><h2>Your visit</h2><a href="{prefix}appointment.html">Book an appointment</a><a href="{prefix}patient-guide.html">Patient guide</a><a href="{prefix}faq.html">Common questions</a><a href="{prefix}contact.html">Find the clinic</a></div><div class="footer-col"><h2>Come say hello</h2><a href="tel:+919824610611">+91 98246 10611</a><a href="{prefix}contact.html">19, Sky Sol, Ground Floor,<br>Aarohi Club Road, Opposite Bhagwat Bunggalows,<br>South Bopal</a><p class="footer-clinic-hours">Monday–Saturday · 9:00 AM–7:30 PM<br>Sunday · Appointment only</p></div></div><div class="container footer-bottom"><span>© <span data-year>2026</span> Shivam Clinic</span><div class="footer-legal"><a href="{prefix}privacy.html">Privacy</a><a href="{prefix}terms.html">Terms</a><a href="{prefix}sitemap.html">Sitemap</a></div><span>Care, with a little more heart. ♡</span></div></footer>'''

def sync(page):
    text=page.read_text(); rel=page.relative_to(ROOT).as_posix();prefix='../' if rel.startswith('blog/') else '/' if rel=='404.html' else ''
    # The first header is the site's navigation. Retain the page's main content.
    text=re.sub(r'<body([^>]*)>.*?</header>',lambda m:'<body'+m.group(1)+'>'+header(prefix,rel),text,count=1,flags=re.S)
    text=re.sub(r'<a class="whatsapp-float".*?</a>','',text,flags=re.S)
    widget=f'<a class="whatsapp-float" href="https://wa.me/919824610611?text=Hello%20Shivam%20Clinic%2C%20I%20would%20like%20to%20ask%20about%20your%20services." target="_blank" rel="noopener noreferrer" aria-label="Chat with Shivam Clinic on WhatsApp (opens in a new tab)"><img src="{prefix}assets/icons/whatsapp.svg" width="28" height="28" alt="" aria-hidden="true"><span>WhatsApp us</span></a>'
    text=re.sub(r'<footer\b.*?</footer>',lambda m:footer(prefix)+widget,text,count=1,flags=re.S)
    text=re.sub(r'<main\b([^>]*)>',lambda m:'<main'+re.sub(r'\s+(?:id|tabindex)="[^"]*"','',m.group(1))+' id="main-content" tabindex="-1">',text,count=1)
    # Remove inherited reference identities, including structured metadata.
    text=re.sub(r',\s*"email":\s*"info@shivamclinic.org"','',text)
    text=re.sub(r'<div class="contact-item"><span class="contact-icon" aria-hidden="true">✉</span>.*?</div></div>','',text,flags=re.S)
    text=text.replace('Call, email or find us on the map.','Call, WhatsApp or find us on the map.')
    text=re.sub(r'<link[^>]+href="(?:\.\./|/)?styles?\.css"[^>]*>','',text)
    text=re.sub(r'<link[^>]+href="https://fonts\.[^>]*>','',text)
    text=re.sub(r'<script src="(?:\.\./|/)?script\.js" defer></script>','',text)
    text=re.sub(r'<link rel="canonical"[^>]*>|<meta (?:property="og:[^"]*"|name="twitter:[^"]*"|name="robots"|name="theme-color")[^>]*>','',text)
    text=re.sub(r'<link rel="icon"[^>]*>','',text)
    text=re.sub(r'<link[^>]+href="(?:\.\./|/)?contact-widget\.css"[^>]*>','',text)
    title=re.search(r'<title>(.*?)</title>',text,re.S).group(1)
    desc=re.search(r'<meta name="description" content="([^"]*)"',text)
    description=desc.group(1) if desc else 'Personal care for your health, skin and wellbeing at Shivam Clinic, South Bopal.'
    canonical='https://shivamclinic.com/'+('' if rel=='index.html' else 'blog/' if rel=='blog/index.html' else rel)
    meta=f'''\n<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONT.replace('&','&amp;')}" rel="stylesheet">
<link rel="stylesheet" href="{prefix}styles.css"><link rel="stylesheet" href="{prefix}contact-widget.css"><script src="{prefix}script.js" defer></script>
<link rel="icon" type="image/svg+xml" href="{prefix}assets/icons/favicon.svg"><meta name="theme-color" content="#63344f">
<link rel="canonical" href="{canonical}"><meta name="robots" content="{'noindex,follow' if rel=='404.html' else 'index,follow'}">
<meta property="og:title" content="{escape(unescape(title))}"><meta property="og:description" content="{description}"><meta property="og:type" content="{'article' if rel.startswith('blog/') and rel!='blog/index.html' else 'website'}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="https://shivamclinic.com/assets/images/skin-banner.jpg"><meta name="twitter:card" content="summary_large_image">\n'''
    text=text.replace('</head>',meta+'</head>')
    if rel=='404.html':
        text=re.sub(r'(href|src)="(?!https?:|tel:|mailto:|/|#)([^"]+)"',r'\1="/\2"',text)
    text='\n'.join(line.rstrip() for line in text.splitlines())+'\n'
    text=re.sub(r'\n{3,}', '\n\n', text)
    page.write_text(text)

if __name__=='__main__':
    pages=list(ROOT.glob('*.html'))+list((ROOT/'blog').glob('*.html'))
    for page in pages:sync(page)
    print(f'Synced shared layout and metadata on {len(pages)} pages.')
