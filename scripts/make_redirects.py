#!/usr/bin/env python3
"""Generate redirect stubs mapping the old Jupyter Book v1 URLs to the new
MyST (v2) URLs, so bookmarks / syllabus links / search results don't 404.

v1 served pages at the site root as `<name>.html` with underscores.
v2 (MyST) serves them as `/<name-with-hyphens>/` (no `.html`).

We drop a tiny HTML file at each old path that redirects to the new one.
Run after `jupyter-book build --html`, writing into the build output dir.
"""
import sys
from pathlib import Path

# old v1 filename (at site root) -> new v2 URL
REDIRECTS = {
    "intro.html": "/",
    "cartes_cerebrales.html": "/cartes-cerebrales/",
    "irm.html": "/irm/",
    "morphometrie.html": "/morphometrie/",
    "irm_fonctionnelle.html": "/irm-fonctionnelle/",
    "connectivite.html": "/connectivite/",
    "irm_diffusion.html": "/irm-diffusion/",
    "imagerie_optique.html": "/imagerie-optique/",
    "tep.html": "/tep/",
    "cartes_statistiques.html": "/cartes-statistiques/",
    "reproductibilite.html": "/reproductibilite/",
    "references.html": "/",  # no dedicated page in v2 -> home
}

TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url={url}">
<link rel="canonical" href="{url}">
<script>location.replace("{url}" + location.hash);</script>
<title>Page déplacée</title>
</head>
<body>
<p>Cette page a été déplacée. Vous allez être redirigé·e vers
<a href="{url}">{url}</a>.</p>
</body>
</html>
"""


def main(out_dir: str) -> None:
    out = Path(out_dir)
    if not out.is_dir():
        sys.exit(f"Build output dir not found: {out}")
    for old, new in REDIRECTS.items():
        target = out / old
        # never clobber a real page produced by the build (e.g. index.html)
        if target.exists():
            print(f"skip (exists): {old}")
            continue
        target.write_text(TEMPLATE.format(url=new), encoding="utf-8")
        print(f"redirect: /{old} -> {new}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "_build/html")
