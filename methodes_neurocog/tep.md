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
(tep-chapitre)=
# Tomographie par émission de positrons

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/sangfrois">
        <img src="https://avatars.githubusercontent.com/u/38385719?v=4?s=100" width="100px;" alt=""/>
        <br /><sub><b>François Lespinasse</b></sub>
      </a>
      <br />
        <a title="Contenu">🤔</a>
        <a title="Révision du texte">👀</a>
    </td>
    <td align="center">
      <a href="https://github.com/pbellec">
        <img src="https://avatars.githubusercontent.com/u/1670887?v=4?s=100" width="100px;" alt=""/>
        <br /><sub><b>Pierre bellec</b></sub>
      </a>
      <br />
        <a title="Contenu">🤔</a>
        <a title="Code">💻</a>
        <a title="Exercices">⚠️</a>
        <a title="Révision du texte">👀</a>
    </td>
  </tr>
</table>

## Objectifs du cours
La [tomographie par émission de positrons](https://fr.wikipedia.org/wiki/Tomographie_par_%C3%A9mission_de_positons) est une technique d'imagerie qui permet de cibler de nombreuses caractéristiques du cerveau, aussi bien au niveau structurel que fonctionnel. Couplée avec un radiotraceur de Fluorodésoxyglucose (FDG), la TEP est couramment utilisée pour cartographier l'activité du cerveau au travers de différentes conditions expérimentales. Avec d'autres traceurs, elle permet de cartographier les dépôts de protéines anormales, ou bien encore la présence de différents récepteurs de neurotransmetteurs.

```{figure} tep/tep.jpg
---
width: 600px
name: tep-scanner-fig
---
Scanneur TEP. Image par [Jejecam](https://commons.wikimedia.org/wiki/User:Jejecam) tirée de [wikipedia](https://fr.wikipedia.org/wiki/Tomographie_par_%C3%A9mission_de_positons#/media/Fichier:TEP-CT_2009.jpg) sous licence [CC-BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0).
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
Un radiotraceur est un produit radioactif qui est injecté au participant de recherche (**a**). Les molécules de ce traceur comportent deux parties: un isotope qui émet des rayons radioactifs, et un précurseur qui va s'accrocher à une cible dans le cerveau (**b**). Cette cible peut être par exemple les récepteurs dopaminergiques (**c**). Image **a** par [rumruay](https://www.shutterstock.com/g/rumruay) disponible sur [shutterstock](https://www.shutterstock.com/image-vector/spect-scan-radiologist-single-computed-image-1329727577) ID `1329727577`, utilisée sous licence shutterstock standard. Image **b** par P. Bellec, sous licence [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/). Image **c** par [simurggdesign](https://www.shutterstock.com/g/simurggdesign) disponible sur [shutterstock](https://www.shutterstock.com/image-vector/vector-illustration-synapse-neurotransmitter-diagram-synapses-2050315106) ID `2050315106`, utilisée sous licence shutterstock standard.
```
L'idée de base de la TEP est d'injecter un produit radioactif, appelé radiotraceur, qui va s'accumuler dans une partie bien définie du cerveau, comme par exemple les [récepteurs dopaminergiques](https://fr.wikipedia.org/wiki/Récepteur_dopaminergique) de type D2. On réalise une image des parties du cerveau qui émettent de la radioactivité, et cela nous permet de quantifier la concentration de la cible du radiotraceur, soit par exemple la présence de récepteurs D2. Le radiotraceur est composé de deux parties: un *radioisotope médical*, qui est un atome radioactif, qui est lié à un composé non-radioactif nommé *précurseur* (ou [*ligand*](https://fr.wikipedia.org/wiki/Ligand_(chimie))), qui va s'accrocher ou s'accumuler dans une *cible* (comme les récepteurs D2). Le *précurseur* est sélectionné pour son affinité avec la *cible*, et représente un choix clé de la conception d'un radiotraceur, et nous permet de capturer une caractéristique particulière du cerveau. Nous verrons dans la prochaine section comment l'accumulation d'isotopes est détectée par le scanner TEP. Nous allons discuté maintenant plus en détails des différents radioisotopes, précurseurs, et ce qui fait un bon radiotraceur.  

```{admonition} Mini-glossaire
:class: tip
:name: resolution

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
| **Radioisotopes**       | **Demi-vie** | **$E_{max} ({\beta^+}) $, KeV** |
| ---------------------- | ------------ | ------------------------------- |
| $^{18}$**F**           | 110 min      | 634                             |
| $^{11}$**C**           | 20.3 min     | 961                             |
| $^{13}$**N**           | 9.97 min     | 1190                            |
| $^{15}$**O**           | 2.1 min      | 1732                            |
| $^{89}$**Zr**          | 78.4 h       | 897                             |
| $^{124}$**I**          | 4.17 j       | 2100                            |
| $^{64}$**Cu**          | 12.8 h       | 656                             |
| $^{68}$**Ga**          | 67.6 min     | 1899                            |

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

Une fois l'isotope produit, il peut être nécessaire d'effectuer des réactions chimiques pour fusionner l'isotope avec le précurseur, et synthétiser le radiotraceur. C'est le cas par exemple pour le FDG, où le $^{18}$**F**) va être intégré à une molécule de glucose. Comme les réactions chimiques font intervenir des composés radioactifs, cette étape est réalisée dans un laboratoire automatisée qui protège les opérateurs des radiations.




En bref, si la tension est trop forte dans la structure atomique, différents mécanismes de désintégration peuvent se produire afin que le noyau se stabilise. Un de ces mécanismes est exploité dans l'imagerie TEP, soit la désintégration Béta+. Cette désintégration correspond à la transformation d'un proton en un neutron ayant pour effet l'émission d'un positron. En d'autres mots, un positron est éjecté de la structure atomique pour que le noyau retrouve sa stabilité. Nous avons vu cette désintgration ${\beta^+}$ se réalise dans un cadre temporel précis (et relativement court), et qu'elle se mesure par les rayons gamma qui traversent les tissus et sortent de la boîte crânienne dans des directions diamétralement opposées. C'est le processus de captation et la modélisation 3D de ces rayons gamma issus de la désintégration qu'on nomme tomographie.

### Détection de coincidences
Le scanner TEP est muni de capteurs (ou de caméras, car ces capteurs mesurent des photons) disposés en cercle autour de la tête du participant. Chaque capteur est couplé à un autre du côté opposé du cercle (la distance entre chaque couple de caméra correspond donc exactement au diamètre du cercle). Cette disposition des capteurs permet de détecter l'arrivée simultanée de deux photons. Ce comptage précis de photons est effectué en même temps par cette série de capteurs disposée en cercle.

L'image produite par le scanner TEP est obtenue au travers une projection de la densité de radiotraceurs dans chaque direction, soit chaque couple de caméras. Cette image ne correspond donc pas (encore) à une image du cerveau.

### Tomographie

La tomographie correspond à la combination des mesures prises par l'ensemble des caméras afin de reconstituer une représentation 3D du cerveau. Ce processus correspond à une opération mathématique connue sous le nom de tomographie. On comprend qu'il est nécessaire de disposer d'un nombre important de caméras afin de procéder à une reconstruction précise de l'espace 3D.

## TEP en neurosciences cognitives

Faire une figure de contraste TEP ici avec ces [données](https://openneuro.org/datasets/ds001421/versions/1.2.0)

À ce stade de l'exposé, il s'agit de se demander le genre d'hypothèses que la TEP nous permet de tester. Revenons sur les notions principales :

1.  Nous fabriquons un isotope radioactif (*e.g.* du fluor radioactif) et nous l'injectons au participant.
2.  L'isotope se fixe à un précurseur (*e.g.* du glucose), et cela forme un radiotraceur conçu pour se fixer sur une *cible* précise.
3.  Le participant s'installe dans le scanner, et à partir de ce moment, il est possible de capter la désintégration ${\beta^+}$ du radiotraceur sous forme de rayons gamma
4.  La concentration relative du radiotraceur reconstituée par tomographie nous indique la position des cibles et/où leur densité.

Nous pouvons remarquer que la concentration relative du radiotraceur peuvent dépendre tant de la physiologie de la condition expérimentatale. Supposons que que nous voulons imager la consommation de glucose au repos d'un participant à l'aide du radiotraceur Fluorodésoxyglucose ([$^{18}$**F**]FDG). Nous pourrions effectuer un contraste simple entre deux conditions expériementales. Il serait possible de constater que l'accumulation captée au repos et celle captée pendant la réalisation d'une tâche est différente. Par exemple, le cortex cingulaire postérieur (noyau du réseau du mode par défaut) pourrait consommer plus de glucose au repos. Autrement, si nous nous attardons aux différences physiologiques de nos participants, il serait possible de constater des différences de métabolisation du glucose en fonction de l'âge des participants.

## Méthodes permettant d'étudier les troubles neurodégénératifs
Nous savons que les troubles neurodégénératifs sont associées au dysfonctionnement de différents systèmes de neurotransmission. Les méthodes en TEP sont particulièrement importantes pour l'investigation de ces troubles, car elles permettent notamment de cartographier la densité des récepteurs de ces neurotransmetteurs, ou toutes autres protéines pathologiques connues pour leur implications dans ces troubles.

### Imagerie des récepteurs
Un **récepteur** est une protéine recevant un signal à l'extérieur de la cellule neuronale, c'est-à-dire qu'elle reconnaît et répond à des messagers chimiques endogènes (ou exogènes comme des médicaments). Ce récepteur agit comme biomarqueur, ou alors, comme cible d'arrimage d'un radioisotope et de son précurseur. Dans ce contexte, l'expression **ligand** est préférée pour dénommer la molécule qui s'accroche aux récepteurs d'intérêt puisque ceux-ci ont été développé spécifiquement pour s'arrimer à des récepteurs de systèmes de neurotransmission. Par exemple, des ligands ont été conçus spécifiquement pour les récepteur dopaminergiques tels que D2 et D3. Ces ligands s'associent aux isotopes [$^{11}$**C**] pour former des radioligands.

### Radioligands pour les plaques Béta amyloïde (A${\beta}$)
L'amyloïde beta vient d'une protéine précurseur de l'amyloïde (APP). L'amyloïde beta peut s'agréger en plaques, notamment dans la maladie d'Alzheimer. Ces plaques bloquent les communication inter-neurones, puis elles déclenchent une réaction inflammatoire neuro-toxique qui accélère la dégénération des tissues cérébraux et contribuent au déclin des fonctions cognitives. Les plaques A${\beta}$ sont considérées comme un biomarqueur de la maladie d'Alzheimer. Des ligands ont été développé pour s'arrimer aux plaques A${\beta}$ tel que le composé [$^{11}$**C**] PIB.

Précisons, cependant, que les plaques peuvent être présentes sans les symptômes des troubles neurodégénératifs (*e.g.* ou de démence). La mesure de densité de plaques comme biomarqueur est constestée.

### Tau
Ajoutons nous cette section ?

## Conclusion et résumé

*   Un radiotraceur est composé d'un précurseur, qui s'accroche à une cible, puis un isotope, qui se désintègre en émettant des rayons gamma.
*   En enregistrant les coincidences d'arrivée de photons, on peut reconstruire une représentation 3D de la concentration du radiotraceur à l'aide d'une opération dite de Tomographie
*   La FDG TEP est utilisée pour étudier le métabolisme du glucose. La métabolisation du glucose nous indique la consommation d'énergie relative des différentes régions cérébrale. Ceci nous permet d'effectuer des contraste de consommation de glucose entre conditions expérimentales.
*   On peut imager la densité de récepteur de différents neurotransmetteurs à l'aide de **radioligands**. Par exemple, ceux de la dopamine.
*   Des radioligands ont été conçus spécifiquement pour imager la densité des plaques A${\beta}$.

## Références

```{bibliography}
:filter: docname in docnames
```

## Exercices

1.  Les données de tomographie par émission de positrons sont (vrai/faux)

    a. Des données avec une meilleure résolution spatiale que l’IRMf.

    b. Des données avec une meilleure résolution spatiale que l’imagerie optique.

    c. Des données avec une meilleure résolution temporelle que l’imagerie optique.

    d. Des données moins chères à recueillir que l’IRMf.

    e. Des données qui donnent une image détaillée de l’activité neuronale dans le cortex.

    f. Des données qui peuvent capturer le métabolisme du glucose.

2.  On effectue une imagerie TEP des plaques de beta amyloide chez un patient jeune en santé, et l’on observe un dépôt substantiel dans la matière blanche. Proposer deux explications à cette observation.

3.  On souhaite mesurer le niveau d’activité au repos dans le cerveau d’une personne âgée à l’aide du FDG TEP. Citez un avantage et une limitation de cette technique par rapport à l’IRMf, ainsi qu’une considération éthique pertinente pour ce projet.

4.  Dans un radiotraceur, est-ce l’isotope ou bien le précurseur qui détermine la demi-vie? et en ce qui concerne la stabilité métabolique?

5.  Est ce que la résolution spatiale de la TEP est identique pour tous les scanners?  

6.  Est ce que la TEP est un appareil d’imagerie fonctionnelle, structurelle, ou bien les deux? Pourquoi?

7.  Quel est l’avantage de disposer d’un cyclotron à proximité d’un centre d’imagerie TEP?

8.  Donnez un exemple de projet de recherche qui nécessite absolument d’utiliser la TEP par rapport à une autre technique de neuroimagerie.
