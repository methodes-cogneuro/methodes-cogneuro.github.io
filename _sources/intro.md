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

# Introduction

Ce texte contient l'ensemble des notes du cours PSY3018 "Méthodes en neurosciences cognitives", donné au baccalauréat en neurosciences cognitives du département de psychologie de l'Université de Montréal. Ce cours présente les principales techniques de neuroimagerie pour étudier la cognition chez l'humain (et l'animal), disposant d'une bonne résolution spatiale:
 * résonance magnétique (anatomique, fonctionnelle, et de diffusion),
 * tomographie par émission de positrons,
 * imagerie optique.

Le principal objectif d’apprentissage pour ce cours est l’acquisition de connaissances théoriques sur les bases physiques et physiologiques de différentes techniques de neuroimagerie, ainsi que les principales techniques de traitement d’image et d’analyse statistique qui leur sont associées. Le cours présentera aussi comment ces techniques de neuroimagerie sont appliquées dans le cadre de projets de recherche en neurosciences cognitives, et chaque chapitre comporte une série d'exercices.

Le cours est donné principalement par Dr Pierre Bellec, avec des contributions par les auxiliaires de recherche, ainsi que de multiples intervenants supplémentaires. Ces notes de cours bénéficie également du retour constructif des étudiants du cours PSY3018 depuis sa création en 2018. Les contributions générales sont présentées ci dessous. Des contributions spécifiques sont listées au sein de chaque chapitre.

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/pbellec">
        <img src="https://avatars.githubusercontent.com/u/1670887?v=4?s=100" width="100px;" alt=""/>
        <br /><sub><b>Pierre bellec</b></sub>
      </a>
      <br />
        <a title="Contenu">🤔</a>
        <a title="Code">💻</a>
        <a title="Quizz">⚠️</a>
        <a title="Révision du texte">👀</a>
    </td>
    <td align="center">
      <a href="https://github.com/eddyfortier">
        <img src="https://avatars.githubusercontent.com/u/72314243?v=4?s=100" width="100px;" alt=""/>
        <br /><sub><b>Eddy Fortier</b></sub>
      </a>
      <br />
        <a title="Contenu">🤔</a>
        <a title="Révision du texte">👀</a>
    </td>
    <td align="center">
      <a href="https://github.com/danjgale">
        <img src="https://avatars.githubusercontent.com/u/14634382?v=4?s=100" width="100px;" alt=""/>
        <br /><sub><b>Dan J Gale</b></sub>
      </a>
      <br />
        <a title="Figure">🎨</a>
    </td>
    <td align="center">
      <a href="https://github.com/SamGuay">
        <img src="https://avatars.githubusercontent.com/u/30598330?v=4?s=100" width="100px;" alt=""/>
        <br /><sub><b>Samuel Guay</b></sub>
      </a>
      <br />
        <a title="Révision du texte">👀</a>
    </td>
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
      <a href="https://github.com/me-pic">
        <img src="https://avatars.githubusercontent.com/u/77584086?v=4?s=100" width="100px;" alt=""/>
        <br /><sub><b>Marie-Eve Picard</b></sub>
      </a>
      <br />
        <a title="Contenu">🤔</a>
        <a title="Révision du texte">👀</a>
    </td>
    <td align="center">
      <a href="https://github.com/anproulx">
        <img src="https://avatars.githubusercontent.com/u/65092948?v=4?s=100" width="100px;" alt=""/>
        <br /><sub><b>Andréanne Proulx</b></sub>
      </a>
      <br />
        <a title="Contenu">🤔</a>
    </td>
  </tr>
</table>

Ces notes de cours sont possibles grâce aux projets suivants:
 * [jupyter book](https://jupyterbook.org) est l'outil utilisé pour générer les notes de cours en utilisant plusieurs formats. Ce projet repose lui-même sur l'outil de documentation [sphynx](https://www.sphinx-doc.org).
 * La librairie [nilearn](https://nilearn.github.io/) en [python](https://www.python.org/) offre tous les outils de visualisation utilisés dans le cours.
 * Les visualisations d'images cérébrales utilisées dans le cours proviennent en partie de jeux de données publiques.
 * Le logo provient du site <a href="https://www.vecteezy.com/free-vector/brain">Brain Vectors by Vecteezy</a>
 * Certaines images du livre ont été obtenues sous droits illimités pour diffusion web et limités pour impression (500k copies) via [shutterstock](https://www.shutterstock.com) par P. Bellec.
