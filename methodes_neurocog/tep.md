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
* Principes physiques et physiologiques de l'imagerie TEP.
* Génération d'images en TEP.
* Principaux types d'images en TEP pour les neurosciences cognitives.

## Principes physiques et physiologiques

### Radiotraceurs
La conception d'un radiotraceur consiste à fabriquer *radioisotope médical* qui sera lié à un composé non-radioactif nommé *précurseur*. Ces deux composés sur une *cible* connue pour son interaction avec le *précurseur*.

L'affinité du précurseur d'avec la cible est connue a priori, ce qui nous permet de capturer le métabolisme associé à l'activité neuronale. Par exemple, nous savons que la production de neurotransmetteurs dans la fente synaptique induit une augmentation de la consommation de glucose et d'oxygène {cite:p}`Heeger2002`. Il est donc possible d'utiliser soit l'oxygène ou le glucose comme précurseur afin de mesurer l'activité métabolique impliquée dans le couplage neurovasculaire. Nous verrons plus loin comment l'accumulation d'isotope est détectée par le scanner TEP.  

```{admonition} Mini-glossaire
:class: tip
:name: resolution

*   **Isotope (ou radioisotope)** : Un atome qui suit un processus de désintégration radioactif en *émettant des radiations détectables* en dehors du corps.

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
Nous avons vu que l'imagerie par TEP était possible grâce à l'accumulation d'isotope radioactif dans l'organisme. Il s'agit maintenant de préciser comment cette accumulation peut refléter les processus métaboliques associés à l'activité neuronale et la production de protéines tels que les neurotransmetteurs.

Il faut d'abord préciser ce qu'est l'émission de positron, et la procédure adoptée pour la capter et la traduire en images. Pour cela, nous avons besoin de deux pièces d'infrastructure importante, soient le cyclotron ainsi que le scanner TEP.

Le cyclotron nous permet de concevoir les isotopes radioactif. Globalement, il nous permet de fabriquer des noyaux atomiques instables de façon contrôlée. En bref, si la tension est trop forte dans la structure atomique, différents mécanismes de désintégration peuvent se produire afin que le noyau se stabilise. Un de ces mécanismes est exploité dans l'imagerie TEP, soit la désintégration Béta+. Cette désintégration correspond à la transformation d'un proton en un neutron ayant pour effet l'émission d'un positron. En d'autres mots, un positron est éjecté de la structure atomique pour que le noyau retrouve sa stabilité.

La TEP  
```{admonition} Stabilité des isotopes
:class: tip
:name: hardball-tip
Un noyau atomique stable est constitué d'un nombre de protons et de neutrons spatialement distribués également. Un noyau instable aura soit trop de proton, trop de neutron, ou encore, aura une distribution non-uniforme de ceux-ci. Le cyclotron conçoit des isotopes qui sont instables d'une façon précise.
```
Faire un tableau avec les isotopes

## Génération d'images en TEP

### Cyclotron

### Détection de coincidences

### Tomographie

## TEP en neurosciences cognitives

Faire une figure de contraste TEP ici avec ces [données](https://openneuro.org/datasets/ds001421/versions/1.2.0)

## Méthodes permettant d'étudier les troubles neurodégénératifs

## Conclusion et résumé

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
