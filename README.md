# notes_cours_psy3018
[![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

Notes de cours pour PSY3018 - Méthodes en neurosciences cognitives

## Usage

### Construire le livre

Si vous souhaitez développer et construire les notes de cours PSY3018, vous devez:

- Clonez ce repository
- Exécutez `pip install -r requirements.txt` (il est recommandé d'effectuer cette commande dans un environnement virtuel)
- (Recommendé) Effacez le répertoire `methodes_neurocog/_build/`
- Exécutez `jb build methodes_neurocog/`

Une version statique html du livre sera générée dans `methodes_neurocog/_build/html/`.

### Hosting the book

The html version of the book is hosted on the `gh-pages` branch of this repo. Navigate to your local build and run,
- `ghp-import -n -p -f methodes_neurocog/_build/html`

This will automatically push your build to the `gh-pages` branch. More information on this hosting process can be found [here](https://jupyterbook.org/publish/gh-pages.html#manually-host-your-book-with-github-pages).

### Generating pdf

The support for pdf generation is experimental with jupyter book, and the output is not perfect. Currently the process looks like:
 * install the depencies described in the section "Building a pdf with latex" in the [jb docs](https://jupyterbook.org/advanced/pdf.html).
 * build latex with individual pages: `jb build methodes_neurocog/ --builder pdflatex --individualpages`. This produces warnings (skip them) and errors. If you ever get stuck in the terminal, leaving the weird latex compilation environment is achieved by pressing `X` (you're welcome). 
 * install xetex `sudo apt-get install texlive-xetex`
 * go in the build directory `cd methodes_neurocog/_build/latex`
 * edit manually the `tex` file of the chapter. Replace all `\chapter` by `\section` and add a proper `\chapter` at the beginning. You can also search `Content` and replace by `Table des matières`. I have tried to switch the whole doc in French but without success so far. 
 * before adding the chapter title, add the following lines: `\setcounter{chapter}{n} \addtocounter{chapter}{-1}`, where `n` is the number of the chapter.
 * Compile a chapter, e.g. `xelatex cartes_cerebrales.tex`
 * the resulting pdf is mega-huge. So shrink it with `gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dNOPAUSE -dQUIET -dBATCH -sOutputFile=notes_cours_cartes_cerebrales.pdf -dPDFSETTINGS=/ebook cartes_cerebrales.pdf`
 * Voilà 🎉 🎉 🎉
 
## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/psy3018/notes_cours_psy3018/graphs/contributors).

## Credits

This project is created using the excellent open source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book). Further credits for the book can be found in the book itself.
