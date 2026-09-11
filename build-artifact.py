#!/usr/bin/env python3
"""Baut artifact.html: Body-Inhalt ohne Doctype/Head-Hülle, Meme-Fotos als data:-URIs eingebettet."""
import base64,re,pathlib
root=pathlib.Path(__file__).parent
s=(root/"index.html").read_text(encoding="utf-8")
s=re.sub(r'^<!doctype html>\s*<html[^>]*>\s*<head>\s*<meta charset="utf-8">\s*<meta name="viewport"[^>]*>\s*','',s)
s=s.replace('</head>\n<body>\n','').replace('\n</body>\n</html>\n','')
def datauri(m):
    f=root/m.group(1)
    return 'img:"data:image/jpeg;base64,'+base64.b64encode(f.read_bytes()).decode()+'"'
s=re.sub(r'img:"(memes/[^"]+)"',datauri,s)
(root/"artifact.html").write_text(s,encoding="utf-8")
print("artifact.html", len(s)//1024, "KB")
