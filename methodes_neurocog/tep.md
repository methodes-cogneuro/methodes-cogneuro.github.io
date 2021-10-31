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
La conception d'un radiotraceur consiste à fabriquer *radioisotope médical* qui sera lié à un composé non-radioactif nommé *précurseur*. Ces deux composés sur une *cible* connue pour son interaction avec le *précurseur*.

L'affinité du précurseur d'avec la cible est connue a priori, ce qui nous permet de capturer le métabolisme associé à l'activité neuronale. Par exemple, nous savons que la production de neurotransmetteurs dans la fente synaptique induit une augmentation de la consommation de glucose et d'oxygène {cite:p}`Heeger2002`. Il est donc possible d'utiliser soit l'oxygène ou le glucose comme précurseur afin de mesurer l'activité métabolique impliquée dans le couplage neurovasculaire. Nous verrons plus loin comment l'accumulation d'isotopes est détectée par le scanner TEP.  

```{admonition} Mini-glossaire
:class: tip
:name: resolution

*   **Isotope (ou radioisotope)** : Un atome qui suit un processus de désintégration radioactif en émettant des radiations détectables* en dehors du corps.

*   **Précurseur** : Un composant *non-radioactif* qui contient un segment actif se liant à la cible, et pouvant être facilement fusionné au radioisotope.

*   **Biomarqueur** : La *cible* est un biomarqueur du phénomène qu'on cherche à mesurer. Il peut notamment s'agir d'une molécule endogène (déjà présente dans l'organisme, soit l'oxygène ou le glucose) dont la concentration est altérée en présence d'une pathologie, ou bien d'un type spécifique d'activité cérébrale.

*   **Radiotraceur** : Une molécule marquée *délivrant le radioisotope* jusqu'au *biomarqueur cible*; tout ça *in vivo*. Autrement dit, c'est la combinaison de l'isotope et du précurseur.
```

### Qualités d'un radiotraceur

*   **Perméabilité à la barrière hémato-encéphalique** : le traceur doit pénétrer les membranes cellulaires neuronales.

*   **Arrimage** ***spécifique*** **et** ***sélectif*** : le traceur doit se fixer sur la bonne cible.

*   **Affinité d'arrimage** : même avec une basse concentration de la cible, le traceur doit pouvoir s'y arrimer.

*   **Rapidité d'arrimage** : la désintégration de l'isotope contraint temporellement le processus d'arrimage. La désintégration doit nécessairement être plus lente que le processus métabolique d'arrimage.

*   **Stabilité métabolique** : le traceur ne doit pas se désagréger avant d'atteindre sa cible. Ici, on ne parle pas de la désintégration de l'isotope, mais plutôt du processus métabolisation du précurseur.

```{admonition} Spécificité et sélectivité de l'arrimage
:class: tip
:name: tep-spec-sel-tip
On veut que le radiotraceur s'arrime uniquement à la cible pour laquelle il a été conçu. On considère un arrimage sélectif lorsque notre traceur se fixe à une cible d'intérêt bien précise (un type de récepteur précis), et il est non-sélectif lorsque notre traceur se fixe à une cible générique (une famille de récepteurs similaires). La spécificité de l'arrimage réfère à sa capacité à refléter un phénomène fidèlement. Un traceur plus ou moins sélectif peut être spécifique aux récepteurs sérotoninergiques, par exemple. Autrement, un traceur non-spécifique est, en ce sens, un traceur de rien.
```

### Isotopes et radioactivité
Nous avons vu que l'imagerie par TEP était possible grâce à l'accumulation d'isotope radioactif dans l'organisme. Il s'agit maintenant d'illustrer comment cette accumulation peut être mesuré afin de refléter les processus métaboliques associés à l'activité neuronale et la production de protéines tels que les neurotransmetteurs.

Il faut d'abord préciser ce qu'est l'émission de positron, et la procédure adoptée pour la capter et la traduire en images. Pour cela, nous avons besoin de deux pièces d'infrastructure importantes, soient le cyclotron ainsi que le scanner TEP.

En termes grossiers, le cyclotron nous permet de concevoir les isotopes radioactif qui seront injectés au participant, et le scanner TEP nous permet de capter les *produits* de la désintégration d'isotopes dans le corps. Les isotopes sont conçus spécifiquement pour qu'ils se déintègrent dans le corps, c'est-à-dire pour que le noyau atomique soit instable et qu'il soit forcé d'émettre des positrons. Le cyclotron et le scanner TEP sont détaillés dans la section suivante.  

```{admonition} Stabilité des isotopes
:class: tip
:name: hardball-tip
Un isotope radioactif est un noyau atomique stable est constitué d'un nombre de protons et de neutrons spatialement distribués également. Un noyau instable aura soit trop de proton, trop de neutron, ou encore, aura une distribution non-uniforme de ceux-ci. Le cyclotron conçoit des isotopes qui sont instables d'une façon précise. C'est cette instabilité qui force le noyau à rétablir son équilibre en émettant des positron à l'extérieur de celui-ci.
```
### Annihilation de positrons et rayons gamma
Lorsque le positron émis en dehors du noyau rencontre un électron, les deux se désintègrent, ce qui génère deux photons partant en direction diamétralement opposée. Ces photons générés à haute énergie sont appelés *rayons gamma*.

La **période radioactive** du noyau durant laquelle s'opère la désintégration, et donc l'émission de positrons capturé à l'aide rayons gamma, correspond à la **demi-vie** du radiotraceur. Référons nous au tableau d'isotopes pour comprendre de combien de temps nous disposons pour effectuer un scan TEP en fonction du processus métabolique ciblé.

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

L'imagerie TEP utilise un certain nombre d'isotopes bien connus. Certains, comme celui fabriqué à partir de fluor (ou $^{18}$**F**), ont une demi-vie assez longue. Cela nous permet de les produire sur un site spécialisé, puis de les transporter sur le lieu de l'étude. D'autres radioisotopes, comme celui fabriqué à partir d'oxygène (ou ^{15}$**O**) ont une demi-vie très courte. Au niveau logistique, ceci nécessite que le cyclotronse trouve à proximité du site ou l'expérimentation se déroule, car le radiotraceur doit immédiatement être utilisé après sa production.

```

## Génération d'images en TEP
Nous avons couvert les principes physiologiques et physiques nous permettant de traduire l'activité métabolique du cerveau en image. Maintenant, il s'agit de préciser comment cette traduction est opérée.

### Cyclotron
Comme nous l'avons vu, le cyclotron nous permet de fabriquer des noyaux atomiques instables de façon contrôlée. En bref, si la tension est trop forte dans la structure atomique, différents mécanismes de désintégration peuvent se produire afin que le noyau se stabilise. Un de ces mécanismes est exploité dans l'imagerie TEP, soit la désintégration Béta+. Cette désintégration correspond à la transformation d'un proton en un neutron ayant pour effet l'émission d'un positron. En d'autres mots, un positron est éjecté de la structure atomique pour que le noyau retrouve sa stabilité. Nous avons vu cette désintgration ${\beta^+}$ se réalise dans un cadre temporel précis (et relativement court), et qu'elle se mesure par les rayons gamma qui traversent les tissus et sortent de la boîte crânienne dans des directions diamétralement opposées. C'est le processus de captation et la modélisation 3D de ces rayons gamma issus de la désintégration qu'on nomme tomographie.

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
