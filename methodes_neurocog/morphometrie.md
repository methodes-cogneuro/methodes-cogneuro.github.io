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

> Pour un rappel concernant termes et les différents types de coupes du cerveau, veuillez vous référer au [Chapitre 1: Cartes cérébrales](https://psy3018.github.io/notes_cours_psy3018/cartes_cerebrales.html#irm-structurelle).

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

L'**approche par voxel**, aussi mieux connue sous le nom de ***voxel-based morphometry*** (ou **VBM**) est une autre approche qu'il est possible d'employer afin de segmenter différentes aires d'intérêt du cerveau.
Son objectif est de mesurer la densité de matière grise à l'intérieur et immédiatement autour d'un voxel donné.
Cette approche est donc moins limitée par le besoin d'avoir des frontières préétablies claires entre les différentes structures à l'étude.
Lorsque répétée pour l'entièreté du volume du cerveau, on peut obtenir une carte tridimensionnelle de la densité de matière grise à travers celui-ci.
L'avantage premier de cette approche est son économie au niveau du temps nécessaire à un.e chercheur.e pour l'étape de la segmentation.
En effet, comme cette technique présente une approche de segmentation automatisée, la présence d'une personne externe ne devient nécessaire que lors de l'étape de la vérification de la segmentation.
Par contre, cette approche ayant une quantité importante de points de mesure (liés à chaque voxel étudié), elle pose aussi un sérieux problème de **comparaisons multiples** lorsque vient le temps de faire les analyses statistiques.


> Les particularités des analyses statistiques en neuroimagerie seront vues en détail lors du [Chapitre 6: Régression linéaire](https://psy3018.github.io/notes_cours_psy3018/regression.html).
> Les particularités des corrections à apporter lors de ces analyses statistiques seront vues en détail lors du [Chapitre 10: Cartes statistiques](https://psy3018.github.io/notes_cours_psy3018/cartes_statistiques.html).


Le traitement des données en VBM suit un processus en quatre étapes:
1. La segmentation
2. Le recalage dans un espace stéréotaxique de référence
3. Le lissage spatial
4. Les analyses statistiques

La **segmentation** est la première étape de la séquence.
L'objectif de cette étape est de déterminer s'il y a de la matière grise dans chacun des voxels.
La segmentation retournera donc une carte des voxels contenant de la matière grise.

La seconde étape est l'étape du **recalage dans un espace stéréotaxique de référence**.
Celle-ci sert à pouvoir mettre en relation les différents voxels à travers différents sujets.
Contrairement à la volumétrie manuelle où chaque volume à l'étude est délimité de façon à représenter la même structure d'intérêt, ni plus, ni moins, lorsque l'on fait une analyse en VBM, les unités de volume que nous obtenons ne sont pas liées à une structure particulière.
En fonction de différentes sources de variation (par exemple: la position de la tête du sujet durant l'acquisition, la variabilité interindividuelle, etc.), un voxel *x* peut se retrouver dans des structures différents lorsque l'on compare deux sujets.
Il faut donc que l'on procède à cette étape afin de créer une concordance des différents voxels à travers les sujets à l'étude.
L'espace stéréotaxique de référence que l'on crée est donc un système de référence sur lequel on réaligne les données de chaque sujet afin de permettre ces comparaisons.

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
