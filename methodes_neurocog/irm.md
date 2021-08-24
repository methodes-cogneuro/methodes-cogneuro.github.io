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
(irm-chapitre)=
# Imagerie par résonance magnétique

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
    </td>
  </tr>
</table>

```{warning}
Ce chapitre est en cours de développement. Il se peut que l'information soit incomplète, ou sujette à changement.
```

## Objectifs du cours
Ce cours a pour but de vous initier aux principes physiques de l'imagerie par résonance magnétique. Au courant de ce cours, nous allons aborder quatre principes fondamentaux de l'IRM:
 * Les principes de base de la résonance magnétique
 * La relaxation : paramètres T1 et T2
 * La formation d'images
 * Les séquences IRM

## Anatomie d'un IRM
:warning: Insérer images d'IRM de différentes forces

Dans l'image ci-haut, nous pouvons voir différens appareils d'imagerie par résonance magnétique. Nous pouvons remarquer que la taille de l'aimant est proportionnelle à sa force. Les appareils de 1.5T sont utilisés principalement à des fins cliniques alors qu'en recherche, le standard est plutôt de 3T, ce qui est environ 60000 fois plus puissant que le champ magnétique terrestre. 

Mais pourquoi voudrions-nous augmenter la force du champ magnétique ? En augmentant la force du champ magnétique, nous pouvons gagner en résolution spatiale et temporelle. Par contre, augmenter la force du champ magnétique peut également introduire des artefacts !

Dans l'image ci-dessous, nous pouvons observer les trois éléments principaux d'un appareil IRM.

:warning: Insérer image où l'on voit les composantes d'un IRM

 * L'**aimant**: en faisant passer un courant électrique dans un aimant, on génère un champ magnétique !
En général, les système IRM utilisent des aimants supra-conductrices qui permettent de produire des champs magnétiques beaucoup plus forts.

 * Les **bobines de gradient**: permettent de faire varier l'intensité du champ magnétique dans l'espace.
Durant l'acquisition des images, les gradients sont activés puis arrêtés plusieurs fois. Les gradients peuvent être produits dans toutes les directions.  
 
 * L'**antenne radio-fréquence**: permettent 1- d'exciter la matière grâce à des émetteurs et 2- de mesurer la réponse de ces tissus biologiques à l'excitation grâce à des récepteurs.
Les impulsions radio-fréquence générées par l'antenne un faible champs magnétique perpendiculaire au champ magnétique principal généré par l'aimant. Nous en parlons un peu plus en profondeur dans la prochaine section. 
 
```{warning}
:name: irm-mouvement-warning
L'IRM est très sensible aux mouvements de la tête ! Il est possible d'utiliser des coussins ou autres dispositifs pour réduire le mouvement.
```

## Spin magnétique et champ B0
Les protons qui constitue en partie les atomes se comportent comme des petits aimants qui tournent autour de leur propre axe,similairement à une toupie. Cette rotation du moment magnétique est appelé le mouvement de précession et dépend entre autre de la composition du noyau. Ainsi, chaque type de noyau possède une *fréquence de Larmor* caractéristique.

Quelques mots sur le moment magnétique... Si l'on considère qu'un proton agit comme un petit aimant, nous pouvons penser à son moment magnétique comme étant la force de cet aimant. Cette force est traduit sous forme de quantité vectorielle avec une direction et une orientation. Peut-être avez-vous entendu parlé de la règle de la main droite ? Et bien, on peut s'en servir pour trouver la direction du moment magnétique, selon son mouvement de précession. 

```{admonition} Fréquence de Larmor d'un atome d'hydrogène
:class: tip
:name: fréquence-larmor-tip
Un atome d'hydrogène possède une fréquence de Larmor de 42.58 MHz/Tesla. Donc, placé dans un champ magnétique externe de 1T, un atome d'hydrogène tourne 42580000 fois par seconde ! Plus le champ magnétique dans lequel se trouve un proton est fort, plus la vitesse à laquelle tourne son moment magnétique va augmenter. 
```

En produisant un champ magnétique (géant !), l'aimant de l'IRM contribue à aligner le moment magnétique des protons selon le même axe que le champ magnétique principal, appelé B0. Ce champ B0 va des pieds vers la tête. Lorsque nous parlons d'un IRM 1.5T, 3T, 7T, etc., on réfère à la force du champ B0.

```{admonition} Bobine + courant = champ magnétique !
:class: tip
:name: champ-magnétique-tip
En créant un anneau avec du fil électrique et en passant un courant électrique, nous produisons un champ magnétique. Dans la [vidéo](https://www.youtube.com/watch?v=bq6IhapfucE), nous pouvons voir les lignes de champ magnétique se dessiner lorsque le champ magnétique est activé. Les lignes de champ sont droites lorsqu'elles passent par le centre de l'anneau, mais elles se propagent en cercles en s'éloignant du centre de l'anneau. 
Pour obtenir un champ magnétique constant à l'intérieur de l'anneau, nous pouvons épaissir l'anneau de sorte à former un cylindre. C'est le même principe que nous retrouvons dans un appareil IRM !
```

```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/xP9M486fRrY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```

## Résonance magnétique
Nous pouvons penser à la résonance comme un mouvement de balançoire. Si nous poussons la balançoire de manière aléatoire, elle n'arrivera pas à osciller adéquatement. Pour avoir un mouvement de balançoire qui s'amplifie, nous devons pousser la balançoire de manière systématique, au même moment. Nous allons alors **entrer en résonance** avec la balançoire. Nous pouvons donc voir la balançoire comme un phénomène de résonance entre l'objet qui se balance et la personne qui donne une impulsion à cet objet. 

L'IRM exploite ce phénomène de résonance. À l'aide de **l'antenne radio-fréquence (RF)**, nous allons créer de petits champs magnétiques en direction perpendiculaire de B0, c'est-à-dire en direction du champ B1. En produisant une série d'impulsion suivant la fréquence de Larmor de l'hydrogène, les atomes d'hydrogène entrent en résonance et basculent dans la direction perpendiculaire. En arrêtant les impulsions, les atomes d'hydrogène entrent en relaxation, c'est-à-dire que leur moment magnétique va retourner dans la direction initiale B0. Autrement dit, le moment magnétique en direction B1 décroit pour revenir dans la direction B0. Ce phénomène de relaxation est très important puisqu'il nous permet d'en déduire les propriétés des tissus selon leur densité en hydrogène. Tout ça est capté par l'antenne !

Les **bobines de gradient** permettent de faire varier l'amplitude du champ magnétique dans trois direction:
 * Direction z : des pieds vers la tête
 * Direction x : de la gauche vers la droite
 * Direction y : du derrière de la tête vers le nez

---
***Réfléchissez-y !***

Maintenant, comment arrivons-nous à faire une coupe du cerveau ?

Indice: rappelez-vous que la fréquence de Larmor d'une particule dépend également de la force du champ magnétique dans lequel elle se trouve. 

*En changeant la force du champ magnétique dans une direction donnée grâce aux bobines de gradient, nous allons modifier la fréquence de Larmor des atomes d'hydrogène à un endroit précis du gradient. Nous pouvons donc aller exciter grâce aux impulsions radio-fréquence les atomes d'hydrogène à cet endroit spécifique et y mesurer les propriétés des tissus. Le mécanisme de base consiste à faire varier l'amplitude des excitations dans l'espace!*

---

Pour résumer, les **ondes radio-fréquences** sont captés notamment par les atomes d'hydrogène qui entrent alors en état d'excitation. Lorsqu'il n'y a plus d'impulsions RF, les protons se réalignent avec le champ B0 et libèrent l'énergie absorbée. Les **gradients** nous permettent de faire varier le champ magnétique dans l'espace pour obtenir des images.

```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/OAtffIWjzSM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```

## Contrastes T1 et T2
Les contrastes T1 et T2 sont les paramètres principaux acquis durant une séance IRM. Initialement, les spins des protons d'hydrogène sont alignés avec B0. L'application d'impulsions RF fait basculer les spins selon l'axe B1, axe perpendiculaire à B0. Une fois les impulsions RF arrêtées, les spins se réalignent avec le champ B0. Ce réalignement est caractérisé par:

1. La composante selon B0 augmente

> L'augmentation de la composante selon B0 (composante Mz) suit une fonction exponentielle croissante. Le temps caractéristique de cette croissance (la vitesse de croissance) s'appelle le **T1 (relaxation longitudinale)**. Le temps T1 correspond au temps écoulé pour obtenir 63% de la valeur d'équilibre de la contribution du moment magnétique selon l'axe z (M0).

```{admonition} M0
:class: tip
:name: M0-tip
À l'état d'équilibre, la contribution du moment magnétique selon l'axe z est appelée B0. Cette valeur dépend de la densité de protons dans les tissus. Ainsi, d'un voxel à un autre, nous n'obtenons pas nécessairement la même valeur de M0.
```

2. La composante selon B1 diminue

> La diminution de la composante selon B1 (composante Mxy) suit plutôt une fonction exponentielle décroissante. Le temps caractéristique de cette décroissance s'appelle le **T2 (relaxation transverse)**.

:warning: (insérer images des courbes)


<br>**TR et TE**

Temps de répétition (TR): délai entre les excitations des atomes d'hydrogène (entre les impulsions RF).

Temps d'écho (TE): délai entre les impulsions RF et l'acquisition des points de mesure.

<br>Lorsque nous acquièrons des données IRM, nous ne mesurons pas la valeur de Mz à plusieurs temps pour réproduire la courbe. Nous prenons simplement un point de mesure au temps TE. Les différents tissus que nous retrouvons dans le cerveau vont avoir des courbes de croissance différentes. En choississant le TE adéquatement, nous allons obtenir des valeurs T1 différentes pour la matière blanche (++), la matière grise (+) et le liquide céphalo-rachidien (-). 

---
***Réfléchissez-y !***

Pourquoi s'embêter à faire des contrastes T1 et T2 quand l'un semble être l'exact opposé de l'autre ?

Observez  bien les images ci-dessous. Y a-t-il certaines régions du cerveau où l'image T2 n'est pas l'exact opposé de l'image T1 ?

```{code-cell} ipython 3
:tags: ["hide-input", "remove-output"]
#Importer les modules requis et le jeu de données
from nilearn.datasets import fetch_icbm152_2009
from nilearn.plotting import plot_anat

data_mri = fetch_icbm152_2009()

#afficher l'image pondérée en T1
plot_anat(data_mri.t1, title="MRI en contraste T1")
```

```{code-cell} ipython 3
:tags: ["hide-input", "remove-output"]
#afficher l'image pondérée en T2
plot_anat(data_mri.t2, title="MRI en contraste T2")
```

*En T2, nous pouvons entre autre voir une partie gris foncé au niveau des noyaux gris centraux. Ces différences sont liées au fait que ces structures possèdent des compositions chimiques différentes qui vont créer des **déphasages** importants. Le contraste T2 est sensible au déphasage alors que le contraste T1 ne l'ai pas, faisant en sorte que ces contrastes ne sont pas l'exact opposé l'un de l'autre ! Nous reparlerons du déphasage dans la prochaine section.* 

---

Bref, les processus de relaxation en T1 et en T2 ne vont pas capturer les mêmes aspects au niveau des tissus. Grâce aux antennes radio-fréquence, nous pouvons construire les contrastes et les mesurer, ce qui nous permet ultimement de faire des cartes du cerveau !

```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/xzmMqHB0uyM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```

## T2* et séquences d'acquisition
Dans la section précédentes, nous avons vu les contrastes T1 et T2 qui nous permettent d'observer les différents tissus du cerveau (matière grise et matière blanche) et le liquide céphalo-rachidien. Le contraste le plus utilisé pour obtenir des images structurelles est le T1. Dans le [cours sur les cartes cérébrales](https://psy3018.github.io/cartes_cerebrales.html), nous avons vu qu'il existait d'autres types d'IRM. Ces différents types d'IRM vont utiliser des séquences d'acquisition différentes. 

Revenons sur le concept de déphasage précédement introduit. En soumettant les tissus à une même impulsion RF, le moment magnétique des protons s'aligne dans la même direction et leur mouvement de rotation se synchronise (i.e., que les protons sont en phase). Lorsque nous arrêtons les impulsions RF, il va y avoir des différences dans le mouvement de précession des protons. C'est le phénomène de déphasage. Les mouvements de précession des protons sont de plus en plus déphasés au fur et à mesure qu'ils retournent à l'équilibre (i.e., alignés avec B0). La décroissance selon l'axe B1 est donc aussi influencé par ce phénomène de déphasage.

Nous avons vu que le champ magnétique B0 permettait d'homogénéisé le champ magnétique dans le cerveau. Certaines molécules agissent comme des aimants et viennent créer des irrégularités dans le champ magnétique, ce qui va accélérer le déphasage des spins. Lorsque nous observons le T2 en présence d'irrégularités, la composante selon B1 décroit plus rapidement. C'est ce que nous appelons le T2* ou T2 apparent.

:warning: Insérer courbe T2 réel vs T2*

Ces inhomogénéités dans le champ magnétique peuvent entre autre être créées par l'oxyhémoglobine et la déoxyhémoglobine que l'on retrouve dans le sang. Nous allons voir plus en détails comment l'oxyhémoglobine et la déoxyhémoglobine perturbent le champ magnétique dans le chapitre sur l'[IRM fonctionnelle](https://psy3018.github.io/irm_fonctionnelle.html). En IRM fonctionnelle, nous utilisons des séquences pondérées en T2*.

**Formation d'images en IRMf**

Nous pouvons observer deux principales différences entre l'image pondérée en T2* et l'image pondérée en T1:
 1. L'image pondérée en T2* est inversé par rapport à l'image en T1. 
 2. L'image pondérée en T2* est plus floue que l'image pondérée en T1 puisque les voxels sont plus gros.
 3. Le temps d'acquisition des images T2* est beaucoup plus court (1-2s) que celui des images T1 (10min).

Quelle est l'utilité d'acquérir des voxels plus gros si ne nous pouvons pas voir correctement l'anatomie du cerveau ? En fait, ce qui nous intéresse en IRMf c'est plutôt les changements d'oxygénation locaux, i.e., les inhomogénéités dans le champ magnétique créés par le ratio d'oxyhémoglobine et de déoxyhémoglobine.

```{code-cell} ipython 3
:tags: ["hide-input", "remove-output"]
#Importer les modules requis et le jeu de données
from nilearn.plotting import plot_img
from nilearn.image import index_img
from nilearn.datasets import fetch_adhd

adhd = fetch_adhd(n_subjects=1)

#Afficher le premier volume de la série
plot_img(index_img(adhd.func[0], 0),
              bg_img=None,
              black_bg=True,
              title="un volume BOLD")
```

**Formation d'images en IRM de diffusion**

En IRM de diffusion, nous utilisons également un contraste en T2*. Par contre, en IRM de diffusion, nous mesurons les inhomogénéités en alternant la direction des impulsions (ex. en donnant une impulsion selon l'axe xy, puis en donnant une impulsion selon l'axe -xy). En effectuant plusieurs images avec des directions d'excitation différentes, nous pouvons obtenir une idée de la direction de la diffusion de l'eau. Cette opération nous permet au finl de connaître la direction des fibres de matière blanche, car plus une fibre pointe vers une direction donnée, plus la diffusion sera grande dans cette direction. Nous allons revenir sur ce sujet dans le chapitre sur [l'IRM de diffusion](https://psy3018.github.io/irm_diffusion.html)

**Séquences IRM**

Les séquences IRM sont souvent représentés par la figure ci-dessous:

:warning: Insérer figure séquence

Nous pouvons mesurer différentes propriétés magnétiques grâce à l'interaction entre ces différents paramètres. Nous pouvons obtenir un contraste T2* par exemple à partir de différentes séquences. Il est donc possible de modifier les paramètres d'une séquence donnée lorsque nous faisons une acquisition IRM à partir de la console IRM. À partir de la console, nous pouvons aussi modifier d'autres paramètres:
* TE
* TR
* champ de vue (field of view, FOV)
* Nombre de coupes
* Épaisseur des coupes


```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/w9z_AN3df_c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```

### Conclusions et références suggérées
Ce chapitre vous a introduit aux principles physiques de l'IRM. Nous avons vu les différentes composantes d'un appareil IRM, les différents phénomènes magnétiques nous permettant d'acquérir des images, ainsi que quelques paramètres que nous pouvons modifier lors de l'acquisition de données IRM. Lors du prochain chapitre, nous parlerons de morphométrie. 

### Références

```{bibliography}
:filter: docname in docnames
```

## Exercices

### Exercice 1
Classez les temps caractéristiques par ordre croissant, si possible.
 * TE
 * TR
 * T1

### Exercice 2
Vrai ou faux? la force du champ d’un IRM est liée à la taille de l’IRM.

### Exercice 3
a ou b? le spin d’un proton d’hydrogène a…
 * Une fréquence de rotation fixe, c’est la fréquence de Larmor.
 * Une fréquence de rotation variable.

### Exercice 4
Qu’est ce qui produit le bruit dans une acquisition IRM?
 * Le champ B0.
 * La climatisation pour refroidir l’aimant.
 * Les bobines de gradient.
 * L’antenne radio-fréquence.

### Exercice 5
Vrai ou faux? L’aimant de l’IRM consomme beaucoup d’électricité.

### Exercice 6
Vrai ou faux? L’IRM fonctionnelle et l’IRM de diffusion utilisent toutes les deux un contraste T2*.

### Exercice 7
Dans un image anatomique, on voit des ventricules blancs sur fond noir. S’agit-il d’une acquisition pondérée en T1 ou en T2? Expliquez pourquoi.

### Exercice 8
On décide de modifier une séquence IRM pour diminuer l’angle de bascule: les spins basculeront de 70 degrés, au lieu de 90 degrés. Quel sera l’effet sur le TR de cette modification?

### Exercice 9
On effectue une acquisition T1 avec un champ de vue de 210mm x 210mm in-plane, et un résolution in-plane de 1 mm isotrope. Quelle est la taille de la matrice d’acquisition in-plane?

### Exercice 10
On effectue une acquisition IRMf avec une résolution de 3 mm x 3 mm in-plane, une matrice in-plane de taille 64x64, une épaisseur de coupe de 3,4 mm (31 coupes). On a un TR de 2 secondes, et on acquiert 150 volumes.
Quelle est la taille du champ de vue 3D, sachant que les coupes sont acquises dans le plan axial?
Quelle est la durée de l’acquisition?
