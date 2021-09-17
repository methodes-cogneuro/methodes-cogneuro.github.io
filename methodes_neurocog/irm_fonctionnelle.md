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
(irmf-chapitre)=
# IRM fonctionnelle

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/anproulx">
        <img src="https://avatars.githubusercontent.com/u/65092948?v=4?s=100" width="100px;" alt=""/>
        <br /><sub><b>Andréanne Proulx</b></sub>
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
- Comprendre les bases **physiques** et **physiologiques** du signal BOLD
- Comprendre l'hypothèse du **système linéaire**, invariant dans le temps
- Connaître les principales étapes de **pré-traitement** des données IRMf
- Connaître le principe de génération d'une **carte d'activation**

Ce quatrième chapitre introduit les fondements théoriques de l'IRM fonctionnelle menant à la construction de cartes d'activation, et ultimement à des inférences sur l'organisation fonctionnelle du cerveau. Nous aborderons dans un premier temps les **bases physiques et physiologiques** de cette modalité, qui tout comme pour l'IRM structurelle sont mises à profit afin de capturer certaines propriétés d'intérêt du cerveau. Toutefois, contraitement à l'IRM où ces propriétés se rapportaient à l'anatomie du cerveau (statique), ici, elles se rapportent plutôt au dynamisme de l'activité neuronale réflété par le **signal BOLD**. 

> Pour un rappel, consultez le [Chapitre 3: Analyses morphométriques](https://psy3018.github.io/morphometrie.html)

|               |   `IRM structurelle`     | `IRM fonctionnelle (T2*)`  |
| ------------- |:-------------:| -----:|
| `Objet d'étude`      | **Anatomie, structures et propriétés des tissus** | **Organisation fonctionnelle**|
| `Dimension`     | 1 volume - **3D**   |  Plusieurs volumes dans le temps - **4D** |
| `Durée de l'acquisition` | Plusieurs minutes |  Secondes |

Nous verrons également **l'hypothèse du système linéaire invariant dans le temps** qui sous-tend la modélisation du signal BOLD, et permet de dériver le niveau d'activation en réponse à divers paradigmes expérimentaux. Nous introduirons ensuite les principales étapes de **prétraitement** appliquées aux images d'IRMf, soit le **recalage**, le **lissage spatial** et le **filtrage de facteurs de non-intérêt** qui recoupent partiellement certaines des étapes vues dans le chapitre précédent sur les analyses morphométriques. Tel que nous le verrons, ces étapes sont nécessaires afin d'éliminer le bruit pouvant s'être mêlé au signal BOLD mesuré, qui ne reflète pas le phénomène d'intérêt. Finalement, nous aborderons la construction de **cartes d'activation**, qui, en exploitant des concepts statistiques, permet d'émettre des théories sur l'organisation fonctionnelle du cerveau. 

## IRM fonctionnelle (T2*)
[L'imagerie par résonnance magnétique fonctionnelle](https://fr.wikipedia.org/wiki/Imagerie_par_r%C3%A9sonance_magn%C3%A9tique_fonctionnelle)
est une modalité d'imagerie qui permet de mesurer indirectement l'activité cérébrale. Son objectif consiste à cartographier les fonctions du cerveau ou de manière plus générale, à mettre en évidence l'organisation fonctionnelle du cerveau. Pour ce faire, l'IRMf acquière des images du cerveau en action (dynamique), et ce, souvent en relation avec des manipulations expérimentales, ayant été conçues pour isoler des processus cognitifs spécifiques. Elle s'appuie, comme nous le verrons, sur des séquence spécifiques, qui mène à la détection du **signal BOLD**, permettant d'inférer l'activité neuronale. 

```{figure} irm_fonctionnelle/irmf.jpg
---
width: 600px
name: irmf-fig
---
Les images d'IRMf permettent d'observer l'activation cérébrale, tiré de [wikipedia](https://fr.wikipedia.org/wiki/Imagerie_par_r%C3%A9sonance_magn%C3%A9tique_fonctionnelle#/media/Fichier:Researcher-test.jpg).
```

Les images d'IRMf sont un peu comme un film du cerveau en action. Elles sont composées d'une **série de volumes 3D** qui se succèdent à une fréquence donnée, plutôt que d'un unique volume comme c'était le cas en IRM. Nous parlons alors d'images **4D** , puisqu'il s'ajoute la dimension du temps. Nous pourrions, par exemple, acquérir 1 volume par 2 secondes pendant un total de 6 minutes, ce qui résulterait en une image IRMf composée d'une série de 180 volumes 3D du cerveau. 

\begin{align}
{volume(3D)}+{temps}
\end{align}

```{code-cell} ipython 3
:tags: ["hide-input", "remove-output"]

#importe les librairies nécessaires
import pandas as pd
import nilearn
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from nilearn.input_data import NiftiLabelsMasker
from mpl_toolkits.mplot3d import Axes3D

# Extraire les séries temporelles pour un sujet d'un jeu de données
haxby_dataset = datasets.fetch_haxby()
haxby_func_filename = haxby_dataset.func[0]

# initialiser le masque
brain_masker = NiftiMasker(
    smoothing_fwhm=6,
    detrend=True, standardize=True,
    low_pass=0.1, high_pass=0.01, t_r=2,
    memory='nilearn_cache', memory_level=1, verbose=0)

# appliquer le masque
brain_time_series = brain_masker.fit_transform(haxby_func_filename,
                                               confounds=None)
# fonctions de visualisations pour le voxel 3D
def expand_coordinates(indices):
    x, y, z = indices
    x[1::2, :, :] += 1
    y[:, 1::2, :] += 1
    z[:, :, 1::2] += 1
    return x, y, z

def explode(data):
    shape_arr = np.array(data.shape)
    size = shape_arr[:3]*2 - 1
    exploded = np.zeros(np.concatenate([size, shape_arr[3:]]), dtype=data.dtype)
    exploded[::2, ::2, ::2] = data
    return exploded

# initialisation de la figure
fig = plt.figure(figsize=(10,3))

# visualiser le voxel
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("z")
ax1.grid(False)
colors = np.array([[['#1f77b430']*1]*1]*1)
colors = explode(colors)
filled = explode(np.ones((1, 1, 1)))
x, y, z = expand_coordinates(np.indices(np.array(filled.shape) + 1))

x[1::2, :, :] += 1
y[:, 1::2, :] += 1
z[:, :, 1::2] += 1

ax1.voxels(x, y, z, filled, facecolors=colors, edgecolors='white', shade=False)
plt.title("Voxel (3D)")


# ajouter séries temporelles
# random voxel 
voxel = 1
ax = fig.add_subplot(1, 2, 2)
ax.plot(brain_time_series[:, voxel])
ax.set_title("Décours temporel d'un voxel")

plt.xlabel("Temps(s)", fontsize = 10)
plt.ylabel("Signal BOLD", fontsize= 10)
```

Le volume du cerveau (3D) est formé plusieurs milliers voxels, qui sont de petites unités de volumes (3D) ayant une coordonnée dans l'espace **x, y, z**. En IRMf, pour chaque voxel du cerveau, nous détenons plusieurs points de mesure de l'activité dans le temps, ce qui forme ce que l'on appelle une **série temporelle** ou **décours temporel**. Typiquement, quelques dizaines à centaines de points de mesures décrivent la série temporelle (avec les appareils modernes nous parlons plutôt d'une centaine de points). Ces points de mesures sont séparées par un intervalle de temps, qui peut varier de millisecondes à secondes (avec les appareils modernes on parle plutôt de l'ordre de ms, soit environ 500 ms). Comme nous le verrons plus loin, la série temporelle contient l'information relative aux changements de l'activité neuronale dans le temps. Une grande partie du travail en IRM fonctionnelle consiste à analyser de telles séries temporelles. 

L'IRMf s'est considérablement développé depuis ses débuts dans les années 1990. Aujourd'hui, il s'agit d'une méthode d'imagerie fonctionnelle largement employée par les chercheurs pour étudier les fonctions du cerveau, en raison de ses avantages vis-à-vis des autres modalités. D'une part, l'IRMf est non-invasive et sécuritaire, ce qui permet d'acquérir les données de mêmes sujets à répétition. De plus, comme nous le verrons, elle admet un bon compromis entre résolution temporelle et spatiale.

```{admonition} Résolution spatiale et temporelle
:class: tip
:name: resolution

L'IRM fonctionnelle détient une moins bonne résolution spatiale que l'IRM structurelle. En effet, pour chaque voxel, nous voulons échantillonner l'activité cérébrale (dans les faits, nous échantillons le signal BOLD, que nous verrons plus loin) assez rapidement pour capturer les variations de cette activité en réponse à des manipulations expérimentales. La réponse maximale étant 5-6 secondes après la manipulation, une résolution temporelle de 2 à 3 secondes permet d’étudier adéquatement ces variations. Ces nouvelles considérations temporelles entraînent un compromis avec la résolution spatiale qui tend à diminuer lorsqu'il s'agit de plus courtes durées d'acquisition. La résolution spatiale de l’IRMf est de l’ordre de quelques millimètres (typiquement 2 à 3 $mm^3$). 
```

### Base physiques et physiologiques
#### Couplage neurovasculaire

L'IRMf et les inférences faites sur les fonctions cérébrales reposent sur une superposition d'hypothèses théoriques. L'une de ces hypothèse, d'origine physiologique, est le phénomène du **couplage neurovasculaire**. Ce phénomème est important comme il est exploité pour mesurer indirectement l'activité neuronale, plus précisément, l'activité post-synaptique des neurones. 

L'activité du neurone est assurée par des composés, impliqués dans diverses réactions chimiques, notamment celles menant à la production de neurotransmetteurs dans la fente synaptique. Bien que nous n'entrerons pas dans le détail de ces mécanismes, en réalité beaucoup plus complexes, il faut retenir que l'**activité du neurone** entretient un lien étroit, quantifiable avec une **réponse vasculaire** caractéristique, d'où le terme, couplage neurovasculaire. En effet, lorsqu'activés, les neurones accroîent leur **demande métabolique** en nutriments et en oxygène localement. Cette demande métabolique produit une réponse vasculaire, se caractérisant par **l'augmentation du volume des capillaires** et **l'augmentation du flux sanguin**, qui **augmente l'acheminement en oxygène** (oxyhémoglobine) vers les populations de neurones actives. Ceci entraîne une modification du rapport du taux d'**oxyhémoglobine** (sang oxygéné) et de la **déoxyhémoglobine** (sang déoxygéné) localement, ce qui est dédectable au moyen de l'IRMf par l'entremise du **signal BOLD** (*Blood Oxygenation Level Dependent*). Le premier modèle quantitatif du couplage neurovasculaire (dit “modèle du ballon”) a été proposé par *Buxton et al., MRM 1998*. 

!!ajouter image couplage-neurovasculaire!!

#### Le signal BOLD 

Quelle est l'origine du **signal BOLD**? L'hémoglobine existe sous deux états, soit l'état oxygéné (porteur de l'oxygène) et déoxygéné (non-porteur d'oxygène). La présence de l'oxygène défini les propriétés éléctromagnétiques ou la stabilité moléculaire de l'hémoglobine.

!! image molécules !!

- L'**oxyhémoglobine** est **diamagnétique**
- La **déoxyhémoglobine** est **paramagnétique**

Ceci implique que lorsque soumises à des séquences d'impulsions électromagnétiques, les molécules se comportent de manière caractéristique. La déoxyhémoglobine créer des inhomogénéités du champ magnétique, alors que l'oxyhémoglobine n'a pas d'effet sur ce même champ. Les séquences  $T2$*, qui sont celles employées en IRMf, sont sensibles à de telles inhomogénéités. 

> Pour un rappel sur les notions de relaxation de l'IRM, consultez le [chapitre 2: l'imagerie par résonnance magnétique fonctionnelle](https://psy3018.github.io/irm.html)

La déoxyhémoglobine déforme donc le champ magnétique  $BO$ induit par l'aimant, ce qui fait en sorte que le temps de relaxation  $T2$* est plus rapide. Ceci a pour effet de réduire le signal BOLD là où le sang est sommairement plus déoxygéné, et à l'inverse de l'amplifier là où le sang est plus oxygéné.

|               |   `Déoxyhémoglobine`     | `Oxyhémoglobine`  |
| ------------- |:-------------:| -----:|
|Propriétés électromagnétiques |Diamagnétique| Paramagnétique|
| Impact sur le signal BOLD      | **Réduit** le signal BOLD  | **Augmente** le signal BOLD|
| $T2$*    | Décroît plus **rapidement**   |   Décroît plus **lentement** |
| Effet sur le champ | **Ajout d'inhomogénéités/distorsions** |  **Pas d'inhomogénétités**  |

En résumé, par les propriétés magnétiques de l'hémoglobine oxygéné et déoxygéné, nous pouvons observer les changements du signal BOLD. Ce signal nous informe de la demande métabolique (en oxygène), ce qui permet d'inférer la réponse neuronale à des manipulations, et ce, pour chaque voxel (présupposant un couplage neurovasculaire typique).

```{admonition} Attention!
:class: tip
:name: attention

L'IRMf constitue par ce fait même, une **mesure indirecte** de l'activité neuronale. En effet, cette modalité ne mesure pas directement l'activité des neurones, mais plutôt la demande métabolique (sang oxygéné vs déoxygéné) associée à celle-ci.
```

```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/SWOww_Ensqg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```

## Modèle (ou fonction) de réponse hémodynamique

#### Théorie des systèmes
Un système comprend un ensemble d'éléments qui interagissent selon certains principes ou règles. En présence d'un système, nous pouvons décrire et de formaliser les interactions entre ses éléments au moyen de termes mathématiques. Pourquoi parlons nous de systèmes? Parce que l'activité neuronale et le signal BOLD forme un système. La **fonction de réponse hémodynamique** est la formule qui contient la description ou formalisation de la relation entre les éléments de ce système, soit **l'activité neuronale ($X$)** et **le signal BOLD ($Y$)** .

\begin{align}
X(t) &\quad \text{intrant : activité neuronale}\\
Y(t) &\quad \text{sortie : réponse hémodynamique}\\
\end{align}

La fonction de réponse hémodynamique, et ses propriétés mathématiques, constituent une autre hypothèses importante pour les aspects de modélisation en IRMf. Essentiellement, la fonction ce modèle sous-tend les inférences que l'on fait sur l'organisation fonctionnelle du cerveau: nous l'employons dans le but d'estimer la réponse à une tâche ou condition donnée. 

#### Propriétés mathématiques 
La figure qui suit montre la réponse hémodynamique attendue suite à un pic d'activation au temps 0. Bien que simplifiée, elle permet de visualiser la fonction largement admis, décrivant relation maintenue entre l'activité neuronale (rouge) et le signal BOLD (bleu), en fonction du temps. 

```{code-cell} ipython 3
:tags: ["hide-input", "remove-output"]

# importer les librairies
import numpy as np
from nipy.modalities.fmri import hrf, utils
import matplotlib.pyplot as plt

# visualiser la fonction hémodynamique
fig_BOLD = plt.plot
hrf_func = utils.lambdify_t(hrf.glover(utils.T))
t = np.linspace(0,25,200)
plt.plot(t, hrf_func(t))
a=plt.gca()
a.set_xlabel('t(s)')
a.set_ylabel('% Signal BOLD')
plt.axvline(x=0, marker = "o", color = "r")
plt.title("La fonction de réponse hémodynamique")
```
Dans la figure ci-haut, l'axe des $X$ représente le temps, et l'axe de $Y$, le **%** du changement du signal BOLD. La ligne verticale rouge indique le pic d'activation neuronale. La courbe bleue, pour sa part, illustre le % du changement du signal BOLD attendu suivant l'activation neuronale. Ci-dessous sont décrit les caractéristiques importantes de la fonction de réponse hémodynamique. 

- **Résolution temporelle**: Réponse lente, durée entre **15 à 20 secondes** suivant le stimulus
- **Temps avant l'atteinte de l'amplitude maximale** :Atteint l'amplitude maximale après **4 à 6 secondes** 
- **Creux post-stimulation (*Undershoot* en anglais)** : Décroît à partir de l'amplitude maximale jusqu'à se retrouver sous le seuil de base
- **Retour au seuil** : La fonction retrouve le niveau de base après environ **15 à 20** secondes
- **Amplitude maximale** : L'ordre du changement relatif du signal BOLD atteint environ **5%** pour des stimulations d'ordre sensorielle, alors qu'elle est plutôt de **0,1 à 0,5%** pour d'autres paradigmes cognitifs

```{admonition} Attention!
:class: tip
:name: adéquation du modèle-tip

Le modèle de réponse hémodynamique peut s'avérer être une hypothèse invalide pour certaines populations, notamment si le couplage neurovasculaire est déréglé. C'est le cas de populations qui ont une vascularisation atypique, par exemple, chez les personnes âgées ou chez les individus ayant des maladies cardiovasculaires. 
```

La fonction de réponse hémodynamique présentée ci-haut se rapporte à un contexte expérimentale bien simple : une simple stimulation courte isolée. En réalité, les **paradigmes expérimentaux sont beaucoup plus complexes** : ils alternent à maintes reprises entre différentes conditions expérimentales/stimuli (par blocs, aléatoirement ou dans un ordre précis). De plus, ils comportent souvent plus d'une stimulation rapprochée dans le temps, ou/et des stimuli qui se prolongent sur plusieurs millisecondes ou secondes. Qu'advient-il alors de la fonction de réponse hémodynamique? Peut-on toujours modéliser la réponse hémodynamique en tant que système, c'est-à-dire définies par des règles mathématiques? Si oui, que deviennent les propriétés de ce système?

```{admonition} Linéarité
:class: tip
:name: linéarité-tip

- Le système est **additif**. Autrement dit, la réponse à plusieurs impulsions rapprochées (ou réponse longue) correspond à la somme des réponses à ces impulsions prises indépendamment.
- La réponse neurale **mise à l'échelle** selon le facteur **a**, change également l'échelle de la réponse BOLD selon ce même facteur. Ceci implique que lorsque l'amplitude de la réponse neuronale est le double, la réponse BOLD est également double.```

!! Figure linéarité !!
```
```{admonition} Invariance au temps
:class: tip
:name: invariance-tip

- Si le stimulus est décalé de $t$ secondes, la réponse BOLD est aussi décalé de $t$ secondes.

!! Figure invariance dans le temps !!
 ```

Combinant l'ensemble de ces propriétés, nous obtenons un système relativement simple à caractériser : nous pouvons alors inférer les réponses à des stimuli complexes, ayant pour connaissance de la réponse aux stimuli court, pris indépendamment.

Comment les propriétés du système ont-elles été vérifiées? Une première étude conduite par **Logothetis et al. Nature Neuroscience (2001)** s'est intéressée à cette question, c'est-à-dire au comportement d'un système opérant dans le cadre de paradigme expérimentaux plus complexes (ici variant la durée des stimulations). Plus précisément, elle visait à tester empiriquement l'hypothèse postulant la linéarité de ce système, c'est-à-dire décrivant une relation linéaire entre activité neuronale ($X$) et BOLD ($Y$). Dans l'étude, les auteurs ont mis en place un protocole ingénieux permettant de mesurer simultanément de l'activité LFP (**activité neuronale**) en électrophysiologie et le signal **BOLD** dans le cortex visuel du singe. Ils ont fait varier les durées d'exposition à une stimulation: les singes étaient soumis à des stimulations visuelles de 3, 6, 12 et 24 secondes (de gauche à droite et de haut en bas sur la figure). Vous trouvez ci-bas la figure des résultats de cette étude qui permet de comparer l'activité LFP et la réponse BOLD mesurées.

!! Figure résultats logothetis !!

```{figure} .PLACEHOLDER.png
---
width: 600px
name: résultats-logothetis-fig
---
L'aire bleue correspond aux LFP (activité neuronale), la courbe rouge est le signal BOLD qui est mesuré, et la courbe grise est le signal BOLD prédit par la convolution des LFP avec une fonction de réponse hémodynamique supposant un système linéaire. Le premier trait vertical représente le début de la stimulation et le second, la fin de cette stimulation. À partir des résultats, nous observons que la réponse BOLD est fonction de la durée de la stimulation. Globalement, une réponse hémodynamique plus importante (plus grande amplitude) est observée pour des stimuli qui s'étalent sur une plus longue durée.
```
Et alors, que peut-on retirer de ces résultats? Lorsque nous regardons la figure des résultats de l'étude par *Logothetis et al. (2001)* nous observons une superposition des deux courbes **signal BOLD mesuré** (rouge) et **signal BOLD prédit** (gris). Ceci nous indique l'adéquation de l'hypothèse linéaire comme décrivant ce système, et ce, même pour des paradigmes expérimentaux augmentant en complexité! 

```{admonition} Attention!
:class: tip
:name: attention
Attention! Un découplage de la réponse BOLD mesurée-prédite est observable vers la fin d'une stimulation très longue (cadrant du bas à droite), ce qui est suppose que l'hypothèse linéaire est moins bien adaptée pour de très longues stimulations.
```
Pour résumer, l'étude par Logothetis et al. (2001) est le premier protocole ayant permis de valider empiriquement l'hypothèse du système linéaire. Aujourd'hui, cette hypothèse a été validée à plus d'une reprise dans divers paradigmes expérimentaux. La connaissance des propriétés du modèle de réponse hémodynamique rend possible la modélisation du signal BOLD, non seulement pour des stimuli simples courts et isolés, mais également pour divers paradigmes expérimentaux complexes, qui sont beaucoup plus proche de la réalité pratique expérimentale.   

```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/91JVOAwOOyE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```

### Prétraitement des données d'IRMf
Nous avons abordé dans les sections précédentes divers aspects de la modélisation de la réponse hémodynamique. Un autre point important en IRMf est la modélisation du bruit et des sources de variations qui peuvent être présentes dans les séries temporelles. Différents **facteurs confondants** ou **artéfacts** (provenant du scanner IRM ou du sujet scanné lui-même) peuvent induire des fluctuations substantielles dans le signal BOLD mesuré, et venir confondre les inférences faites sur l'activité neuronale en réponse à des tâches. 

Quelques exemples d'**artéfacts**:

- Fréquence cardiaque
- Mouvement du sujet lors de l'acquisition
- Décharge électrique du scanner 
- Inhomogénéités dans le champ magnétique aux intersections air-tissu

À l'issue des acquisitions, les images d'IRM fonctionnelle brutes contiennent une composition de ces artéfacts (erreurs), qui se superposent à l'image. Les images d'IRMf doivent, donc, en amont des analyses statistiques être soumises à des corrections. Pour se faire, différentes stratégies de modélisation peuvent être employées pour régresser de tels facteurs du signal. Dans cette section, nous présentons un aperçu de trois grandes étapes de prétraitement en IRMf, qui, typiquement sont appliquées séquentiellement (c.-à.d. à travers l'utilisation d'un pipeline).

- `Le recalage`

- `Le filtrage de facteurs de non-intérêts`

- `Lissage spatiale`

```{admonition} Qu'est-ce qu'une image?
:class: tip
:name: image-tip

Une image est une **matrice de nombres**, qui contient des valeurs en chaque point de l'espace quantifiant une propriété donnée qui nous intéresse. Par exemple, si on prend le cas d'une photo, à chaque point de l'espace, c'est-à-dire pixel, nous avons trois valeurs qui quantifie la valeur du rouge, du vert et du bleu associée à cette localisation spatiale tout précisément. De manière analogue, l'image en IRM fonctionnelle est une matrice de nombres qui contient des valeurs en chaque points de l'espace, mais cette fois-ci décrivant l'activité BOLD. Plutôt que parler de pixels (2D), nous parlons de voxels (3D). Le prétraitement d'images sous-entend généralement que nous effectuons des opérations ou transformations mathématiques sur de telles matrices de nombre.
```
#### Recalage

Le recalage consiste à aligner une image à une image de référence. C'est une étape de prétraitement complétée avant les analyses statistiques, comme celles-ci présupposent qu'il y a une correspondance entre les voxels de différentes images. Le recalage s'assure qu'un voxel maintient de mêmes coordonnées à travers les images d'un même individu (analyses individuelles) ou/et à travers les images de différents individus (analyses de groupe). Plusieurs notions de cette section font un rappel de ce qui a été vu dans le cours sur les analyses morphométriques. 

> Pour un rappel, consultez le [Chapitre 3: Analyses morphométriques](https://psy3018.github.io/morphometrie.html)

Le recalage comprend **deux** étapes : 

`1. Estimation des paramètres de transformation`: Ils spécifient comment bouger l'image pour l'aligner à la référence. Ces paramètres peuvent être linéaires et/ou non-linéaire dépendamment du type de recalage. 

`2. Ré-échantillonnage`: Le ré-échantillonnage consiste à appliquer les paramètres de transformation à l'image. Les coordonnées orginales sont transformées dans un nouvel espace, et la nouvelle image est créée à partir des coordonnées transformées.

Le recalage fait appel à **deux** catégories de transformation: 

- **Transformation linéaires** : Les transformation linéaires appliquent des opérations/fonctions linéaires sur les coordonnées des voxels de l'image (p.e. translation, rotation, mise à l'échelle), leur assignant une nouvelle localisation. Elles transforment chaque voxels de l'image de manière équivalente : les structures changent d'emplacement, mais conserve leur forme.

- **Transformation non-linéaires**: Les transformations non-linéaires comprennent des opérations/fonctions ayant un degré de complexité plus grand (p.e. fonction polynomiale, cosine) avec davantage de paramètres. Elles offrent une plus de flexibilité dans la transformation des voxels de l'image, dans la mesure où elles peuvent transformer certains voxels de l'images plus drastiquement que d'autres. Ceci permet de changer la forme des structures du cerveau.

Nous verrons dans la section suivante, trois types de recalage possible en IRM fonctionnelle.
           
- `Un recalage intra-sujet (mouvement)`
- `Un recalage inter-modalité (BOLD-T1)`
- `Un recalage inter-sujet (stéréotaxique)`

```{admonition} Recalage intra-sujet des volumes pour mouvement (avec volume de référence)
:class: tip
:name: recalage mouvement-tip

> Cette étape a été présentée dans le cadre du cours 3, [analyses morphométriques](https://psy3018.github.io/morphometrie.html) 

Souvent, le sujet ne maintient pas exactement la même position de la tête dans le scanner tout au long des acquisitions, qui peuvent parfois durer plus d'une heure et/ou exiger des arrêts. (p.e. baillements, fatigue musculaire, clignement de yeux, etc.). Ces mouvements ont des impacts non-négligeables sur le signal BOLD. A priori, ils peuvent entraîner des distorsions de l'intensité du signal de l'image. Dans un second temps, ils impliquent que, d'une image à l'autre, les voxels ne sont plus alignés par rapport à une référence (c.-à.-d. la boîte de l'image).

`1.Estimation des paramètres de transformation`: Le cerveau d'un même individu ne change pas de forme ou de taille à travers les acquisitions. Ainsi, cette étapese rapporte à l'estimation d'un sous-ensemble de transformations linéaires, la translation et la rotation. Nous pouvons obtenir l'estimation des paramètres **linéaires** de mouvement pour chaque volume du cerveau, pour:

- **3 translations (x, y, z)**
- **3 rotations (x, y, z)**

L'évolution des paramètres de mouvement sont souvent représenter au moyen d'un graphique comme celui ci-bas, où *X* est la variable du temps et *y* la valeurs des paramètres de mouvement.

!! Image montrant les paramètres de mouvement !!

`2.Ré-échantillonnage`: L'estimation de ces paramètres permet ensuite d'appliquer des transformations pour recaler chaque volume à un volume de référence choisi. Ce volume de référence peut être par exemple, le premier volume de la série, le dernier, ou bien la moyenne de tous les volumes.

Parmis les populations étudiées, ce sont les enfants et les personnes âgés qui tendent à bouger davantage lors des acquisitions. L'endurance musculaire est le plus grand prédicteur de la quantité de mouvement d'un sujet. Certains chercheurs choisissent d'exclure les sujets ayant bougé au-delà d'un certain seuil (p.e. lorsque les paramètres de mouvement montrent d'immenses pics, par exemple). Il arrive aussi que les images soient irrécupérables: alors on jette les données.
```

```{admonition} Recalage inter-modalité (BOLD avec $T1$ comme référence)
:class: tip
:name: recalage intermodalité-tip
Il est commun d'aligner l'image BOLD avec l'image anatomique T1 du sujet. Pourquoi? L'image fonctionnelle détient une moins bonne résolution spatiale que l'image structurelle $T1$ : nous avons de plus courtes durées d'acquisition pour acquérir un même volume.

`1. Estimation des paramètres de transformation`: Pour une image BOLD donnée, nous obtenons l'estimation des paramètres de transformations **linéaires** vers l'image $T1$ pour :
- **3 transations (x,y,z)**
- **3 rotations (x,y,z)**

`2. Ré-échantillonnage`: Les coordonnées sont transformées vers un nouvel espace en appliquant les transformations estimées à l'étape précédente.

!! image recalage BOLD-T1 !!
```

```{admonition} Recalage inter-sujet dans l'espace stéréotaxique (avec atlas comme référence)
:class: tip
:name: recalage intersujet-tip

> Cette étape a été présentée dans le cours 3, [Analyses morphométriques](https://psy3018.github.io/morphometrie.html)

Pour les comparaisons inter-individuelles ou les analyses statistiques de groupe, il doit y avoir une correspondance entre les voxels des images provenant de différents individus. Or, les cerveaux et les structures anatomiques peuvent avoir différentes tailles et formes d'individus en individus. Le recalage dans l'espace stéréotaxique (*spatial normalization* en anglais) consiste à recaler les cerveaux dans un espace standard cible défini par l'atlas choisi, les rendant ainsi comparables. Les templates MNI (Montreal Neurological Institute) sont un exemple d'atlas largement employés comme espace standard dans la communauté. 

`1. Estimation des paramètres de transformation`: Une variété d'algorithmes existent pour recaler les images individuelles à l'espace stéréotaxique. Typiquement, en plus des estimations de paramètres de transformations linéaires de **translations (x,y,z)** et **rotations (x,y,z)**, nous ajoutons les **mises à l'échelle (x,y,z)** (les cerveaux n'ont pas la même taille), et les transformations **non-linéaires** qui permettent de déformer les structures pour aligner les détails anatomiques des images d'un individu à l'autre.

`2. Ré-échantillonnage` Les coordonnées originales sont transformées vers un nouvel espace, en appliquant les transformations estimées.

!! image recalage stéréotaxique !!
```

De manière standard, un recalage intra-sujet est toujours performé pour corriger le mouvement du sujet au cours de l'acquisition. Pour les autres types de recalage, il en dépend des objectifs scientifiques ou des analyses statistiques entrevues par les expérimentateurs (p.e. individuelles ou de groupe). 

```{admonition} Lissage spatiale
:class: tip
:name: lissage spatiale-tip
Nous revenons ici sur une étape de prétraitement que nous avons déjà abordé lors du cours sur la VBM: le lissage spatial.  

> Pour un rappel, consultez le [Chapitre 3: Analyses morphométriques](https://psy3018.github.io/morphometrie.html)

 Le processus du lissage est semblable pour l'IRM fonctionnelle, mais la portée de cette étape est un peu différente comme l'image est dynamique (l'objet de ce lissage ne sont pas les valeurs de l'intensité de l'image comme en IRM structurelle, mais plutôt celles du signal BOLD). Certains artéfacts, comme le mouvement du sujet au cours de l'acquisition, peuvent entraîner des pics/fluctuations aléatoires dans le signal BOLD, et avoir un effet néfastes sur les analyses statistiques. Le lissage spatiale entre alors en jeu : il a pour effet de diminuer le bruit, en éliminant la contribution des fluctuations aléatoires ciblant des voxels spécifiques. De manière plus opérationnelle, le lissage consiste à prendre les voxels de l'image et à les remplacer par une nouvelle valeur considérant les valeurs des voxels voisins. Chaque voxels voisins se voit attribuer une pondération qui quantifie sa contribution à la nouvelle valeur attribué à un voxel cible. La valeur originale du voxel cible est celle qui aura la plus grande pondération, et les valeurs des voxels voisins seront pondérés en fonction de la proximité entretenue avec le voxel cible. Mis à part l'amélioration du ratio signal-bruit, le lissage permet également d'atténuer les erreurs/imperfections de recalage inter-sujet. 
 
!! image lissage sur cerveau !!

Le paramètre `FWHM` (*full width at half maximum*) contrôle l'échelle de ce lissage (plus important ou moins important). Il détermine l'étalement des voxels voisins qui participeront à la nouvelle valeur d'un voxel cible. D'un point de vue mathématique, le paramètre `FWHM` représente la demi de la largeur de la courbe gaussienne, qui décrit du bruit distribuée aléatoirement. Une plus grande valeur `FWHM` sous-tend une participation plus étalée des voxels voisins à la nouvelle valeur  d'un voxel cible de l'image. Plusieurs études choisissent `6 mm` comme valeur pour le paramètre `FWHM`. 
```

```{admonition} Filtrage des facteurs de non-intérêt
:class: tip
:name: filtrage-tip

La dernière étape de prétraitement qui sera abordé est celle du filtrage de facteurs de non-intérêt. Différents **facteurs confondants** ou **artéfacts** peuvent induire des fluctuations dans le signal BOLD. Ces artéfacts peuvent avoir différentes fréquences du spectre, soit plus lentes ou rapides. Lorsque ce bruit est systématique ou périodique, il possible de le régresser (c'est-à-dire de le retirer) en employant différentes stratégies comme des filtres. Les dérives lentes constituent un exemple commun de facteurs de non-intérêt, et elles sont assez facilement repérables dans le signal. Dans ce cas, pouvons appliquer un filtre passe-haut, qui conserve uniquement les fréquence plus haute qu'un certain seuil (p.e. 0.01 Hz). 

!! image filtrage passe-haut pour dérives lentes !!
```

### Analyse statistiques

Cette section est un aperçu général du cours sur les analyses statistiques à venir. Nous laisserons certains détails de côté pour le moment, mais nous y reviendrons dans le cours 6 sur les [analyses statistiques](https://psy3018.github.io/cartes_statistiques.html). Rappelons une fois de plus nos objectifs en IRMf : nous voulons dégager de nouvelles connaissances sur le fonctionnement du cerveau. Ceci implique le recours à des analyses statistiques. 

Les analyses statistiques comportent généralement des **analyses individuelles** dans lesquelles les séries temporelles sont analysés séparément pour chacun des sujets (on analyse l'effet des manipulations expérimentales), puis des **analyses de groupe** (on analyse l'effet de groupe), où ces données sont combinées pour plusieurs sujets pour être analysées. 

#### IRMf - Expérience basée sur une tâche
Pour déterminer si l'activité des voxels du cerveau changent en réponse à des manipulations expérimentales, une approche expérimentale standard consiste à manipuler la tâche que réalise le sujet dans le scanneur, par exemple en alternant différentes conditions par blocs (yeux ouverts, yeux fermés). Nous avons ensuite recours à des constrastes, aussi appelées analyse de soustraction qui procède en comparant les séries temporelles d'une condition à une autre condition, ou à un seuil de base. Ces contrastes sont répétées pour chacun des voxels du cerveau. 


```{admonition} Problème de comparaisons multiples
:class: tip
:name: comparaisons multiples-tip
Les analyses statistiques en IRMf surviennent dans un contexte particulier. Ce sont des analyses massivement univariées, c'est-à-dire que nous avons des tests statistiques répétés plusieurs milliers de fois (à chacun de nos voxels). Ceci entraîne un problème de comparaisons multiples qui requiert une correction pour l'inflation de faux positifs. Ceci sera abordé plus en détail dans le cours sur les analyses statistiques.
```

```{admonition} Paradigmes classiques
:class: tip
:name: paradigmes classiques-tip
Les premiers paradigmes expérimentaux en IRMf consistaient à répéter un tâche pendant la durée de l'acquisition, puis à contraster avec un seuil de base en utilisant des procédures statistiques comme le test-t. Inspiré par ces approches, les premières études faisait la différence entre la moyenne d'activation lors de tâche et à l'état de repos. Dans l'études par Kwong et al. (1992) par exemple, des blocs de stimulations visuels étaient suivis de blocs sans stimulation. 
```

#### Régression univariée
Il est possible de généraliser l'analyse de soustraction pour tenir compte de **1) la forme de la réponse hémodynamique**
**2) la présence de plusieurs conditions dans une même expérience**. Tel que soulevé précédemment, une grande partie du travail en IRMf consiste à analyser/expliquer les séries temporelles. Nous pouvons utiliser nos connaissances sur la fonction de réponse hémodynamique, ainsi que celles sur les conditions du paradigme expérimental, pour estimer le niveau d'activation BOLD dans une condition (nous irons plus dans les détails ultérieurement, mais globalement celles-ci deviennent les variables explicatives dans des modèles de régressions qui tente d'expliquer les séries temporelles). Les séries temporelles sont aussi expliquer comme étant partiellement **3) du bruit/erreur**, que l'on suppose aléatoire. Nous ajustons les paramètres de ce modèle tenant compte **1)**, **2)** et **3)**. Ceux-ci sont mis à l'échelle : c'est ce qui nous permet de connaître le niveau d'activation pour une condition. Une fois ce niveau connu, il peut être contrasté entre différentes conditions ou avec un niveau de base, en calculant la différence entre les moyennes d'activation de chaque condition respectivement. En employant une distribution gaussienne, nous pouvons évaluer la probabilité d'observer une telle différence, ou n'importe quelle statistique donnée (p.e. test-t). Le formalisme décrit ci-haut s'appelle le modèle linéaire général. On en reparlera au cours 5. 

#### IRMf - Cartes d'activation
Les cartes d'activation sont souvent ce que l'on retrouvent dans des articles scientifiques dans la section des résultats. Ce sont des cartes du cerveau sur lesquelles se superposent les statistiques obtenues (p.e. niveau d'activation, test-t, valeur p). Elles sont supersposées vis-à-vis des voxels ou régions correspondant(e)s. Ces cartes peuvent être construites pour des **sujets** (p.e. effet yeux ouverts vs yeux fermés) ou des **groupes**, si nous combinons les données de plusieurs sujets (p.e. effet de l'âge ou d'appartenir au groupe non-voyant vs voyant). Elles sont souvent présentées suite à l'application de seuils ou de masques, venant isoler les régions les plus actives, avec les différences moyennes entre conditions les plus importantes et/ou les plus statistiquement significatives. Via de telles cartes, nous pouvons étudier l’organisation de systèmes d'intérêt (visuel, moteur, auditif, mémoire de travail, etc), mais aussi comparer des groupes ou bien associer le niveau d’activation à des traits d'intérêt comme le QI. La faisabilité de cette approche a été démontrée simultanément par trois groupes: *Ogawa et al. PNAS 1992; Kwong et al. PNAS 1992; Bandettini et al. MRM 1992*, ayant introduit l'idée de cartographier le cerveau avec des tâches en IRMf. 

#### Conclusion
La réalisation d'une expérience d'IRMf nécessite de bien penser les conditions d'intérêts et de contrôles pour isoler des processus cognitifs pertinents, mais cela requiert aussi de réfléchir aux hypothèses sous-jacentes. Nous débutons généralement avec une hypothèse scientifique qui postule que certaines manipulations expérimentales vont guider des différences observables dans des régions d'intérêt. Nous poursuivons avec des hypothèses neuronales : les populations de neurones vont s'activer en réponse à nos conditions. Nous supposons que la réponse neuronale sera couplée à une réponse vasculaire caractéristique qu'il est possible de modéliser avec la fonction hémodynamique, laquelle est linéaire et invariante dans le temps. Finalement, nous faisons des hypothèses sur la généralisabilité de nos résultats.

#### Un peu d'histoire - Gall -

```{admonition} Origines de la ségrégation fonctionnelle
:class: tip
:name: histoire-tip
De nos jours, une partie importante de la littérature suppose que le cerveau est découpé en aires fonctionnelles, en d'autre mots, elle admet le principe de ségrégation fonctionnelle. L'idée de localiser les fonctions cognitives n'est pas une idée nouvelle. Dans les faits, c'était l'idée de Gall, avec la phrénologie, qui assumait un lien entre la morphologie du crâne et les fonctions cognitives. Selon la phrénologie, la forme de la boîte crânienne est informative des tendances des individus. Les aires du cerveau sont organisées selon des concepts cognitifs comme "counsciousness", "destructiveness" et autres dimensions. Bien que peu rigoureuse, cette idée est revisitée dans le cadre de la modalité de l'IRMf, mais avec bien plus de rigueur scientifique. Son émergence légitime dans le discours scientifique remonte, notamment, aux travaux de Brodmann lequel employait des techniques de teintures pour observer la forme et variations des cellules nerveuses (cytoarchitecture) à travers le cortex. Nous admettons, aujourd'hui, arriver à accéder à certains aspects de l'organisation fonctionnelle cérébrale.
```

```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/-u0WCHGi8_A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```

### Cartes d'activation
```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/ayr6xFw2qPs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```

### Conclusions et références suggérées

### Références

```{bibliography}
:filter: docname in docnames
```

## Exercices

### Exercice 1
Choisissez la bonne réponse. Des données d’IRMf sont en général...
 1. Une image du cerveau.
 2. Une dizaine d’images du cerveau.
 3. Des centaines d’images du cerveau.

### Exercice 2
Qu’est ce que le signal BOLD? (vrai / faux).
 1. Un signal très courageux.
 2. Une séquence pondérée en T2*.
 3. Un type de séquence d’IRM qui mesure l’activité du cerveau.
 4. Un type de séquence d’IRM qui mesure l’oxygénation du sang.

### Exercice 3
Choisissez la bonne réponse. Le signal BOLD dépend sur...
 1. Le flux sanguin local.
 2. Le volume sanguin local.
 3. La concentration relative en désoxyhémoglobine.
 4. Toutes les réponses ci-dessus.

### Exercice 4
Vrai / faux. Le principe d’additivité de la réponse hémodynamique est...
 1. Un modèle mathématique.
 2. Une propriété bien connue du couplage neurovasculaire.
 3. Une hypothèse courante, en partie confirmée expérimentalement.

### Exercice 4
Quel est l’événement principal à l’origine des changements de signal mesuré par le BOLD?

### Exercice 5
Dans quelle portion de l’arbre vasculaire observe-t-on les changements principaux liés à l’activité neuronale locale?

### Exercice 6
Vrai / faux?
 1. La réponse hémodynamique démarre immédiatement après l’excitation neuronale.
 2. La réponse hémodynamique est visible une seconde après l’excitation neuronale.
 3. La réponse hémodynamique est maximale 2 secondes après l’excitation neuronale.
 4. La réponse hémodynamique est toujours visible 7 secondes après l’excitation neuronale.
 5. La réponse hémodynamique est toujours visible 30 secondes après l’excitation neuronale.

### Exercice 7
Vrai / faux / peut-être? (expliquez pourquoi)
 1. Les données IRM fonctionnelle et structurelle doivent être réalignées pour générer une carte d’activation.
 2. Les données d’IRMf “brutes” (avant prétraitement) sont inutilisables pour générer une carte d’activation.
 3. Le lissage spatial est important, même pour une analyse individuelle.

### Exercice 8
On compare l’activation pour une tâche de mémoire dans le cortex frontal entre deux groupes de participants: des sujets sains et des sujets âgés (N=20 par groupe). Contrairement à nos hypothèses, on ne trouve aucune différence. Donnez trois raisons qui peuvent expliquer ce résultat.
