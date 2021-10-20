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

## Objectifs
*   Comprendre les principes de base d'un radiotraceur.
*   Comprendre le principe de l'émission de rayons gamma et de la tomographie.
*   Connaître les principaux isotopes.
*   Connaître des exemples des principaux types d'images en TEP pour les neurosciences cognitives: imagerie du métabolisme, des récepteurs, et des protéines pathologiques.

## Radiotraceurs
La conception d'un radiotraceur consiste à fabriquer *radioisotope médical* qui sera lié à un composé non-radioactif nommé *précurseur*. Ces deux composés sur une *cible* connue pour son interaction avec le *précurseur*.<

L'affinité du précurseur d'avec la cible est connue a priori, ce qui nous permet de capturer le métabolisme associé à l'activité neuronale. Par exemple, nous savons que la production de neurotransmetteurs dans la fente synaptique induit une augmentation de la consommation de glucose et d'oxygène {cite:p}`Heeger2002`. Il est donc possible d'utiliser soit l'oxygène ou le glucose comme précurseur afin de mesurer l'activité métabolique impliquée dans le couplage neurovasculaire. Nous verrons plus loin comment l'accumulation d'isotope est détectée par le scanner TEP.  

### Définitions
*   **Radioisotope médical** : Un atome qui suit un processus de désintégration radioactive en *émettant des radiations détectables* en dehors du corps.

*   **Précurseur** : Un composant *non-radioactif* qui contient un segment actif se liant à la cible, et pouvant être facilement fusionné au radioisotope.

*   **Biomarqueur** : La *cible* est un biomarqueur du phénomène qu'on cherche à mesurer. Il peut notamment s'agir d'une molécule endogène (déjà présente dans l'organisme, soit l'oxygène ou le glucose) dont la concentration est altérée en présence d'une pathologie, ou bien d'un type spécifique d'activité cérébrale.

*   **Radiotraceur** : Une molécule marquée *délivrant le radioisotope* jusqu'au *biomarqueur cible*; tout ça *in vivo*. Autrement dit, c'est la combinaison de l'isotope et du précurseur.

### Qualités d'un radiotraceur

*   **Perméabilité à la barrière hémato-encéphalique** : le traceur doit pénétrer les membranes cellulaires neuronales.

*   **Arrimage** ***spécifique*** **et** ***sélectif*** : le traceur doit se fixer sur la bonne cible.

*   **Affinité d'arrimage** : même avec une basse concentration de la cible, le traceur doit pouvoir s'y arrimer.

*   **Rapidité d'arrimage** : la désintégration de l'isotope contraint temporellement le processus d'arrimage. La désintégration doit nécessairement être plus lente que le processus métabolique d'arrimage.

*   **Stabilité métabolique** : le traceur ne doit pas se désagréger avant d'atteindre sa cible. Ici, on ne parle pas de la désintégration de l'isotope, mais plutôt du processus métabolisation du précurseur.

```{admonition} Spécificité et sélectivité de l'arrimage
:class: tip
:name: hardball-tip

```
## Les isotopes et l'émission de positrons

```{admonition} Stabilité des isotopes
:class: tip
:name: hardball-tip

```
Faire un tableau avec les isotopes

## Détection de coincidences et imagerie TEP

## Utilisation de la TEP en neurosciences cognitives

Faire une figure de contraste TEP ici

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
