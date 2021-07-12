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
(connectivite-chapitre)=
# Connectivité fonctionnelle

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/sangfrois">
        <img src="https://avatars.githubusercontent.com/u/38385719?v=4?s=100" width="100px;" alt=""/>
        <br /><sub><b>François Lespinasse</b></sub>
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
*   Comprendre la définition de la connectivité fonctionnelle.
*   Comprendre la distinction entre activité intrinsèque et évoquée.
*   Comprendre la notion de réseau fonctionnel.
*   Connaître les principaux réseaux au repos.


## Carte de connectivité fonctionnelle
Revenons ce qu'est une carte d'activation IRMf afin de nous donner une compréhension intuitive de ce qu'est une carte connectivité fonctionnelle. Une carte d'activation exploite des fluctuations BOLD évoquées par une tâche, de sorte que nous puissions les associer avec des fluctuations qui changent en fonction d'un paradigme expérimental.

La carte d'activation illustre donc les voxels dont l'activité est plus ou moins reliée à une tâche (ou bloc expérimental) à comparer à l'autre. En d'autres mots, elle indique la corrélation entre l'activité attendue (soit, celle hypothétiquement associée au bloc expérimental) et l'activité mesurée (soit, le signal BOLD-IRMf de tous les voxels).

Ici, il est important de souligner que le signal BOLD peut être exploité par de nombreux modèles statistiques différents, c'est-à-dire que la carte d'activation  d'un seul sujet elle-même est un modèle.

**Exemples:** Nous pourrions décider de mesurer la corrélation entre le décours temporel de chaque voxel et l'intensité avec laquelle un participant presse sur un ou des boutons d'un contrôleur avec son pouce. Nous obtiendrions probablement une carte d'activation montrant des voxels significativement activés au cortex moteur. Nous pourrions aussi mesurer la corrélation entre le décours temporel de chaque voxel et le décours temporel du rythme du coeur. Nous obtiendrions probablement une carte d'activation montrant des voxels significativement activés au niveau des strucutures sous-corticales. Finalement, dans le contexte du cours, notre intérêt serait de mesurer la corrélation entre le décours temporel des voxels d'une région particulière et le reste des voxels. De cette façon, nous obtiendrions une carte de connectivité fonctionnelle montrant avec quelle autre(s) région(s) l'activité BOLD de celle choisie est reliée.
{: .note}

```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/sRL6MyBG_VE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```

## Activité intrinsèque et activité évoquée
La connectivité cérébrale locale (cytoarchitecture) et distribuée (fibres de matière blanche) amènent à l’émergence transitoire d’assemblées neuronales fonctionnelles à différentes échelles spatiales. Différentes techniques existent pour capturer ce phénomène à partir du signal BOLD [@Varela2001].
En général, les modèles de connectivité fonctionnelle tente de répondre à ce que @Varela2001 a nommé le problème d'intégration à grande-échelle. Ceci réfère à l'idée que le système nerveux coordonne un série de procesus distribués hiérarchiquement au travers les différentes régions cérébrales afin de produire un "moment cognitif unifié". Ceux-ci émergent d'une synchronisation de l'activité dans des régions cérébrales distantes, d'où l'intérêt de mesurer la corrélation entre un ensemble de voxels d'avec le reste.

Nous pouvons donc obtenir une carte de connectivité fonctionnelle nonobstant l'activité réalisée par le sujet chez qui nous mesurons le signal BOLD. Celui-ci peut donc être au repos, ce qui signifie qu'on lui instruit de fixer une croix sur l'écran devant lui. Dans ce cas, nous pouvons créer des cartes de connectivité fonctionnelle de l'activité intrinsèque du cerveau. Ou alors, celui-ci peut réaliser une tâche quelconque, et nous tentons de mesurer la corrélation entre la tâche et l'activité d'un ensemble de régions co-activés.

```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/OTWDQgEVOIA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```

## Réseaux fonctionnels
Une méta-analyse effectuée à partir de données TEP identifie un réseau de régions dont l’activité est plus élevée au repos que durant l’exécution d’une série de tâches [@Shulman1997]. Dans un article de revue, @Raichle2001 proposent que ce réseau de régions est engagé de manière systématique dans des processus cognitifs dominant dans l’état de repos, et baptisent ce réseau “mode par défaut”.

@Greicius2002 utilisent la méthodologie introduite par @Biswal1995, en utilisant l’IRMf au repos, et une région cible dans le cortex cingulaire postérieur. Cette analyse identifie un réseau d’activité spontanée au repos très similaire spatialement au réseau du mode par défaut, identifié via les déactivations en TEP.

Une carte de connectivité au repos associé au réseau attentionnel dorsal identifie une corrélation négative avec le réseau du mode par défaut. Cette analyse renforce la notion de transitions spontanées entre un état dirigé vers l’extérieur, et un état introspectif, reflétant la compétition entre deux réseaux distribués [@Fox2005].

@ThomasYeo2011 identifient sept grands réseaux de régions cérébrales dont l’activité spontanée au repos est fortement corrélée. Chaque réseau est illustré via une carte de connectivité pour une région cible choisie, sauf le réseau méso-limbique. Une analyse plus fine par régions cibles permet d’identifier des décompositions en sous-réseaux, ici pour le réseau visuel.

Note pour plus de ressources voir cette [présentation](https://pbellec.github.io/functional_parcellation/#/) et les [notebooks correspondants](https://github.com/pbellec/functional_parcellation).

## Applications
```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/5v4nnQ_FctQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```

### Conclusions et références suggérées
*   La connectivité fonctionnelle consiste à mesurer la cohérence (corrélation) entre l’activité d’une région cible et l’activité du reste du cerveau.

*   La connectivité fonctionnelle peut être observée au repos (activité spontanée), en l’absence de protocole expérimental. En général, on a une superposition de l’activité évoquée vs spontanée.

*   Un réseau fonctionnel est un groupe de régions dont l’activité spontanée prés ente une forte connectivité fonctionnelle. On distingue 7 réseaux principaux, dont le réseau du mode par défaut.

### Références

```{bibliography}
:filter: docname in docnames
```

## Exercices
On commence par des exercices de révisions, qui concernent la vidéo “resting-state network” suivante:
```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/_Iph3WW9UOU?start=18" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```

### Exercice 1
“La septième jour” (sic), extrait en français: 0:54 - 4:35
 1. Qui représente le jeune homme?
 2. À quel résultat fait-il référence?
 3. Qui représente la jeune femme?
 4. À quel résultat fait-elle référence?
 5. Pourquoi appeler ce film “la septième jour” (sic) ?

### Exercice 2
“Neuro-météorologie”: 4:48 - 5:30

```{admonition} Traduction de l’extrait
:class: tip
:name: neuro-meteorologie-tip
Regardons quelle activité intrinsèque nous arrive pour cette fin de semaine.
Comme vous pouvez le voir ici, le mode par défaut et le réseau “tâche-positif” font leurs affaires habituelles, présent / absent, yin et yang. Cela ressemble à l’activité habituelle de rêverie et de concentration intense pour la fin de semaine.
Le mode par défaut semble un peu dominant.
Le visuel sera beau, le moteur sera beau, à moins qu’une fluctuation alcoolique soudaine nous arrive du sud.
L’imagerie satellite nous indique des turbulences dans la région du précunéus qui pourraient devenir très intéressantes en début de semaine.
Mais, comme l’a dit le philosophe latin (Sénèque, NDLR): le repos est loin d’être de tout repos.  
```
1.  De quels réseaux parle-t-on ici?
2.  Pourquoi qualifie-t-il le réseau du mode par défaut et le réseau “tâche-positif” de “Yin and yang”?
3.  Est ce qu’il manque des réseaux dans cette prévision?
4.  Pourquoi est-ce que les turbulences dans le précunéus (ou plutôt le cortex cingulaire postérieur) sont intéressantes?

### Exercice 3
“Hardball”: 8:01 - 9:46
```{admonition} Traduction de l’extrait
:class: tip
:name: hardball-tip
 - Présentateur (Pr): “Bonjour, aujourd’hui nous avons avec nous deux chercheurs distingués, Dr Yann Schnizel et Dr Paul Salami. Prêt à débattre sans compromis?”
 - Paul Salami (PS): “Je souhaite dire que le développement de la littérature sur le mode par défaut et l’état de repos propose de bonnes questions, de bonnes expériences, et cela bénéficie pour l’essentiel aux jeunes qui démarrent la recherche, mais je ne pense pas personnellement qu’étudier le repos est particulièrement utile. Si vous voulez étudier le comportement, vous le faites de la façon traditionnelle, comme nous le faisions avant, vous le faites expérimentalement.”
 - Yann Schnizel (YS): “Ce n’est pas le cas! La distinction importante n’est pas entre repos et tâche, mais plutôt entre activité intrinsèque et évoquée.”
 - PS: “Si nous sommes tous les deux d’accord pour dire que l’activité spontanée est présente dans tous les états cognitifs, je ne vois pas pourquoi nous devrions spécifiquement, je dis bien spécifiquement!, dans un état de repos.”
 - YS: “Nous ne devons certainement pas l’étudier exclusivement au repos, mais l’état de repos est LA condition dans laquelle ces fluctuations spontanées ont été étudiées de la manière la plus détaillée.”
 - PS: “Ceci est fondamentalement non-psychologique!”
 - YS: “Non!”
 - PS: “non-psychologique!”
 - YS: “VOUS êtes fondamentalement non-psychologique!”
 - PS: “au moins j’étudie la cognition durant l’instant où l’événement cognitif se passe.”
 - Pr: “whaou messieurs, les esprits s’échauffent! Calmons nous un peu. Il semble qu’il ne nous reste plus de temps.”
(bataille entre PS et YS)
 - Pr: “La semaine prochaine, dans “cluster analysis”, nous partirons sur la route avec Michael Milham, chanteur folk légendaire. Il voyage de par le monde pour partager l’histoire des réseaux au repos, en chanson. Merci d’avoir regardé cluster analysis sur le réseau du repos,”
```
 1.Est-il vrai que l’activité spontanée est présente aussi bien au repos que durant une tâche?
 2. Est-il vrai que l’activité spontanée a été principalement étudiée dans un état de repos en IRMf?
 3. En quoi est-il “non psychologique” d’étudier une condition de repos?
 4. Question ouverte: est ce que l’un d’entre eux a raison? Ou les deux?

### Exercice 4
Carte de connectivité: vrai/faux
 1. Une carte de connectivité change si on change la région cible.
 2. Pour définir une région cible, on doit faire une carte d’activation.
 3. Une carte de connectivité peut être générée avec un modèle de régression.
 4. Une carte de connectivité fonctionnelle présente des valeurs entre 0 et 1.
 5. Une carte de connectivité en IRMf est un outil pour identifier le réseau du mode par défaut.

### Exercice 5
Activité spontanée et évoquée: vrai/faux
 1. L’activité spontanée du cerveau ne s’observe que dans un état de repos.
 2. L’activité cérébrale évoquée par une tâche peut être caractérisée par une carte d’activation IRMf.
 3. L’activité spontanée du cerveau est plus importante au repos que pendant une tâche visuelle dans certaines parties du cerveau.

### Exercice 6
On souhaite comparer la connectivité fonctionnelle entre des personnes jeunes et âgées.
 1. Citer un facteur de confusion potentiel, qui n’est pas lié à l’activité neuronale intrinsèque.
 2. On souhaite contrôler l'atrophie globale du cerveau dans cette analyse. Décriver brièvement une procédure statistique permettant de tenir compte de cette atrophie dans une comparaison de groupes.
