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
(regression-chapitre)=
# Régression linéaire
<table>
  <tr>
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

On va parler du modèle de régression dans le contexte de l’IRM fonctionnelle, ainsi que pour générer des cartes statistiques individuelles et de groupe sur l’activité cérébrale. Les statistiques de groupe permettent de combiner l’activation de plusieurs individus et ainsi de contraster des groupes (ex. groupe de personnes jeunes et groupe de personnes âgées).


Nous allons l’appliquer à l’IRMf aujourd’hui car c’est la modalité où on va avoir les modèles les plus complexes puisqu’on va devoir faire un modèle individuel et un modèle de groupe, mais la mécanique de ce qui sera vu dans ce cours s’applique à la plupart des modalités de façon plus ou moins identique. 

Les objectifs du cours sont les suivants : 
On va détailler les étapes de génération d’une carte paramétrique cérébrale : 
 * Carte IRMf : fonction de réponse hémodynamique, dessin expérimental 
 * Régression linéaire sur des séries temporelles, contraste individuel
 * Régression linéaire sur des paramètres d’activation, contraste de groupe

## Dessin expérimental, contraste

## Modéle linéaire et cartes statistiques individuelles
```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/WIvMt3r7AVU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```

## Cartes statistiques de groupe
```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/mQtO_RwUIaE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```
