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
>
> Les particularités des corrections à apporter lors de ces analyses statistiques seront vues en détail lors du [Chapitre 10: Cartes statistiques](https://psy3018.github.io/notes_cours_psy3018/cartes_statistiques.html).

Le traitement des données en VBM suit un processus en quatre étapes:
1. La segmentation
2. Le recalage dans un espace stéréotaxique de référence
3. Le lissage spatial
4. Les analyses statistiques

La **segmentation** est la première étape de la séquence.
Dans le contexte de la VBM, qui est une analyse de la matière grise, l'objectif principal de cette étape est de déterminer s'il y a de la matière grise dans chacun des voxels.
Un des types de segmentation automatisée qu'il est possible d'utiliser pour obtenir cette information est la segmentation probabiliste.
Dans ce genre d'algorithme, on essaie d'attribuer une étiquette concernant le contenu du voxel (air autour de la tête, liquide céphalo-rachidien, matière grise, matière blanche, etc.).
Pour ce faire, on établit la probabilité que la valeur du voxel appartienne à l'une ou l'autre des catégories possibles.
La segmentation retournera donc une carte des voxels contenant probablement de la matière grise.
Il est en effet possible que la segmentation automatique nous retourne certains autres tissus non-désirés, mais dont les valeurs étant similaires à celle de la matière grise, ne sont pas distinguées par l'algorithme de segmentation.
Il est aussi possible que des voxels se trouvant directement sur la jonction entre une zone blanche et une zone noire (par exemple, sur une paroi de matière blanche qui borderait un ventricule) aient comme valeur résultante une valeur s'apparentant plutôt au gris associé à la matière grise (valeur moyenne entre blanc et noir).
On appelle ce genre d'effet de mélange de noir et de blanc les volumes partiels (une partie du volume du voxel est blanche alors que l'autre partie est noire).
- Ce genre d'erreur est une source possible de faux positifs.

Il est aussi possible de perdre certaines structures pour lequelles le contraste entre matière blanche et matière grise ne seraient pas assez important pour que l'algorithme réussisse à les classer efficacement.
Pour ce genre de structure, il est important d'ajouter des a priori (des règles/conditions supplémentaires) dans notre algorithme de traitement afin de ne pas les perdre.
Il est aussi envisageable d'effectuer cette partie de la segmentation de façon manuelle.
- Ce genre d'erreur est une source possible de faux négatifs.

La seconde étape est l'étape du **recalage dans un espace stéréotaxique de référence** (*coregistration* en anglais).
Celle-ci sert à pouvoir mettre en relation les différents voxels à travers différents sujets (nécessaire pour les analyses statistiques).
Contrairement à la volumétrie manuelle où chaque volume à l'étude est délimité de façon à représenter la même structure d'intérêt, ni plus, ni moins, lorsque l'on fait une analyse en VBM, les unités de volume (voxels) que nous obtenons ne sont pas liées à une structure particulière.
En fonction de différentes sources de variation (par exemple: la position de la tête du sujet durant l'acquisition, la variabilité interindividuelle, etc.), un voxel *x* peut se retrouver dans des structures différentes lorsque l'on compare deux sujets.
Il faut donc que l'on procède à cette étape afin de créer une concordance des différents voxels à travers les sujets à l'étude.
L'espace stéréotaxique de référence que l'on crée ainsi est donc un système de référence sur lequel on réaligne les données de chaque sujet afin de permettre ces comparaisons.
Ainsi, on s'assure que lorsque l'on observe une coupe particulière du cerveau de différents participants, on observe aussi les mêmes structures.

> Les détails concernant l'étape du recalage seront présentés plus en détail plus loin dans le [présent chapitre](https://psy3018.github.io/notes_cours_psy3018/morphometrie.html#recalage-d-images).

L'étape suivante correspond au **lissage spatial** (aussi appelée convolution spatiale).
Le lissage s'apparente à ajouter un filtre sur l'image la rendant plus floue.
Il est nécessaire de procéder à cette étape afin d'obtenir des valeurs de densité de matière grise pour des zones qui dépasse le voxel unique.
Comme l'objectif de notre carte de densité de matière grise est de pouvoir observer des densités locales contenant des groupes (voisinages) de voxels, il est plus facile de procéder à ce genre d'observation après l'étape du lissage spatial.
Lors de cette opération, on remplace la valeur obtenue pour le voxel *x* par une moyenne pondérée par une distribution gaussienne des valeurs de ce voxel et des voxels avoisinants.
Comme c'est une moyenne pondérée, la valeur originale du voxel est celle qui aura la plus grande pondération, mais les valeurs des voxels situés directement autour vont aussi l'affecter grandement.
Mais plus on s'éloigne du voxel d'intérêt *x*, moins les autres voxels influencent sa valeur.
Afin de savoir jusqu'à quel point on s'éloignera du voxel *x* pour calculer la valeur lissée, il nous faudra un autre paramètre: le FWHM (*full width at half maximum*).
- Il est important de ne pas confondre cette valeur avec l'écart-type.

Plus la valeur de FWHM est grande, plus grand sera le rayon du voisinage de voxels qui auront un impact sur la valeur lissée du voxel *x*.

> Les détails concernant l'étape du lissage spatial seront présentés plus en détail lors du [Chapitre 4: IRM fonctionnelle](https://psy3018.github.io/notes_cours_psy3018/irm_fonctionnelle.html#pretraitement-des-donnees-d-irmf).

L'ultime étape de ce processus est celle des **analyses statistiques**.
C'est lors de cette étape que l'on parvient à obtenir les cartes finales avec lesquelles il est possible de procéder aux analyses et de tirer les observations et conclusions d'une étude en morphométrie.
On y superpose à l'image de l'espace stéréotaxique de référence les valeurs obtenues pour les régions où des informations d'intérêt statistique pour le protocol de recherche ont été obtenues.
C'est généralement le genre d'image qui sera par la suite utilisé lors de publications scientifiques.

## Recalage d'images
```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/VYN4K-K-Fjc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```
Le **recalage* est une étape cruciale du processus lorsque l'on utilise des approches automatisées basées sur des unités de volumes fixes à travers le cerveau (voxels) et que nous voulons pouvoir procéder à des comparaisons entre plusieurs sujets.
Cette étape peut aussi être nécessaire afin de comparer les données d'un même sujet acquises lors de différentes séances dans le scanneur.
En effet, à chaque fois que les images de la tête d'un sujet présentent des différences:
-À cause d'un possible mouvement de la tête durant une même séance
-À cause d'un positionnement qui peut différer légèrement d'une séance à l'autre
-À cause des différences inter-individuelles
-etc.

il y aura un besoin de recalage afin de palier à ces différences et permettre les comparaisons.
Sa principale fonction est de réaligner les images du cerveau sur une même référence, permettant ainsi de pouvoir comparer les voxels à leur équivalent (voxels représentant le même lieu physique dans les cerveaux représentés par différentes images).
Différents types de recalage sont disponibles, ont des propriétés plus ou moins complexes et permettent des comparaisons entre des cerveau présentant plus ou moins de variations inter-individuelles.

#### Recalage linéaire
Le **recalage linéaire** est la version la plus simple du processus de recalage, mais il est aussi la première étape de la version plus complexe du processus qu'est le recalage non-linéaire.
Cette technique est efficace pour aligner le contour du cerveau et/ou les structures de grande taille s'y trouvant.
En d'autres mots, cette technique peut être utilisé pour ajuster les grosses différences.
Le recalage linéaire est une combinaison plus ou moins complexe, selon les besoins, de trois paramètres de transformation linéaire:
-La rotation (pour corriger si la tête a pivoté)
-La translation (si la tête est décalée latéralement)
-La mise à l'échelle (afin d'ajuster la taille et/ou la forme du cerveau)

Chacun de ces paramètres peut être modifié le long des trois axes (espace tridimensionnel), ce qui nous donne un total de 9 paramètres pouvant être ajustés.
Ces paramètres seront estimés par un algorithme et nous permettront de réaligner grossièrement les images de cerveau étudiées.

#### Recalage non-linéaire
Le **recalage non-linéaire** est une étape plus complexe permettant des ajustements localisés, tels que des asymétries, grâce à une norme (*template*) basée sur notre espace stéréotaxique de référence.

## Recalage d'images (CETTE SECTION SEMBLE REDONDANTE??!!)
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
