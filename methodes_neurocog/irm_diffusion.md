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
(irm-diffusion-chapitre)=
# IRM de diffusion
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/me-pic">
        <img src="https://avatars.githubusercontent.com/u/77584086?v=4?s=100" width="100px;" alt=""/>
        <br /><sub><b>Marie-Eve Picard</b></sub>
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
        <a title="Quizz">⚠️</a>
        <a title="Révision du texte">👀</a>
    </td>
  </tr>
</table>

```{warning}
Ce chapitre est en cours de développement. Il se peut que l'information soit incomplète, ou sujette à changement.
```

## Objectifs du cours

Ce cours a pour but de vous initier aux principes de l'imagerie par résonance magnétique de diffusion (IRMd). Pendant ce cours, nous allons aborder :

   - L'origine du signal
   - Les analyses de tractographie
   - Les croisements de fibres
   - L'utilité de l'IRMd


## Principe physique

L'IRM de diffusion est une modalité de neuroimagerie qui nous permet d'étudier les **fibres de matière blanche**. Nous allons donc pouvoir examiner les connexions entre différentes régions, autant interhémisphériques (i.e., fibres de matière blanche voyageant d'un hémisphère à l'autre), qu'intrahémisphériques (i.e., fibres de matière blanche voyageant au sein d'un même hémisphère).

```{admonition} Corps calleux
Le corps calleux est le plus gros faisceau de matière blanche du cerveau, connectant les régions homologues d'un hémisphère à l'autre. D'ailleurs, seuls les mammifères placentaires possèdent un corps calleux !
```

Le principle physique à la base de l'IRMd est la **diffusion**. En IRM de diffusion, nous nous intéresons à la manière dont l'eau diffuse dans le cerveau. En examinant comment l'eau se diffuse, nous pouvons apprendre des informations sur le milieu de diffusion, dans notre cas, le cerveau ! Plus précisément, l'IRMd nous permet d'en apprendre davantage sur les **propriétés de la microstructure** des fibres de matière blanche.

```{admonition} Une goutte d'encre dans un bocal d'eau...
Pour un exemple concret de diffusion, nous pouvons imaginer ce qui se passe lorsque nous laissons tomber une goutte d'encre dans un bocal d'eau. L'encre va au cours du temps se diffuser dans l'eau colorant l'eau petit à petit, jusqu'à ce qu'elle devienne colorée de manière homogène. Les molécules d'eau et d'encre entre en collision dans des directions aléatoires, selon un processus de marche aléatoire. 
```

Nous allons maintenant introduire deux nouveaux termes: la diffusion **isotropique** et la diffusion **anisotropique**.

> Une diffusion est caractérisée d'**isotropique** lorsqu'elle est la même dans toutes les directions. C'est ce qui se passe lorsque nous laissons tomber une goutte d'encre sur un papier mouchoir.

>  Une diffusion est caractérisée d'**anisotropique** lorsqu'elle n'est pas la même dans toutes les directions, c'est-à-dire qu'elle est plus grande selon une certaine direction. C'est ce qui se passe lorsque nous laissons tomber une goutte d'encre sur du papier journal.

[insérer images diffusion isotropique vs anisotropique]

Les axones des neurones viennent contraindre la diffusion de l'eau, les molécules d'eau ne peuvent donc pas se déplacer librement dans toutes les directions. Alors, en sachant comment diffuse l'eau, nous pouvons déterminer la configuration des axones, similairement aux fibres du papier journal. Le phénomène de diffusion dépend de la structure du tissu !

```{admonition} Que se passe-t-il à l'intérieur et à l'extérieur des fibres de matière blanche ?
À l'intérieur des fibres de matière blanche, la diffusion de l'eau est restreinte par la structure des fibres de matière blanche. La diffusion va donc principalement se faire parallèle à l'orientation des fibres.
À l'extérieur des fibres de matière blanche, l'eau se diffuse dans tous les sens puisqu'elle n'est pas restreinte.
```
L'eau diffuse plus facilement dans la direction parallèle aux fibres. La diffusion est donc anisotrope et le coefficient de diffusion sera alors plus élevé dans cette direction parallèle !

### Acquisition des données d'IRM de diffusion

En IRM de diffusion, nous allons prendre des images selon plusieurs orientations. Ce sont des images pondérées en T2* que nous acquirons en IRMd, simplement car elles sont sensibles à la diffusion de l'eau dans une direction donnée. Pour un voxel donnée, nous allons avoir des mesures selon différentes orientations. Un **tenseur de diffusion** va pouvoir être calculé pour chaque voxel.

## Tenseur de diffusion

Nous pouvons imaginer un tenseur comme un ballon. Un tenseur de diffusion tient compte du **modèle Gaussien** de la diffusion de l'eau dans les fibres de matière blanche. Nous pouvons estimer la forme de notre ballon dans chaque voxel selon les différentes valeurs de diffusion obtenues pour chaque direction d'acquistion. Si la diffusion est plus grande selon une certaine direction, notre ballon ressemblera plutôt à un ballon de rugby. Si la diffusion est semblable dans toutes les directions d'acquisition, nous obtiendrons plutôt un ballon de soccer.

```{admonition} Tenseur de diffusion sous forme mathématique
Une diffusion anisotropique possède un coefficient de diffusion qui est présenté sous la forme d'un [tenseur](https://fr.wikipedia.org/wiki/Tenseur):
    ┌               ┐
    │Dxx   Dxy   Dxz│
D = │Dyx   Dyy   Dyz│
    │Dzx   Dzy   Dzz│
    └               ┘
où x, y et z représente les trois axes perpendiculaires de diffusion.
```

```{admonition} Modèle Gaussien de diffusion de l'eau

```

L'imagerie par tenseurs de diffusion (*diffusion tensor imaging*, DTI) est l'une des premières techniques d'analyse qui a vu le jour en IRM de diffusion. Pour estimer la forme de notre ballon, nous avons besoin d'au moins six directions d'acquisition: xy, xz, yz, -xy, -xz, y-z. C'est en combinant les images dans ces six directions que nous pouvons estimer notre tenseur de diffusion (notre ballon).

```{admonition} Anisotropie fractionnelle (FA)
L'[anisotropie fractionnelle](https://en.wikipedia.org/wiki/Fractional_anisotropy) permet de mesurer le degré d'anisotropie d'un phénomène de diffusion, en prenant des valeurs entre 0 et 1. Une valeur d'anisotropie fractionnelle de 0 indique une diffusion isotropique (ballon de soccer), alors qu'une valeur de 1 indique une diffusion fortement anisotropie (ballon de rugby). À noter que l'anisotropie fractionnelle de l'eau est 0, à moins que la diffusion soit contrainte par une structure. 
```

Nous pouvons aussi mesurer la diffusivité moyenne selon l'équation suivante:

$$\overline{\lambda} = \frac{\lambda_{1}+\lambda_{2}+\lambda_{3}}{3}$$

La diffusivité moyenne nous indique à quel point il y a de la diffusion à l'intérieur d'un voxel. En pratique, la mesure d'anisotropie fractionnelle (FA) est favorisée par rapport à la diffusivité moyenne, puisque la FA nous permet en plus de savoir si la diffusion dans un voxel est principalement dans une direction ou si elle est dans plusieurs directions.

### Cartes de diffusion 

À partir des cartes de FA (i.e., valeur de FA pour chacun de nos voxels), nous allons pouvoir reconstruire les différents faisceaux de matière blanche. Nous pouvons également calculer des statistiques à partes des cartes de FA.
 
## Tractographie

## Croisement de fibres

## Applications

Maintenant que nous avons vu plusieurs principles de l'IRM de diffusion et différentes approches d'analyse, voyons ses applications possibles.

- Maladies neurodégénératives: nous pouvons étudier l'impact du vieillissement et des démences sur l'intégrité de la matière blanche grâce à l'IRM de diffusion.

- Développement du cerveau: nous pouvons étudier le développement de la matière blanche dans les différentes régions du cerveau au cours du développement de l'enfant. En effet, la matière blanche se développe à différents rythmes selon les différentes régions du cerveau.

- Planification de chirurgie: il est important de savoir comment sont organisés les fibres de matière blanche avant une chirurgie, par exemple avant de retirer une tumeur cérébrale pour ne pas endommager les fibres qui ne sont pas touchées par la tumeur.

- Découvertes anatomiques dans la matière blanche: l'IRM de diffusion nous permet d'obtenir des informations supplémentaires à des études de dissection. En IRM de diffusion, les algorithmes utilisés permettent de découvrir des chemins de matière blanche qui ne seraient potentiellement pas visible à l'oeil.

- Comprendre les liens entre les structures et les fonctions du cerveau: nous pouvons examiner les liens structurels entre différentes régions qui sont fonctionnellement reliées.

- Traumatismes crâniens et accidents vasculaires cérébraux: nous qualifions souvent les traumatismes crâniens comme étant une maladie de la matière blanche, puisqu'ils entrainent des altérations de la microstructure de matière blanche. Nous pouvons également observer des altérations de la microstructure suite à des accidents vasculaires cérébraux.

## Références
