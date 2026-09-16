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
L'idée de base de la TEP est d'injecter un produit radioactif, appelé radiotraceur, qui va s'accumuler dans une partie bien définie du cerveau, comme par exemple les [récepteurs dopaminergiques](https://fr.wikipedia.org/wiki/Récepteur_dopaminergique) de type D2. On réalise une image des parties du cerveau qui émettent de la radioactivité, et cela nous permet de quantifier la concentration de la cible du radiotraceur, soit par exemple la présence de récepteurs D2. Le radiotraceur est composé de deux parties: un *radioisotope médical*, qui est un atome radioactif, qui est lié à un composé non-radioactif nommé *précurseur* (ou [*ligand*](https://fr.wikipedia.org/wiki/Ligand_(chimie))), qui va s'accrocher ou s'accumuler dans une *cible* (comme les récepteurs D2). Le *précurseur* est sélectionné pour son affinité avec la *cible*, et représente un choix clé de la conception d'un radiotraceur, et nous permet de capturer une caractéristique particulière du cerveau. Nous verrons dans la prochaine section comment l'accumulation d'isotopes est détectée par le scanner TEP. Nous allons discuté maintenant plus en détails des différents radioisotopes, précurseurs, et ce qui fait un bon radiotraceur.  

```{admonition} Mini-glossaire
:class: tip
:name: glossaire-tep

*   **Isotope (ou radioisotope)** : Un atome qui suit un processus de désintégration radioactif en émettant des radiations détectables* en dehors du corps.

*   **Précurseur (ou ligand)** : Un composant *non-radioactif* qui contient un segment actif se liant à la cible, et pouvant être facilement fusionné au radioisotope.

*   **cible (ou biomarqueur)** : La *cible* est un biomarqueur du phénomène qu'on cherche à mesurer.

*   **Radiotraceur (ou radioligand)** : Une molécule marquée *délivrant le radioisotope* jusqu'au *biomarqueur cible*; tout ça *in vivo*. Autrement dit, c'est la combinaison de l'isotope et du précurseur.
```

### Isotopes et radioactivité
```{figure} tep/isotope.png
---
width: 800px
name: isotope-fig
---
Un isotope radioactif est un atome dont le ratio entre le nombre de protons et de neutrons est instable (**a**). Cette structure instable amène à l'émission d'un positron, qui s'annihile en percutant un électron, ce qui produit l'émission de rayons gamma opposés (**b**). Les rayons gamma sont des photons à très haute énergie, qui peuvent traverser les tissus biologiques, mais sont arrêtés par le plomb (**c**). Image **a** par et **b** adaptés d'une image de [OSweetNature](https://www.shutterstock.com/g/OSweetNature) disponible sur [shutterstock](https://www.shutterstock.com/image-vector/beta-decay-nuclear-energy-diagram-showing-1509181103) ID `1509181103`, utilisée sous licence shutterstock standard. Image **c** par [OSweetNature](https://www.shutterstock.com/g/OSweetNature) disponible sur [shutterstock](https://www.shutterstock.com/image-vector/types-radiation-penetrating-power-through-paper-1169023357) ID `1169023357`, utilisée sous licence shutterstock standard.
```

L'imagerie par TEP était possible grâce à l'accumulation d'isotopes radioactifs dans l'organisme, qui sont détectés par l'appareil TEP et permettent de construire une image. Mais comment cette accumulation peut-elle être mesuré? Les isotopes sont conçus spécifiquement pour qu'ils se désintègrent dans le corps, c'est-à-dire pour que le noyau atomique soit instable. Un isotope stable a un noyau constitué d'un nombre de protons et de neutrons équilibrées. Un noyau instable aura soit trop de protons, soit trop de neutrons. À un moment, cette structure instable va se stabiliser en émettant un positron et un neutrino électronique. Lorsque le positron émis en dehors du noyau rencontre un électron, les deux se désintègrent, ce qui génère deux photons partant en direction diamétralement opposée. Ces photons à haute énergie sont appelés *rayons gamma*.

Les radioisotopes sont produits dans un cyclotron, et vont commencer à se désintégrer immédiatement. La **demi-vie** du radiotraceur correspond au temps nécessaire pour que la moitié des atomes radioactifs contenus dans le traceur se soient transformés en atomes stables. Chaque désintégration atomique est aléatoire, mais à cause du grand nombre d'atomes contenus dans une dose de radiotraceurs, la demi-vie est un phénomène très stable. L'imagerie TEP utilise un certain nombre d'isotopes bien connus. Certains, comme celui fabriqué à partir de fluor (ou $^{18}$**F**), ont une demi-vie assez longue. Cela nous permet de les produire sur un site spécialisé, puis de les transporter sur le lieu de l'étude. D'autres radioisotopes, comme celui fabriqué à partir d'oxygène (ou $^{15}$**O**) ont une demi-vie très courte. Au niveau logistique, ceci nécessite que le cyclotron se trouve à proximité du site ou l'expérimentation se déroule, car le radiotraceur doit immédiatement être utilisé après sa production. Référons nous au tableau d'isotopes pour comprendre de combien de temps nous disposons pour effectuer un scan TEP en fonction de l'isotope utilisé.

```{admonition} Tableau d'isotopes TEP
:class: tip
:name: isotopes-table
| **Radioisotopes**      | **Demi-vie** |
| ---------------------- | ------------ |
| $^{18}$**F**           | 110 min      |
| $^{11}$**C**           | 20.3 min     |
| $^{13}$**N**           | 9.97 min     |
| $^{15}$**O**           | 2.1 min      |
| $^{89}$**Zr**          | 78.4 h       |
| $^{124}$**I**          | 4.17 j       |
| $^{64}$**Cu**          | 12.8 h       |
| $^{68}$**Ga**          | 67.6 min     |

```
### Précurseurs et biomarqueurs
```{figure} tep/fdg.jpg
---
width: 500px
name: fdg-fig
---
Molécule de Fluorodeoxyglucose. Chaque sphère représente un atome (noir: carbone, rouge: oxygène, blanc: hydrogène, vert: $^{18}$**F**). Image par [StudioMolekuul](https://www.shutterstock.com/g/molekuul) disponible sur [shutterstock](https://www.shutterstock.com/image-illustration/fludeoxyglucose-18f-fluorodeoxyglucose-fdg-cancer-imaging-149603819) ID `149603819`, utilisée sous licence shutterstock standard.
```
Le précurseur peut être une molécule endogène (déjà présente dans l'organisme, soit l'oxygène ou le glucose) dont la concentration est altérée en présence de l'activité cérébrale ou bien d'une pathologie. Le précurseur peut aussi être une molécule qui va s'accrocher à une partie spécifique du cerveau (par exemple les récepteurs d'un certain neurotransmetteur). Une réaction chimique est utilisée pour synthétiser une molécule qui regroupe le radioisotope et le précurseur. Dans l'exemple du FDG, une molécule de glucose standard va perdre un oxygène et un hydrogène, qui vont être remplacés par du $^{18}$**F** synthétisé par un cyclotron, voir {numref}`fdg-fig`. Comme nous le verrons plus tard dans ce chapitre, le glucose va s'accumuler dans les parties du cerveau où les neurones sont les plus actifs. La FDG va ainsi agir comme un biomarqueur de l'activité cérébrale.

### Qualités d'un radiotraceur
Pour être utile en neuroimagerie, un radiotraceur doit posséder les qualités suivantes:
 * **Perméabilité à la barrière hémato-encéphalique** : le traceur injecté dans le sang doit pouvoir se rendre au cerveau.
 * **Spécificité d'arrimage**: le traceur doit se fixer seulement sur la bonne cible.
 * **Affinité d'arrimage** : même avec une basse concentration de la cible, le traceur doit pouvoir s'y arrimer.
 * **Rapidité d'arrimage** : la désintégration de l'isotope contraint temporellement le processus d'arrimage. La désintégration doit nécessairement être plus lente que le processus métabolique d'arrimage.
 * **Stabilité métabolique** : le traceur ne doit pas se désagréger avant d'atteindre sa cible. Ici, on ne parle pas de la désintégration de l'isotope, mais plutôt du processus de métabolisation du précurseur. Par exemple la consommation du glucose par l'organisme, en dehors de l'activité cérébrale.

## Génération d'images en TEP
Nous avons couvert les principes physiologiques et physiques des radiotraceurs. nous permettant de traduire l'activité métabolique du cerveau en image. Maintenant, il s'agit de préciser comment l'activité des radiotraceurs peut être utilisée pour générer une image. Pour cela, nous avons besoin de deux pièces d'infrastructure: le cyclotron et le scanner TEP. Nous aurons aussi besoin de méthodes d'analyses d'image.

### Cyclotron
```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/6BxyqFK2KRI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```

Comme nous l'avons vu, le cyclotron nous permet de fabriquer des noyaux atomiques instables de façon contrôlée. Cette production fait partie du processus de génération d'images TEP, car les radioisotopes sont instables et doivent être préparés dans un temps court avant l'expérience. La vidéo ci dessus présente le fonctionnement d'un cyclotron. Brièvement, un cyclotron est un accélérateur de particules compact, qui permet de bombarder des molécules avec des protons à haute énergie pour générer des isotopes radioactifs.

```{figure} tep/radiochemistry.jpg
---
width: 600px
name: radiochemistry-fig
---
Module de synthèse radiochimique automatisé. Image par [Bork](https://www.shutterstock.com/g/stratum) disponible sur [shutterstock](https://www.shutterstock.com/image-photo/manipulation-cell-43798612) ID `43798612`, utilisée sous licence shutterstock standard.
```

Une fois l'isotope produit, il peut être nécessaire d'effectuer des réactions chimiques pour fusionner l'isotope avec le précurseur, et synthétiser le radiotraceur. C'est le cas par exemple pour le FDG, où le $^{18}$**F** va être intégré à une molécule de glucose. Comme les réactions chimiques font intervenir des composés radioactifs, cette étape est réalisée dans un laboratoire automatisée qui protège les opérateurs des radiations ({numref}`radiochemistry-fig`).

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
Injecteur plombé permettant de protéger l'opérateur TEP des radiations émises par le radiotraceur. Image par [Jens Maus](https://github.com/jens-maus) tirée de [wikipedia](https://commons.wikimedia.org/wiki/File:PET-schema.png) sous licence [domaine public](https://fr.wikipedia.org/wiki/Domaine_public_(propri%C3%A9t%C3%A9_intellectuelle)).
```
Une fois le radiotraceur injecté et accumulé sur la cible, la radioactivité est émise par les parties du cerveau que l'on souhaite étudier. Pour chaque évènement radiactif, les deux rayons gamma sortent de la boîte crânienne dans des directions diamétralement opposées. Le scanner TEP est muni de capteurs (ou de caméras, car ces capteurs mesurent des photons) disposés en cercle autour de la tête du participant ({numref}`coincidence-fig`). Comme les rayons gamma se déplacent à grande vitesse, ils viennent frapper deux caméras pratiquement au même moment (à quelques nanosecondes près). Cette arrivée simultanée, appelée **coincidence**, est détectée par le scanneur TEP. Il est possible possible de savoir qu'un événement radioactif a eu lieu sur la droite reliant les capteurs, et il est possible de calculer l'activité accumulée au cours du temps selon l'ensemble des droites possibles. Pour le FDG, il existe plusieurs millions d'événements radioactifs par minutes, et on effectue une mesure accumulée sur plusieurs dizaines de minutes. Mais ces mesures, appelées **projections**, ne correspondent pas (encore) à une image du cerveau.

### Tomographie
```{figure} tep/projection.gif
---
width: 800px
name: projection-fig
---
Illustration de la construction de projections multiples d'une image 2D. Image par [Lucas VB](https://commons.wikimedia.org/wiki/User:LucasVB) tirée de [wikipedia](https://commons.wikimedia.org/wiki/File:Radon_transform_sinogram.gif) sous licence [CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.en).
```
La figure {numref}`projection-fig` illustre comment un object 2D peut être convertie en un série de projections. La tomographie est une opération qui consiste à reconstruire une image 3D du cerveau à partir de la combinaison des mesures prises par l'ensemble des caméras. Si l'on disposait de l'ensemble des projections possibles, on pourrait en théorie faire une reconstruction parfaite. En pratique, on est limité par la taille et le nombre des caméras du scaneur TEP. La figure ci dessous illustre une image simplifiée de coupe 2D du cerveau, le processus de projections multiples, et une reconstruction de l'image à partir des projections. Pour un appareil TEP humain, la résolution spatiale est de l'ordre de 4-7 mm.

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
imkwargs = dict(vmin=-0.2, vmax=0.2)
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
Le [$^{18}$**F**]FDG se comporte comme du glucose normal. Nous avons vu que le couplage neurovasculaire permet de suivre l'activité neuronale au travers des changements d'activité métaboliques et vasculaires, notamment l'extraction d'oxygène locale dans l'hémoglobine. Un autre aspect clé du couplage neurovasculaire est l'extraction de glucose dans le sang. Lorsque l'activité neuronale augmente, une plus grande quantité de FDG est extraite, et le [$^{18}$**F**] va s'accumuler dans les cellules gliales. Éventuellement, ce [$^{18}$**F**] va se désintégrer et être nettoyé par l'organisme, mais durant l'examen la radiactivité va refléter le niveau de métabolisme du glucose, et donc l'activité neuronale. L'acquisition d'un scan FDG prend plusieurs dizaines de minutes, et on peut contraster deux conditions (par exemple repos et une tâche visuelle). Il serait aussi possible de mesurer des différences de métabolisation du glucose en fonction de l'âge des participants, ou leur santé cognitive.

```{admonition} Traitement des images PET
:class: tip
:name: traitement-fdg
Les données TEP doivent être prétraitées avant analyses statistiques. Il est courant de normaliser la carte par rapport aux valeurs observées dans une région contrôle, qui ne contient pas de radiotraceur. Certaines corrections peuvent aussi être appliquées sur les images, comme une correction des volumes partiels. Enfin, il est possible de recaler l'image PET sur une IRM structurelle de chaque sujet, pour visualiser la localisation des activations, et aussi appliquer un recalage dans un espace stéréotaxique pour effectuer des analyses statistiques de groupe similaires à l'IRMf.
```
### Imagerie des récepteurs
```{figure} ./tep/receptors-tep.jpeg
---
width: 800px
name: receptors-fig
---
Images de traceurs TEP pour 18 récepteurs et transporteurs de neurotransmetteurs différents, au travers de 9 systèmes de neurotransmetteurs et 1200 participants en santé. Tiré de [Hansen et al. (2021)](https://www.biorxiv.org/content/10.1101/2021.10.28.466336v1) sous licence CC-BY 4.0.
```
Il existe de nombreux types de neurotransmetteurs dans le cerveau, qui joue un rôle clé dans la communication neuronale, au niveau des synapses, et sont associés à des **récepteurs** spécifiques. Certains de ces neurotransmetteurs sont particulièrement impliqués dans certains processus coginitifs, comme la dopamine et les récopmenses. Il est donc utile de comprendre la distribution spatial des récepteurs pour différents neurotransmetteurs. Ce récepteur agit comme biomarqueur, ou alors, comme cible d'arrimage d'un radioisotope et de son précurseur. Des ligands ont été conçus spécifiquement pour des récepteurs spécifiques, par exepmle les récepteurs dopaminergiques de type D2 et D3.

### Radioligands pour les plaques Béta amyloïde (A${\beta}$)
```{figure} ./tep/pib.jpg
---
width: 500px
name: pib-fig
---
Comparaison d'un scan TEP [$^{11}$**C**] PIB entre un sujet présentant une démence de type Alzheimer et un participant cognitivement sain. Les aires jaunes et rouge suggèrent l'accumulation de plaques A${\beta}$. Image par Klunkwe tirée de [wikipedia](https://commons.wikimedia.org/wiki/File:PiB_PET_Images_AD.jpg) sous licence [CC-BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0).
```
L'amyloïde beta vient d'une protéine précurseur de l'amyloïde (APP). L'amyloïde beta peut s'agréger en plaques, notamment dans la maladie d'Alzheimer. Ces plaques bloquent les communication inter-neurones, puis elles déclenchent une réaction inflammatoire neuro-toxique qui accélère la dégénération des tissues cérébraux et contribuent au déclin des fonctions cognitives. Les plaques A${\beta}$ sont considérées comme un biomarqueur de la maladie d'Alzheimer. Des ligands ont été développés pour s'arrimer aux plaques A${\beta}$ tel que le composé [$^{11}$**C**] PIB. Précisons, cependant, que les plaques peuvent être présentes sans les symptômes cognitifs des troubles neurodégénératifs.

## Conclusion et résumé

*   Un radiotraceur est composé d'un précurseur, qui s'accroche à une cible, puis un isotope, qui se désintègre en émettant des rayons gamma.
*   En enregistrant les coincidences d'arrivée de photons, on peut reconstruire une représentation 3D de la concentration du radiotraceur à l'aide d'une opération dite de Tomographie
*   La FDG TEP est utilisée pour étudier le métabolisme du glucose. La métabolisation du glucose nous indique la consommation d'énergie relative des différentes régions cérébrale. Ceci nous permet d'effectuer des contraste de consommation de glucose entre conditions expérimentales.
*   On peut imager la densité des récepteurs de différents neurotransmetteurs, par exemple, ceux de la dopamine.
*   Des radioligands ont été conçus spécifiquement pour imager la densité des plaques A${\beta}$.

## Références

```{bibliography}
:filter: docname in docnames
```

## Exercices

```{admonition} Exercice 1
:class: note
Les données de tomographie par émission de positrons sont (vrai/faux)
 1. Des données avec une meilleure résolution spatiale que l’IRMf.
 2. Des données avec une résolution spatiale largement supérieure à l’imagerie optique.
 3. Des données qui donnent une image de l’activité neuronale dans tout le cerveau.

```

```{admonition} Exercice 2
:class: note
Les données de tomographie par émission de positrons sont (vrai/faux)
 1. Des données avec une meilleure résolution temporelle que l’imagerie optique.
 2. Des données moins chères à recueillir que l’IRMf.
 3. Des données qui peuvent capturer le métabolisme du glucose.
 4. Des données qui peuvent capturer la structure du cerveau.
```

```{admonition} Exercice 3
:class: note
Choisissez la bonne réponse: Dans un radiotraceur cérébral:
 1. L’isotope détermine la demi-vie.
 2. Le précurseur détermine la cible du traceur.
 3. Le radiotraceur dans son ensemble doit pouvoir traverser la barrière hémato-encéphalique.
 4. Réponses 1 et 2.
 5. Réponses 1, 2 et 3.
```

```{admonition} Exercice 4
:class: note
On effectue une imagerie TEP des plaques de beta amyloide chez un patient jeune en santé, et l’on observe un dépôt substantiel dans la matière blanche. Proposer deux explications à cette observation.
```

```{admonition} Exercice 5
On souhaite mesurer le niveau d’activité au repos dans le cerveau d’une personne âgée ainsi que la présence de dépôt de plaques beta-amyloide dans le réseau du mode par défaut, au niveau individuel. L’expérience aura lieu à côté d’un cyclotron. Quelle(s) technique(s) de neuroimagerie utiliseriez vous, et pourquoi?
```  

```{admonition} Exercice 6
Pour répondre aux questions de cet exercice, lisez d'abord l'article *Tau pathology in cognitively normal older adults* de Ziontz et collaborateurs (disponible comme [preprint](https://doi.org/10.1101/611186 ) sur Biorxiv sous licence CC0 et publié dans le journal Alzheimer's & Dementia: Diagnosis, Assessment & Disease Monitoring [doi](https://doi.org/10.1016/j.dadm.2019.07.007). Les questions suivantes requièrent des réponses à développement court.
- Quelle technique de neuroimagerie est utilisée? S'agit-il d'une technique structurelle ou fonctionnelle?
- Quelle type de radiotraceurs est utilisé?
- Quelle normalisation est appliquée aux cartes?
- Quelles régions sont utilisées pour les analyses statistiques?
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
