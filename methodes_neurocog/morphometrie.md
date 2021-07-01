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
(morphometrie-chapitre)=
# Analyses morphométriques

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/eddyfortier">
        <img src="https://avatars.githubusercontent.com/u/72314243?v=4?s=100" width="100px;" alt=""/>
        <br /><sub><b>Eddy Fortier</b></sub>
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

Ce troisième chapitre introduit différentes approches utilisées afin de modéliser et d'exploiter les données acquises grâce aux techniques d'imagerie par résonance magnétique anatomique vues lors du cours 2.
Tout d'abord, on y survolera des approches basées sur l'analyse de **volumes** telles que la **volumétrie manuelle** et l'**approche par voxel (*voxel-based morphometry* ou VBM)**.
On tente par ce type d'analyse d'identifier et/ou de délimiter différentes aires du cerveau.
Ce processus rendra par la suite possible l'étude des tissus présents dans ces différentes segmentations/unités de volume.
Il sera ensuite question de l'utilisation du **recalage** et du **contrôle de qualité** dans le traitement des données d'imagerie.
Nous terminerons cette séance avec une famille d'approches permettant l'étude de l'épaisseur corticale: les **analyses de surface**.

## Morphométrie

En neurosciences, la **morphométrie** est l'étude de la forme du cerveau et de ses structures.
Le terme morphométrie vient de deux termes tirés du grec ancien: *morphos* (forme) et *métron* (mesure).
La morphométrie est donc la "mesure" de la "forme".
Cette discipline se concentre sur la caractérisation des dimensions et des formes des différentes structures d'intérêt.
Pour ce faire, il est nécessaire de pouvoir observer clairement les délimitations de ces structures.
L'utilisation de ce genre de technique permet aussi de faire des comparaisons inter-individuelles.
On pourrait en effet vouloir comparer les variations dans la forme de divers structures à travers les cerveaux de différentes personnes.
De telles comparaisons peuvent être informatrices au niveau du stade développemental d'un sujet, ou même, de la présence de certaines lésions ou pathologies.

## Volumétrie manuelle
```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/CzsZdtqBmCg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```

La **volumétrie manuelle** est une approche qui peut sembler assez simple a priori, mais qui nécessite du temps et un protocol rigoureux ayant des critères de segmentation clairs.
Cette façon de faire est essentielle afin d'assurer une segmentation logique, un bon niveau de reproductibilité des résultats et un accord inter-juge acceptable.
La procédure nécessitera l'utilisation d'un logiciel permettant de dessiner les "frontières" de chacune des aires que l'on veut pouvoir identifier sur les images obtenues lors du scan d'un cerveau.
On commencera d'abord par identifier ce contour sur chaque coupe où la structure est présente dans un premier plan (par exemple, sur une coupe axiale), puis il faudra aller corriger cette délimitation sur chaque coupe prise dans un second plan (comme une coupe sagitale) et finalement, répéter de nouveau cette correction sur le troisième plan (une coupe coronale).

> Pour un rappel concernant termes et les différents types de coupes du cerveau, veuillez vous référer au [Chapitre 1: Cartes cérébrales](https://psy3018.github.io/notes_cours_psy3018/cartes_cerebrales.html).

Le processus nécessaire à l'obtention d'une segmentation finale précise d'une structure unique peut donc être très long et ardu.
Il devra d'ailleurs être répété de nouveau pour chaque nouvelle structure d'intérêt.

## Voxel-based morphometry
```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/yyUKkPaG3Q8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```

## Recalage d'images
```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/VYN4K-K-Fjc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```

## Recalage d'images
```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/VYN4K-K-Fjc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```

## Analyses de surface
```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/S-8rk7PlWBI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```
