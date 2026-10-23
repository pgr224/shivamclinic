#!/usr/bin/env python3
"""Check every static page, link, fragment, image and JSON-LD block."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import sys

class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links=[]; self.ids=[]; self.counts={}; self.structured=[]; self.script=None; self.duplicate_attrs=[]
    def handle_starttag(self, tag, attrs):
        names=[name for name,value in attrs]
        if len(names)!=len(set(names)): self.duplicate_attrs.append(tag)
        attrs=dict(attrs); self.counts[tag]=self.counts.get(tag,0)+1
        if attrs.get('id'): self.ids.append(attrs['id'])
        for name in ('href','src','poster'):
            if attrs.get(name): self.links.append(attrs[name])
        if tag=='script' and attrs.get('type')=='application/ld+json': self.script=''
        if tag=='img' and 'alt' not in attrs: self.links.append('ERROR: Image missing alt text')
    def handle_data(self, data):
        if self.script is not None: self.script+=data
    def handle_endtag(self, tag):
        if tag=='script' and self.script is not None:
            self.structured.append(self.script); self.script=None

def validate_site(root):
    root=Path(root).resolve(); pages={}
    for file in root.rglob('*.html'):
        if any(part.startswith('.') or part in {'dist','node_modules','docs'} for part in file.relative_to(root).parts): continue
        parser=Page(); parser.feed(file.read_text()); pages[file]=parser
    errors=[]; links=0
    for file,page in pages.items():
        label=file.relative_to(root)
        for tag in ('html','head','body','main','h1','title'):
            if page.counts.get(tag)!=1: errors.append(f'{label}: expected one {tag}, found {page.counts.get(tag,0)}')
        if len(page.ids)!=len(set(page.ids)): errors.append(f'{label}: duplicate IDs')
        if page.duplicate_attrs: errors.append(f'{label}: duplicate attributes on {page.duplicate_attrs}')
        for block in page.structured:
            try:json.loads(block)
            except ValueError as error:errors.append(f'{label}: invalid JSON-LD: {error}')
        for link in page.links:
            if link.startswith('ERROR:'): errors.append(f'{label}: {link}');continue
            parsed=urlsplit(link)
            if parsed.scheme or parsed.netloc: continue
            links+=1
            path=unquote(parsed.path)
            target=(root/path.lstrip('/') if path.startswith('/') else file.parent/path).resolve() if path else file
            if target.is_dir():target/= 'index.html'
            if not target.is_relative_to(root) or not target.exists():errors.append(f'{label}: missing file {link}');continue
            if parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:errors.append(f'{label}: missing fragment {link}')
    if errors:raise ValueError('\n'.join(errors))
    print(f'Validated {len(pages)} HTML pages and {links} local links/fragments; documents, image alt text and JSON-LD passed.')

if __name__=='__main__':validate_site(sys.argv[1] if len(sys.argv)>1 else Path(__file__).resolve().parents[1])
