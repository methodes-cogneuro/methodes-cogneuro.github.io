---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst  
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
(tep-chapitre)=
# Tomographie par émission de positrons

## Objectifs
La [tomographie par émission de positrons](https://fr.wikipedia.org/wiki/Tomographie_par_%C3%A9mission_de_positons) est une technique d'imagerie qui permet de cibler de nombreuses caractéristiques du cerveau, aussi bien au niveau structurel que fonctionnel. Couplée avec un radiotraceur de Fluorodésoxyglucose (FDG), la TEP est couramment utilisée pour cartographier l'activité du cerveau au travers de différentes conditions expérimentales. Avec d'autres traceurs, elle permet de cartographier les dépôts de protéines anormales, ou bien encore la présence de différents récepteurs de neurotransmetteurs.

```{figure} tep/tep.jpg
---
width: 600px
name: tep-scanner-fig
---
Scanneur TEP. Image par [Jejecam](https://commons.wikimedia.org/wiki/User:Jejecam) tirée de [wikipedia](https://commons.wikimedia.org/wiki/File:TEP-CT_2009.jpg) sous licence [CC-BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0).
```

Les objectifs spécifiques du cours sont:
*   Principes physiques et physiologiques de l'imagerie TEP.
*   Génération d'images en TEP.
*   Principaux types d'images en TEP pour les neurosciences cognitives.

## Principes physiques et physiologiques

### Radiotraceurs
```{figure} tep/radiotraceur.png
---
width: 800px
name: radiotraceur-fig
---
Un radiotraceur est un produit radioactif qui est injecté au participant de recherche (**a**). Les molécules de ce traceur comportent deux parties: un isotope qui émet des rayons radioactifs, et un précurseur qui va s'accrocher à une cible dans le cerveau (**b**). Cette cible peut être par exemple les récepteurs dopaminergiques (**c**). Image **a** par [rumruay](https://www.shutterstock.com/g/rumruay) disponible sur [shutterstock](https://www.shutterstock.com/image-vector/spect-scan-radiologist-single-computed-image-1329727577) ID `1329727577`, utilisée sous licence shutterstock standard. Image **b** par L. Bellec, sous licence [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/). Image **c** par [simurggdesign](https://www.shutterstock.com/g/simurggdesign) disponible sur [shutterstock](https://www.shutterstock.com/image-vector/vector-illustration-synapse-neurotransmitter-diagram-synapses-2050315106) ID `2050315106`, utilisée sous licence shutterstock standard.
```
L'idée de base de la TEP est d'injecter un produit radioactif, appelé radiotraceur, qui va s'accumuler dans une partie bien définie du cerveau, comme par exemple les [récepteurs dopaminergiques](https://fr.wikipedia.org/wiki/Récepteur_dopaminergique) de type D2. On réalise une image des parties du cerveau qui émettent de la radioactivité, et cela nous permet de quantifier la concentration de la cible du radiotraceur, soit par exemple la présence de récepteurs D2. Le radiotraceur est composé de deux parties: un *radioisotope médical*, qui est un atome radioactif, qui est lié à un composé non-radioactif nommé *précurseur* (ou [*ligand*](https://fr.wikipedia.org/wiki/Ligand_(chimie))), qui va s'accrocher ou s'accumuler dans une *cible* (comme les récepteurs D2). Le *précurseur* est sélectionné pour son affinité avec la *cible*, et représente un choix clé de la conception d'un radiotraceur, et nous permet de capturer une caractéristique particulière du cerveau. Nous verrons dans la prochaine section comment l'accumulation d'isotopes est détectée par le scanner TEP. Nous allons maintenant discuter plus en détail des différents radioisotopes, précurseurs, et ce qui fait un bon radiotraceur.  

```{admonition} Mini-glossaire
:class: tip
:name: glossaire-tep

*   **Isotope (ou radioisotope)** : Un atome qui suit un processus de désintégration radioactif en émettant des radiations détectables en dehors du corps.

*   **Précurseur (ou ligand)** : Un composant *non-radioactif* qui contient un segment actif se liant à la cible, et pouvant être facilement fusionné au radioisotope. En radiochimie, le mot *précurseur* désigne plus précisément la molécule qui réagit avec l'isotope pendant la synthèse du traceur; dans ce cours, on l'emploie par simplification pour la partie du traceur qui se lie à la cible.

*   **cible (ou biomarqueur)** : La *cible* est un biomarqueur du phénomène qu'on cherche à mesurer.

*   **Radiotraceur (ou radioligand)** : Une molécule marquée *délivrant le radioisotope* jusqu'au *biomarqueur cible*; tout ça *in vivo*. Autrement dit, c'est la combinaison de l'isotope et du précurseur.
```

### Isotopes et radioactivité
```{figure} tep/isotope.png
---
width: 800px
name: isotope-fig
---
Un isotope radioactif est un atome dont le ratio entre le nombre de protons et de neutrons est instable (**a**). Cette structure instable amène à l'émission d'un positron, qui s'annihile en percutant un électron, ce qui produit l'émission de rayons gamma opposés (**b**). Les rayons gamma sont des photons à très haute énergie, qui peuvent traverser les tissus biologiques, mais sont arrêtés par le plomb (**c**). Images **a** et **b** adaptées d'une image de [OSweetNature](https://www.shutterstock.com/g/OSweetNature) disponible sur [shutterstock](https://www.shutterstock.com/image-vector/beta-decay-nuclear-energy-diagram-showing-1509181103) ID `1509181103`, utilisée sous licence shutterstock standard. Image **c** par [OSweetNature](https://www.shutterstock.com/g/OSweetNature) disponible sur [shutterstock](https://www.shutterstock.com/image-vector/types-radiation-penetrating-power-through-paper-1169023357) ID `1169023357`, utilisée sous licence shutterstock standard.
```

L'imagerie TEP repose sur l'accumulation d'isotopes radioactifs dans l'organisme, qui sont détectés par l'appareil TEP et permettent de construire une image. Mais comment cette accumulation peut-elle être mesurée? Les isotopes utilisés en TEP sont choisis parce que leur noyau atomique est instable. Un noyau stable contient des protons et des neutrons dans des proportions équilibrées; un noyau instable a trop de l'un ou de l'autre. Les isotopes de la TEP ont un excès de protons. Ils se stabilisent par une désintégration dite *bêta plus* (β+): un proton se transforme en neutron, en émettant un positron (l'antiparticule de l'électron, de charge positive) et un neutrino électronique. Le positron parcourt une courte distance dans les tissus, puis rencontre un électron: les deux s'annihilent, et leur masse est convertie en deux photons qui partent dans des directions diamétralement opposées. Ces photons à haute énergie sont appelés *rayons gamma*.

Les radioisotopes sont produits dans un cyclotron, et vont commencer à se désintégrer immédiatement. La **demi-vie** du radiotraceur correspond au temps nécessaire pour que la moitié des atomes radioactifs contenus dans le traceur se soient transformés en atomes stables. Chaque désintégration atomique est aléatoire, mais à cause du grand nombre d'atomes contenus dans une dose de radiotraceurs, la demi-vie est un phénomène très stable. L'imagerie TEP utilise un certain nombre d'isotopes bien connus. Certains, comme le fluor 18 ($^{18}$**F**), ont une demi-vie assez longue. Cela nous permet de les produire sur un site spécialisé, puis de les transporter sur le lieu de l'étude. D'autres radioisotopes, comme l'oxygène 15 ($^{15}$**O**), ont une demi-vie très courte. Au niveau logistique, ceci nécessite que le cyclotron se trouve à proximité du site où l'expérimentation se déroule, car le radiotraceur doit être utilisé immédiatement après sa production. Référons nous au tableau d'isotopes pour comprendre de combien de temps nous disposons pour effectuer un scan TEP en fonction de l'isotope utilisé.

```{admonition} Tableau d'isotopes TEP
:class: tip
:name: isotopes-table
| **Radioisotopes**      | **Demi-vie** |
| ---------------------- | ------------ |
| $^{18}$**F**           | 110 min      |
| $^{11}$**C**           | 20,4 min     |
| $^{13}$**N**           | 9,97 min     |
| $^{15}$**O**           | 2,0 min      |
| $^{89}$**Zr**          | 78,4 h       |
| $^{124}$**I**          | 4,18 j       |
| $^{64}$**Cu**          | 12,7 h       |
| $^{68}$**Ga**          | 67,7 min     |

```

### Dose de radiation
Injecter un produit radioactif à une personne en santé, pour la recherche, n'est pas anodin. Pour un examen au FDG, la dose reçue est de l'ordre de quelques millisieverts (mSv), soit à peu près ce que l'on reçoit en un à deux ans d'exposition à la radioactivité naturelle (environ 2 à 3 mSv par an). Le risque individuel est faible, mais il s'additionne d'un examen à l'autre. Les comités d'éthique limitent donc le nombre d'examens TEP qu'un même participant peut passer, et les enfants, plus sensibles aux radiations, sont rarement inclus dans des études TEP de recherche. Cette contrainte pèse sur la conception des expériences: une étude TEP compte peu de conditions par participant, et l'on préfère une technique sans radiation, comme l'IRMf, dès que la question de recherche le permet.

### Précurseurs et biomarqueurs
```{figure} tep/fdg.jpg
---
width: 500px
name: fdg-fig
---
Molécule de Fluorodeoxyglucose. Chaque sphère représente un atome (noir: carbone, rouge: oxygène, blanc: hydrogène, vert: $^{18}$**F**). Image par [StudioMolekuul](https://www.shutterstock.com/g/molekuul) disponible sur [shutterstock](https://www.shutterstock.com/image-illustration/fludeoxyglucose-18f-fluorodeoxyglucose-fdg-cancer-imaging-149603819) ID `149603819`, utilisée sous licence shutterstock standard.
```
Le précurseur peut être une molécule endogène (déjà présente dans l'organisme, comme l'eau, l'oxygène ou le glucose) dont la concentration est altérée en présence de l'activité cérébrale ou bien d'une pathologie. Le précurseur peut aussi être une molécule qui va s'accrocher à une partie spécifique du cerveau (par exemple les récepteurs d'un certain neurotransmetteur). Une réaction chimique est utilisée pour synthétiser une molécule qui regroupe le radioisotope et le précurseur. Dans l'exemple du FDG, on part d'une molécule de glucose, dont un groupe hydroxyle (un atome d'oxygène lié à un atome d'hydrogène) est remplacé par du $^{18}$**F** produit par un cyclotron, voir {numref}`fdg-fig`. Le FDG est un *analogue* du glucose: les cellules le captent comme du glucose, mais ne peuvent pas le consommer jusqu'au bout. Comme nous le verrons plus loin dans ce chapitre, le FDG s'accumule ainsi dans les cellules qui consomment le plus de glucose. Le FDG agit donc comme un biomarqueur de l'activité cérébrale.

### Qualités d'un radiotraceur
Pour être utile en neuroimagerie, un radiotraceur doit posséder les qualités suivantes:
 * **Perméabilité à la barrière hémato-encéphalique** : le traceur injecté dans le sang doit pouvoir se rendre au cerveau.
 * **Spécificité d'arrimage**: le traceur doit se fixer seulement sur la bonne cible.
 * **Affinité d'arrimage** : même avec une basse concentration de la cible, le traceur doit pouvoir s'y arrimer.
 * **Rapidité d'arrimage** : la désintégration de l'isotope contraint temporellement le processus d'arrimage. La désintégration doit nécessairement être plus lente que le processus métabolique d'arrimage.
 * **Stabilité métabolique** : le traceur ne doit pas se désagréger avant d'atteindre sa cible. Ici, on ne parle pas de la désintégration de l'isotope, mais plutôt de la dégradation du traceur par l'organisme. Par exemple, un traceur dégradé dans le sang ou le foie avant d'atteindre le cerveau, ou dont les fragments radioactifs entreraient eux-mêmes dans le cerveau, brouillerait la mesure.

## Génération d'images en TEP
Nous avons couvert les principes physiques et physiologiques des radiotraceurs. Il s'agit maintenant de préciser comment l'activité des radiotraceurs peut être utilisée pour générer une image. Pour cela, nous avons besoin de deux pièces d'infrastructure: le cyclotron et le scanner TEP. Nous aurons aussi besoin de méthodes d'analyses d'image.

### Cyclotron
```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/6BxyqFK2KRI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```

Le cyclotron permet de fabriquer des noyaux atomiques instables de façon contrôlée. Cette production fait partie du processus de génération d'images TEP, car les radioisotopes sont instables et doivent être préparés peu de temps avant l'expérience. La vidéo ci-dessus présente le fonctionnement d'un cyclotron. Brièvement, un cyclotron est un accélérateur de particules compact, qui permet de bombarder des atomes avec des protons à haute énergie, et de transformer leur noyau en isotope radioactif. Par exemple, le $^{18}$**F** est produit en bombardant de l'eau enrichie en oxygène 18.

```{figure} tep/radiochemistry.jpg
---
width: 600px
name: radiochemistry-fig
---
Module de synthèse radiochimique automatisé. Image par [Bork](https://www.shutterstock.com/g/stratum) disponible sur [shutterstock](https://www.shutterstock.com/image-photo/manipulation-cell-43798612) ID `43798612`, utilisée sous licence shutterstock standard.
```

Une fois l'isotope produit, il peut être nécessaire d'effectuer des réactions chimiques pour fusionner l'isotope avec le précurseur, et synthétiser le radiotraceur. C'est le cas par exemple pour le FDG, où le $^{18}$**F** va être intégré à une molécule de glucose. Comme les réactions chimiques font intervenir des composés radioactifs, cette étape est réalisée dans un laboratoire automatisé qui protège les opérateurs des radiations ({numref}`radiochemistry-fig`).

```{figure} tep/injection_tep.jpg
---
width: 500px
name: injection-tep-fig
---
Injecteur plombé permettant de protéger l'opérateur TEP des radiations émises par le radiotraceur. Image par [JeJecam](https://commons.wikimedia.org/wiki/User:Jejecam) tirée de [wikipedia](https://commons.wikimedia.org/wiki/File:Injecteur_plombe.jpg) sous licence [CC-BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0).
```
Une fois produite, la dose de radiotraceur doit être acheminée rapidement pour être injectée au participant de recherche. La demi-vie du FDG est d'environ deux heures, ce qui permet de produire le radiotraceur et de l'utiliser sur des sites différents, si nécessaire. Durant le transport, la dose de radiotraceurs émet continuellement des radiations, et il est nécessaire d'utiliser des équipements de protection ({numref}`injection-tep-fig`).

### Détection de coincidences
```{figure} tep/coincidence_tep.png
---
width: 800px
name: coincidence-fig
---
Principe d'un scanner TEP. Lors d'une annihilation (en bas à gauche), deux rayons gamma partent dans des directions opposées et frappent presque simultanément deux capteurs de l'anneau (en rouge). Une unité de traitement détecte ces coïncidences, qui servent ensuite à reconstruire l'image. Image par [Jens Maus](https://github.com/jens-maus) tirée de [wikipedia](https://commons.wikimedia.org/wiki/File:PET-schema.png) sous licence [domaine public](https://fr.wikipedia.org/wiki/Domaine_public_(propri%C3%A9t%C3%A9_intellectuelle)).
```
Une fois le radiotraceur injecté et accumulé sur la cible, la radioactivité est émise par les parties du cerveau que l'on souhaite étudier. Pour chaque événement radioactif, les deux rayons gamma sortent de la boîte crânienne dans des directions diamétralement opposées. Le scanner TEP est muni de capteurs (ou de caméras, car ces capteurs mesurent des photons) disposés en cercle autour de la tête du participant ({numref}`coincidence-fig`). Comme les rayons gamma se déplacent à grande vitesse, ils viennent frapper deux caméras pratiquement au même moment (à quelques nanosecondes près). Cette arrivée simultanée, appelée **coïncidence**, est détectée par le scanner TEP. On sait alors que l'annihilation a eu lieu quelque part sur la droite qui relie les deux capteurs, appelée *ligne de réponse*, et il est possible de compter les événements accumulés au cours du temps pour l'ensemble des lignes de réponse. Pour le FDG, le scanner enregistre plusieurs millions d'événements par minute, et on effectue une mesure accumulée sur plusieurs dizaines de minutes. Mais ces mesures, appelées **projections**, ne correspondent pas (encore) à une image du cerveau.

Tous les rayons gamma ne sortent pas de la tête: une partie est absorbée ou déviée par les tissus traversés, et ce d'autant plus que le trajet est long. Sans correction, le centre du cerveau paraîtrait moins radioactif que sa surface. On corrige cette *atténuation* à l'aide d'une carte de la densité des tissus, obtenue le plus souvent par un tomodensitomètre (un scanner à rayons X, ou CT) intégré au même appareil: c'est le cas du scanner TEP-CT de la {numref}`tep-scanner-fig`. Il existe aussi des appareils qui combinent la TEP et l'IRM.

### Tomographie
```{figure} tep/projection.gif
---
width: 800px
name: projection-fig
---
Illustration de la construction de projections multiples d'une image 2D. Image par [Lucas VB](https://commons.wikimedia.org/wiki/User:LucasVB) tirée de [wikipedia](https://commons.wikimedia.org/wiki/File:Radon_transform_sinogram.gif) sous licence [CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.en).
```
La {numref}`projection-fig` illustre comment un objet 2D peut être converti en une série de projections. La tomographie est une opération qui consiste à reconstruire une image 3D du cerveau à partir de la combinaison des mesures prises par l'ensemble des caméras. Si l'on disposait de l'ensemble des projections possibles, on pourrait en théorie faire une reconstruction parfaite. En pratique, on est limité par la taille et le nombre des caméras du scanner TEP. La figure ci-dessous illustre une image simplifiée de coupe 2D du cerveau, le processus de projections multiples, et une reconstruction de l'image à partir des projections.

Pour un appareil TEP humain, la résolution spatiale est de l'ordre de 4 à 7 mm. Elle est limitée par la taille des caméras, mais aussi par la physique elle-même: le positron parcourt une courte distance avant de s'annihiler (moins d'un millimètre en moyenne pour le $^{18}$**F**, quelques millimètres pour l'$^{15}$**O**), et la ligne de réponse indique où a eu lieu l'annihilation, pas la désintégration. De plus, chaque ligne de réponse ne compte qu'un nombre limité d'événements: l'image reconstruite est bruitée, et on la lisse généralement, ce qui rapproche sa {ref}`résolution spatiale effective <resolution-spatiale-warning>` du centimètre.

```{code-cell} ipython 3
:tags: ["hide-input", "remove-output"]
# Importe les librairies
import numpy as np
import matplotlib.pyplot as plt
from skimage.data import shepp_logan_phantom
from skimage.transform import radon, rescale

# Télécharge données fantôme
image = shepp_logan_phantom()
image = rescale(image, scale=0.4, mode='reflect')

# Prépare la figure
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4.5))

# Image originale
ax1.set_title("Image originale")
ax1.imshow(image, cmap=plt.cm.Greys_r)

# Projections
theta = np.linspace(0., 180., max(image.shape), endpoint=False)
sinogram = radon(image, theta=theta)
dx, dy = 0.5 * 180.0 / max(image.shape), 0.5 / sinogram.shape[0]
ax2.set_title("projections")
ax2.set_xlabel("Angle projection (deg)")
ax2.set_ylabel("Position projection(pixels)")
ax2.imshow(sinogram, cmap=plt.cm.Greys_r,
           extent=(-dx, 180.0 + dx, -dy, sinogram.shape[0] + dy),
           aspect='auto')

# Reconstruction
from skimage.transform import iradon

reconstruction_fbp = iradon(sinogram, theta=theta, filter_name='ramp')
ax3.set_title("Image reconstruite")
ax3.imshow(reconstruction_fbp, cmap=plt.cm.Greys_r)
fig.tight_layout()

fig.savefig(
  "tep/radon-fig.png",
  dpi=300,
  bbox_inches="tight",
  pad_inches=0
)
```

```{figure} tep/radon-fig.png
---
name: radon-fig
align: center
width: 800px
---
Une image 2D ressemblant à une coupe de cerveau (image de gauche). Représentation de la même image avec une série de projections correspondant à différentes positions dans l'espace et différents angles de projection (image du centre). Image reconstruite à partir des projections (image de droite). Cette figure est générée par du code python à l'aide de la librairie [scikit-image](https://scikit-image.org/docs/dev/auto_examples/transform/plot_radon_transform.html) (cliquer sur + pour voir le code), et est distribuée sous licence CC-BY.
```
## TEP en neurosciences cognitives
Nous allons maintenant discuter de quelques radiotraceurs en TEP et de leur utilisation en neuroscience cognitive

### FDG TEP et métabolisme du glucose
```{figure} ./cartes_cerebrales/fig_tep.jpg
---
width: 800px
name: tep2-fig
---
Montage de coupes axiales d'un scanner TEP avec un radiotraceur FDG, illustrant le niveau d'activité métabolique du glucose durant la durée du scan. Image [shutterstock](https://www.shutterstock.com) ID `1342194254`.
```
Le [$^{18}$**F**]FDG est capté par les cellules comme du glucose normal. Le glucose, comme l'oxygène, est apporté au cerveau par le sang, et nous avons vu que l'IRMf et l'imagerie optique mesurent la réponse vasculaire à l'activité neuronale, c'est-à-dire le {ref}`couplage neurovasculaire <couplage-neurovasculaire-irmf-section>`. Le FDG mesure autre chose: la consommation de glucose elle-même. Le cerveau n'extrait qu'une faible fraction du glucose qui le traverse (de l'ordre de 10%). Ce qui détermine la quantité de FDG captée est donc la demande des cellules, bien plus que l'apport sanguin. On parle parfois de *couplage neurométabolique*, pour le distinguer du couplage neurovasculaire.

Une fois dans la cellule, le glucose est transformé par une enzyme, l'hexokinase, qui lui ajoute un groupe phosphate: c'est la première étape de sa consommation. L'hexokinase transforme aussi le FDG, en FDG-6-phosphate. Mais à cause de l'atome de fluor, le FDG-6-phosphate ne peut pas poursuivre les étapes suivantes, et il ne peut pas non plus ressortir de la cellule: il reste piégé. Plus une région consomme de glucose, plus le FDG s'y accumule. Ce *piégeage métabolique* est ce qui rend le FDG utile: le glucose normal, lui, est consommé et ne laisse pas de trace. Le FDG est capté à la fois par les neurones et par les astrocytes (un type de cellule gliale), et des travaux suggèrent que les astrocytes contribuent fortement au signal ([Zimmer et al., 2017](https://hdl.handle.net/10.1038%2Fnn.4492)). Dans tous les cas, la radioactivité accumulée reflète le métabolisme du glucose, et donc indirectement l'activité neuronale. Le FDG qui n'a pas été capté est éliminé par les reins, et le $^{18}$**F** piégé finit par se désintégrer.

Le FDG s'accumule pendant environ 30 à 40 minutes après l'injection, et l'image reflète la consommation de glucose moyenne pendant cette période. Une acquisition FDG ne capture donc qu'une seule condition. Pour contraster deux conditions (par exemple repos et tâche visuelle), il faut deux sessions, souvent à des jours différents, puisque le traceur de la première injection reste présent pendant plusieurs heures. La TEP au FDG se prête mieux à la comparaison de groupes, par exemple en fonction de l'âge des participants ou de leur santé cognitive.

```{admonition} Traitement des images TEP
:class: tip
:name: traitement-fdg
Les données TEP doivent être prétraitées avant les analyses statistiques. Il est courant de normaliser la carte par rapport à une *région de référence*, où le traceur est présent mais ne se lie pas à sa cible. Pour les traceurs des plaques amyloïdes, par exemple, on utilise souvent la matière grise du cervelet (la structure située à l'arrière du cerveau, sous les lobes occipitaux), où les plaques sont rares. Le rapport entre la valeur de chaque voxel et la valeur moyenne dans la région de référence s'appelle le SUVR (*standardized uptake value ratio*): un SUVR proche de 1 indique une fixation comparable à celle de la région de référence, et un SUVR plus élevé une fixation sur la cible. Pour le FDG, qui est capté partout, on normalise plutôt par une région peu affectée par la condition étudiée (par exemple le pont, une structure du tronc cérébral), ou par la moyenne du cerveau entier. Certaines corrections peuvent aussi être appliquées sur les images, comme une correction de l'{ref}`effet de volume partiel <volume-partiel-tip>`, qui pèse lourd vu la faible résolution de la TEP. Enfin, il est possible de recaler l'image TEP sur une IRM structurelle de chaque sujet, pour visualiser la localisation des activations, et aussi appliquer un recalage dans un espace stéréotaxique pour effectuer des analyses statistiques de groupe similaires à l'IRMf.
```

### TEP à l'eau marquée et débit sanguin
Le FDG n'est pas le seul traceur qui a servi à cartographier l'activité cérébrale. Dans les années 1980 et 1990, avant l'IRMf, les études d'activation en TEP utilisaient surtout de l'eau marquée à l'oxygène 15 ([$^{15}$**O**]H$_2$O). L'eau traverse librement la barrière hémato-encéphalique, et sa distribution reflète le débit sanguin cérébral: ce traceur-là mesure donc bien la réponse vasculaire, comme l'IRMf. Sa demi-vie très courte (environ 2 minutes, voir le {ref}`tableau d'isotopes <isotopes-table>`) est ici un avantage: une image s'acquiert en une minute environ, et la radioactivité disparaît en une dizaine de minutes. On peut donc répéter l'injection une dizaine de fois dans une même session, en alternant les conditions expérimentales. C'est ainsi qu'ont été réalisées des études fondatrices des neurosciences cognitives, comme la cartographie des régions impliquées dans la lecture et la production de mots ([Petersen et al., 1988](https://hdl.handle.net/10.1038%2F331585a0)). En contrepartie, l'expérience doit avoir lieu à côté d'un cyclotron.
### Imagerie des récepteurs
```{figure} ./tep/receptors-tep.jpeg
---
width: 800px
name: receptors-fig
---
Images de traceurs TEP pour 18 récepteurs et transporteurs de neurotransmetteurs différents, au travers de 9 systèmes de neurotransmetteurs et 1200 participants en santé. Tiré de la prépublication de [Hansen et al. (2021)](https://hdl.handle.net/10.1101%2F2021.10.28.466336) sous licence CC-BY 4.0, publiée depuis dans [Nature Neuroscience (2022)](https://hdl.handle.net/10.1038%2Fs41593-022-01186-3).
```
Il existe de nombreux neurotransmetteurs dans le cerveau. Ils jouent un rôle clé dans la communication entre neurones, au niveau des synapses, où chacun agit sur des **récepteurs** spécifiques: des protéines qui reconnaissent un messager chimique et y répondent. Certains neurotransmetteurs sont particulièrement impliqués dans des processus cognitifs, comme la dopamine dans la récompense. Il est donc utile de cartographier la distribution spatiale des récepteurs de différents neurotransmetteurs ({numref}`receptors-fig`). Le récepteur joue alors le rôle de cible, et l'on conçoit un ligand, c'est-à-dire une molécule qui s'arrime au récepteur, auquel on attache un radioisotope. Des ligands ont par exemple été développés pour les récepteurs dopaminergiques de type D2 et D3, comme le [$^{11}$**C**]raclopride. Ce traceur entre en compétition avec la dopamine produite par le cerveau pour les mêmes récepteurs: lorsque de la dopamine est libérée, moins de raclopride s'arrime. On peut ainsi mesurer indirectement une libération de dopamine, par exemple dans le striatum (un ensemble de noyaux situés en profondeur, sous le cortex) pendant que des participants jouent à un jeu vidéo ([Koepp et al., 1998](https://hdl.handle.net/10.1038%2F30498)).

### Radioligands pour les plaques Béta amyloïde (A${\beta}$)
```{figure} ./tep/pib.jpg
---
width: 500px
name: pib-fig
---
Comparaison d'un scan TEP [$^{11}$**C**] PIB entre un sujet présentant une démence de type Alzheimer et un participant cognitivement sain. Les aires jaunes et rouge suggèrent l'accumulation de plaques A${\beta}$. Image par Klunkwe tirée de [wikipedia](https://commons.wikimedia.org/wiki/File:PiB_PET_Images_AD.jpg) sous licence [CC-BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0).
```
L'amyloïde bêta provient d'une protéine plus grande, la protéine précurseur de l'amyloïde (APP). Elle peut s'agréger en plaques, notamment dans la maladie d'Alzheimer. Selon l'hypothèse dite de la *cascade amyloïde*, ces plaques perturberaient la communication entre neurones et déclencheraient une réaction inflammatoire qui accélère la dégénérescence des tissus cérébraux. Cette hypothèse reste débattue, mais les plaques A${\beta}$ sont un biomarqueur établi de la maladie d'Alzheimer. Le premier radiotraceur des plaques A${\beta}$ est le [$^{11}$**C**]PIB (*Pittsburgh compound B*). Sa demi-vie de 20 minutes impose de le produire sur place, à côté d'un cyclotron. Des traceurs marqués au $^{18}$**F**, comme le florbétapir ([$^{18}$**F**]AV45), ont été développés depuis: leur demi-vie plus longue permet de les distribuer à des sites d'imagerie qui n'ont pas de cyclotron. Comme tout traceur, ils ne sont pas parfaitement spécifiques, et une partie du signal ne correspond pas à des plaques. Précisons enfin que les plaques peuvent être présentes sans les symptômes cognitifs de la maladie.

### Radioligands pour la protéine tau
Une deuxième protéine anormale caractérise la maladie d'Alzheimer: la protéine tau, qui forme des enchevêtrements (ou écheveaux) à l'intérieur des neurones. Des radiotraceurs de la protéine tau, comme le [$^{18}$**F**]flortaucipir, sont apparus plus récemment. Contrairement aux plaques A${\beta}$, la quantité de tau suit de près les symptômes cognitifs. Sa distribution suit aussi une progression typique: elle apparaît d'abord dans le lobe temporal médian (la face interne du lobe temporal, qui comprend l'hippocampe), puis s'étend au reste du cortex au fil de la maladie.

## Conclusion et résumé

*   Un radiotraceur est composé d'un précurseur, qui s'accroche à une cible, et d'un isotope, qui se désintègre en émettant des rayons gamma.
*   En enregistrant les coïncidences d'arrivée de photons, on peut reconstruire une représentation 3D de la concentration du radiotraceur à l'aide d'une opération dite de tomographie.
*   La demi-vie de l'isotope dicte la logistique d'une étude, et la dose de radiation limite le nombre d'examens par participant.
*   La TEP au FDG est utilisée pour étudier le métabolisme du glucose: le FDG est piégé dans les cellules qui consomment du glucose. Une acquisition FDG ne capture qu'une condition; l'eau marquée à l'oxygène 15 mesure le débit sanguin et permet d'alterner plusieurs conditions dans une session.
*   On peut imager la densité des récepteurs de différents neurotransmetteurs, par exemple ceux de la dopamine.
*   Des radioligands ont été conçus spécifiquement pour imager les plaques A${\beta}$ et les enchevêtrements de protéine tau.

## Références

```{bibliography}
:filter: docname in docnames
```

## Exercices

Les exercices marqués d'un astérisque (*) sont plus difficiles.

```{admonition} Exercice 1
:class: note
Vrai/faux. Les données de tomographie par émission de positrons sont…
 1. Des données avec une meilleure résolution spatiale que l'IRMf.
 2. Des données qui permettent de mesurer les structures profondes du cerveau, contrairement à l'imagerie optique.
 3. Des données qui, avec le FDG, mesurent la réponse vasculaire à l'activité neuronale, comme l'IRMf.
 4. Des données où une seule coïncidence détectée indique exactement où l'isotope s'est désintégré.
 5. Des données qui reposent sur la détection de paires de photons émis dans des directions opposées.
```

```{admonition} Exercice 2
:class: note
Vrai/faux. Les données de tomographie par émission de positrons sont…
 1. Des données avec une meilleure résolution temporelle que l'imagerie optique.
 2. Des données que l'on peut recueillir aussi souvent que souhaité chez un même participant.
 3. Des données qui peuvent capturer le métabolisme du glucose.
 4. Des données qui peuvent capturer la structure du cerveau.
 5. Des données qui, avec le FDG et une seule injection, permettent de comparer deux conditions de 10 minutes chacune (yeux fermés, puis yeux ouverts), présentées l'une après l'autre pendant une même acquisition de 20 minutes.
```

```{admonition} Exercice 3
:class: note
Choisissez la bonne réponse. Dans un radiotraceur cérébral…
 1. L'isotope détermine la demi-vie.
 2. Le précurseur détermine la cible du traceur.
 3. Le radiotraceur dans son ensemble doit pouvoir traverser la barrière hémato-encéphalique.
 4. Réponses 1 et 2.
 5. Réponses 1, 2 et 3.
```

```{admonition} Exercice 4
:class: note
On effectue une imagerie TEP des plaques de bêta-amyloïde chez un patient jeune en santé, et l'on observe un dépôt substantiel dans la matière blanche. Proposez deux explications à cette observation.
```

```{admonition} Exercice 5
:class: note
On souhaite mesurer le niveau d'activité au repos dans le cerveau d'une personne âgée ainsi que la présence de dépôts de plaques bêta-amyloïdes dans le réseau du mode par défaut, au niveau individuel. L'expérience aura lieu à côté d'un cyclotron. Quelle(s) technique(s) de neuroimagerie utiliseriez-vous, et pourquoi?
```

```{admonition} Exercice 6
:class: note
Pour répondre aux questions de cet exercice, lisez d'abord l'article *Tau pathology in cognitively normal older adults* de Ziontz et collaborateurs (disponible comme [prépublication](https://hdl.handle.net/10.1101%2F611186) sur bioRxiv sous licence CC0 et publié dans le journal Alzheimer's & Dementia: Diagnosis, Assessment & Disease Monitoring, [lien](https://hdl.handle.net/10.1016%2Fj.dadm.2019.07.007)). Les questions suivantes requièrent des réponses à développement court.
- Quelle technique de neuroimagerie est utilisée? S'agit-il d'une technique structurelle ou fonctionnelle?
- Quel type de radiotraceurs est utilisé?
- Quelle normalisation est appliquée aux cartes?
- Quelles régions sont utilisées pour les analyses statistiques?
```

```{admonition} Exercice 7
:class: note
Une équipe veut comparer, chez les mêmes participants, quatre conditions expérimentales: lire des mots, écouter des mots, répéter des mots, et le repos. Elle hésite entre deux traceurs TEP: le [$^{18}$**F**]FDG et l'eau marquée à l'oxygène 15.
 1. Quel traceur choisiriez-vous? Justifiez en vous appuyant sur la demi-vie de chaque isotope.
 2. Quelle contrainte ce choix impose-t-il sur le lieu de l'expérience?
```

```{admonition} Exercice 8*
:class: note
Un participant reçoit une injection de FDG au repos, les yeux fermés. Trente-cinq minutes après l'injection, juste avant le début de l'acquisition, on lui demande d'ouvrir les yeux et de regarder un damier qui clignote, pendant toute l'acquisition (20 minutes).
 1. Comparé à un participant resté les yeux fermés du début à la fin, s'attend-on à observer une augmentation du signal dans le cortex visuel (à l'arrière du cerveau)? Justifiez.
 2. Le même protocole, réalisé avec de l'eau marquée à l'oxygène 15 injectée au moment où le participant ouvre les yeux, poserait-il le même problème? Justifiez.
```

```{admonition} Exercice 9
:class: note
Choisissez la bonne réponse. Un hôpital n'a pas de cyclotron: les radiotraceurs sont produits dans un centre situé à deux heures de route. Aidez-vous du {ref}`tableau d'isotopes <isotopes-table>`. Quelles études TEP cet hôpital peut-il réaliser?
 1. Une étude du métabolisme du glucose au [$^{18}$**F**]FDG.
 2. Une étude des plaques amyloïdes au [$^{11}$**C**]PIB.
 3. Une étude d'activation à l'eau marquée à l'oxygène 15.
 4. Une étude des plaques amyloïdes au [$^{18}$**F**]florbétapir.
 5. Réponses 1 et 4.
```

```{admonition} Exercice 10
:class: note
On mesure les plaques amyloïdes en TEP, en normalisant les cartes par la matière grise du cervelet (la structure située à l'arrière du cerveau, sous les lobes occipitaux). On étudie une forme génétique rare de la maladie d'Alzheimer, dans laquelle des plaques se forment aussi dans le cervelet. Quel effet cela aura-t-il sur les valeurs de SUVR dans le cortex de ces patients? Quelle conséquence pour l'interprétation?
```

## Contributeurs

🤔 Contenu | 💻 Code | 🧩 Quizz | 👀 révision du texte
::::{grid}
:::{grid-item}
![Lune Bellec](https://avatars.githubusercontent.com/u/1670887?v=4?s=100)
[Lune bellec](https://github.com/lunebellec) 🤔💻🧩👀
:::
:::{grid-item}
![François Lespinasse](https://avatars.githubusercontent.com/u/38385719?v=4?s=100)
[François Lespinasse](https://github.com/sangfrois)
🤔👀
:::

::::
