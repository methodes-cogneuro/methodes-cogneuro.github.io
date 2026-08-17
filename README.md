# notes_cours_psy3018
[![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

Introduction aux Méthodes de Neuroimagerie en neurosciences cognitives

## Usage

Le livre est construit avec **Jupyter Book v2 ([MyST](https://mystmd.org/))**. La
configuration et la table des matières se trouvent dans `myst.yml`, et le contenu
dans les fichiers `.md` du dossier `methodes_neurocog/`.

### Construire le livre

Si vous souhaitez développer et construire les notes de cours PSY3018, vous devez:

- Cloner ce repository.
- Installer la commande Jupyter Book v2 (via npm) : `npm install -g jupyter-book`.
- (Optionnel) Installer les dépendances Python pour réexécuter les notebooks :
  `pip install -r requirements.txt` (de préférence dans un environnement virtuel).
- Modifier le contenu du livre à partir des fichiers `.md` (et la table des
  matières dans `myst.yml`).
- Prévisualiser le site localement : `jupyter book start`.
- Construire le site statique : `jupyter book build --html` (résultat dans `_build/html`).

### Hosting the book

- Ouvrir une pull request pour faire des changements.
- Une fois les changements importés dans `main`, l'action GitHub
  (`.github/workflows/deploy.yml`) construit le livre et le publie automatiquement
  sur GitHub Pages (source : *GitHub Actions*).
- Les anciennes URL de la version 1 (`/page_exemple.html`) sont redirigées vers les
  nouvelles URL de la version 2 (`/page-exemple/`) grâce à `scripts/make_redirects.py`,
  exécuté lors de la construction. Pour préserver une nouvelle ancienne URL, ajoutez-la
  au dictionnaire `REDIRECTS` de ce script.

## Contributors

We welcome and recognize all contributions. You can see a list of all contributors in the book.

## Credits

This project is created using the excellent open source [Jupyter Book project](https://jupyterbook.org/). Further credits for the contributors of the book can be found in the book itself.
