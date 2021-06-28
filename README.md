# notes_cours_psy3018
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

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/psy3018/notes_cours_psy3018/graphs/contributors).

## Credits

This project is created using the excellent open source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book). Further credits for the book can be found in the book itself.
