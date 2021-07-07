---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
(irm-chapitre)=
# Imagerie par résonance magnétique

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/me-pic">
        <img src="https://avatars.githubusercontent.com/u/77584086?v=4?s=100" width="100px;" alt=""/>
        <br /><sub><b>Marie-Ève Picard</b></sub>
      </a>
      <br />
        <a title="Contenu">🤔</a>
    </td>
    <td align="center">
      <a href="https://github.com/pbellec">
        <img src="https://avatars.githubusercontent.com/u/1670887?v=4?s=100" width="100px;" alt=""/>
        <br /><sub><b>Pierre bellec</b></sub>
      </a>
      <br />
        <a title="Contenu">🤔</a>
    </td>
  </tr>
</table>

```{warning}
Ce chapitre est en cours de développement. Il se peut que l'information soit incomplète, ou sujette à changement.
```

## Objectifs du cours

## Anatomie d'un IRM

## Spin magnétique et champ B0
```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/xP9M486fRrY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```

## Résonance magnétique

```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/OAtffIWjzSM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```

## Contrastes T1 et T2

```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/xzmMqHB0uyM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```

## T2* et séquences d'acquisition

```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/w9z_AN3df_c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```

### Conclusions et références suggérées

### Références

```{bibliography}
:filter: docname in docnames
```

## Exercices

### Exercice 1
Classez les temps caractéristiques par ordre croissant, si possible.
 * TE
 * TR
 * T1

### Exercice 2
Vrai ou faux? la force du champ d’un IRM est liée à la taille de l’IRM.

### Exercice 3
a ou b? le spin d’un proton d’hydrogène a…
 * Une fréquence de rotation fixe, c’est la fréquence de Larmor.
 * Une fréquence de rotation variable.

### Exercice 4
Qu’est ce qui produit le bruit dans une acquisition IRM?
 * Le champ B0.
 * La climatisation pour refroidir l’aimant.
 * Les bobines de gradient.
 * L’antenne radio-fréquence.

### Exercice 5
Vrai ou faux? L’aimant de l’IRM consomme beaucoup d’électricité.

### Exercice 6
Vrai ou faux? L’IRM fonctionnelle et l’IRM de diffusion utilisent toutes les deux un contraste T2*.

### Exercice 7
Dans un image anatomique, on voit des ventricules blancs sur fond noir. S’agit-il d’une acquisition pondérée en T1 ou en T2? Expliquez pourquoi.

### Exercice 8
On décide de modifier une séquence IRM pour diminuer l’angle de bascule: les spins basculeront de 70 degrés, au lieu de 90 degrés. Quel sera l’effet sur le TR de cette modification?

### Exercice 9
On effectue une acquisition T1 avec un champ de vue de 210mm x 210mm in-plane, et un résolution in-plane de 1 mm isotrope. Quelle est la taille de la matrice d’acquisition in-plane?

### Exercice 10
On effectue une acquisition IRMf avec une résolution de 3 mm x 3 mm in-plane, une matrice in-plane de taille 64x64, une épaisseur de coupe de 3,4 mm (31 coupes). On a un TR de 2 secondes, et on acquiert 150 volumes.
Quelle est la taille du champ de vue 3D, sachant que les coupes sont acquises dans le plan axial?
Quelle est la durée de l’acquisition?
