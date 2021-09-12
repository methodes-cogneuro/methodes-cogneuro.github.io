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
      <a href="https://github.com/elisabethloranger">
        <img src="https://avatars.githubusercontent.com/u/90270981?v=4?s=100" width="100px;" alt=""/>
        <br /><sub><b>Élisabeth Loranger</b></sub>
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

On va parler du modèle de régression dans le contexte de l’IRM fonctionnelle, ainsi que pour générer des cartes statistiques individuelles et de groupe sur l’activité cérébrale. Les statistiques de groupe permettent de combiner l’activation de plusieurs individus et ainsi de contraster des groupes (ex. groupe de personnes jeunes et groupe de personnes âgées).


Nous allons l’appliquer à l’IRMf aujourd’hui car c’est la modalité où on va avoir les modèles les plus complexes puisqu’on va devoir faire un modèle individuel et un modèle de groupe, mais la mécanique de ce qui sera vu dans ce cours s’applique à la plupart des modalités de façon plus ou moins identique. 

Les objectifs du cours sont les suivants : 
On va détailler les étapes de génération d’une carte paramétrique cérébrale : 
 * Carte IRMf : fonction de réponse hémodynamique, dessin expérimental 
 * Régression linéaire sur des séries temporelles, contraste individuel
 * Régression linéaire sur des paramètres d’activation, contraste de groupe

## Dessin expérimental, contraste

Ce schéma représente la réponse aux émotions de l’amygdale lors de la présentation de stimuli. Les stimuli présentent 3 visages, un en haut et deux en bas, et le participant doit mettre les visages identiques en correspondance et donner sa réponse via un bouton. Il y a plusieurs processus mentaux qui vont se passer, incluant l’identification des émotions que présentent les visages. C’est pour cela qu’entre la présentation des visages, on a la présentation d’un stimulus contrôle avec des formes (ellipses) avec différentes orientations à la place des visages. La même tâche de mise en correspondance est faite avec les formes. 
On va présenter ces stimuli pour des durées relativement brèves de 4 secondes et on va alterner la condition des visages et la condition contrôle. La discrimination visuelle est présente dans les deux conditions de cette tâche, les visages ont un contenu émotionnel qui n’est pas présent pour les formes. 

Lorsque nous allons faire le contraste entre l’activité hémodynamique des deux conditions, nous allons capturer des régions qui sont spécifiquement activées lors de la présentation de visages avec un contenu émotionnel. Ici, on identifie l’amygdale. Par ailleurs, faire ces contrastes n’est pas de toute simplicité.

## Contraste et réponse hémodynamique

Le premier schéma en haut représente ce qui se passerait au niveau neuronal dans un monde idéal. Dans ce schéma, une activation maximale est atteinte lors de la présentation du stimulus de la condition 1 et, lors de la condition 2 (e.g. condition contrôle), l’activation tombe immédiatement à 0. En faisant la valeur moyenne lors des blocs rouge (1) moins la valeur moyenne pendant les blocs bleus (0), nous obtiendrions un contraste de 1 entre les deux conditions. Or, nous n’avons accès à des données comme celles-ci que si nous ouvrons la boite crânienne de notre participant.

Lors de l’IRM, nous mesurons un phénomène vasculaire qui est lent, et donc, qui met quelques secondes à venir et quelques secondes à partir. En fait, on dit que ça prend environ 5 secondes. Puisque ces blocs ne sont pas des blocs de 30 secondes, la réponse hémodynamique mesurée par l’IRMf sera décalée par rapport à la présentation réelle des blocs de conditions. Ici, puisque les blocs sont environ du même temps que le temps nécessaire pour observer une réponse hémodynamique lors de la présentation des visages, le pic d’activation est atteint à la fin de la présentation du stimulus. Ensuite, lors de la présentation des formes, cela prendra l’entièreté du bloc afin que l’activation revienne à la ligne de base. Si nous ne faisons que la moyenne d’activation des blocs rouges et la moyenne des blocs bleus, nous obtiendrions 0.5 pour les deux.  En effet, sur la moitié de chaque bloc, l’activation est proche du minimum et sur l’autre moitié elle est près du maximum. Ainsi, nous trouverions une valeur de 0 pour la différence entre les deux conditions, signifiant qu’il n’y a aucun contraste. 

Pour remédier à la situation, on peut décaler le bloc de mesure fonction du décalage de la réponse hémodynamique. Dans le 3e graphique, nous avons décalé les blocs de mesure pour les deux conditions d’environ 2.5 secondes. Ainsi, le pic se situera au centre du bloc rouge, et le retour aux valeurs de base se situera au centre des blocs bleus. Les moyennes seront ainsi de 0.75 et 0.25 respectivement, ce qui est plus représentatif de la différence d’activation que l’on retrouve réellement entre les deux conditions. Le contraste sera ainsi de 0.5, ce qui n’est toujours par optimal considèrent qu’il y a théoriquement une différence de 100% entre les deux conditions. 

La solution est de rétrécir le bloc de mesure pour les deux conditions. Cela permet de concentrer les données utilisées pour chaque bloc autour du pic, ce qui fait que notre moyenne se rapproche de la véritable amplitude pour les deux conditions. Nous pouvons imaginer que la moyenne pour les blocs rouges se situera autour de 0.9 puisqu’elle n’est pas parfaitement à 1 et que l’inverse se produira pour les blocs bleus avec une moyenne autour de 0.1, ce qui nous donnera un contraste résultant de 0.8. 

On va se donner un modèle mathématique comportant deux fonctions Gammas. Ces modèles peuvent être plus ou moins complexes. Nous pourrions faire un modèle pour un événement unitaire (unique) dont le seul paramètre est l’amplitude du pic, apparaissant à un moment fixe à la suite de la présentation du stimulus.  

Ensuite, nous pouvons complexifier le modèle pour qu’il soit plus près de ce qu’il se passe réellement au niveau neuronal. Nous pouvons ajouter un paramètre de plongée initiale ou initial dip, qui représente le moment ou la glie tire de l’oxygène des capillaires avant l’augmentation du flux et du volume sanguin. Il y a ainsi une augmentation de la concentration relative en déoxyhémoglobine et donc, une diminution initiale du signal BOLD. 
Nous pouvons aussi ajouter la plongée post-stimulus ou post-stimulus dip comme paramètre du modèle. Ceci représente une surcontraction des capillaires à la suite de la réponse hémodynamique ou une inhibition neuronale, son origine n’est pas encore claire. Un dernier paramètre peut être ajouté au modèle, soit la vitesse à laquelle l’activation augmente et diminue, ou bien la largeur du pic. 

Trois postulats permettent la prédiction de la réponse à n’importe quel train de stimulation. 

*	Additivité : Lorsque nous avons plusieurs événements, la réponse sera la somme des activations des événements simples. 
*	Proportionnalité : Si nous avons des événements qui ont des amplitudes différentes, la réponse observée sera proportionnelle à la stimulation. 
*	Invariance dans le temps

Dans cette image, les réponses sont très séparées dans le temps donc elles n’interagissent pas ensemble. Si elles étaient collées, nous aurions vu une superposition des réponses. 

Ici, en bleu, nous voyons les données expérimentales et en rouge, le modèle de réponse. Nous pouvons ajuster le modèle en fonction de différents paramètres tels que vus plus tôt, mais un premier paramètre important est la localisation du pic d’activation. En fait, la courbe en entier doit passer près des points expérimentaux. Ce processus se nomme l’ajustement ou le goodness of fit. Donc, en estimant le modèle qui est le plus près des données expérimentales, nous trouvons une amplitude du pic qui se situe près de 0.5 (en y). 

Finalement, quand on parle de régressions linéaires pour des séries temporelles en IRMf, c’est de ce qu’on parle. La partie linéaire est en fait le pic d’activation. 
 
On peut avoir différents stimuli, qui peuvent être de longueur et d’amplitude variable, ce qui va nous donner une fonction en « escalier ». Ensuite, nous appliquons notre modèle mathématique de réponse, ce qui nous donne notre réponse prédite qui est représentée par la courbe rouge dans ce graphique. Cependant, nous ne connaissons pas son amplitude. C’est ensuite que nous faisons la technique d’ajustement, où nous ne regardons pas seulement le max, nous combinons tous nos événements. Cette méthode est très puissante et elle nous permet de tirer intégralité de toutes nos données. 

## Modéle linéaire et cartes statistiques individuelles
```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/WIvMt3r7AVU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```
Ici, à gauche, nous avons le signal enregistré. Nous avons une ligne de base qui est plutôt arbitraire. Le signal n’est jamais à 0. Nous allons essayer de décomposer ce signal en la combinaison de 3 choses : (1) la ligne de base, (2) l’activation BOLD liée à la tâche et (3) les résidus qui représentent tout ce qui ne s’explique pas par notre modèle. Ce que nous ne connaissons pas lorsque nous faisons une régression linéaire ce sont les coefficients ou l’amplitude de chaque composante de notre signal (e.g. 100x pour la ligne de base, 10x opur le signal BOLD et x2 pour les résidus). Ces valeurs sont en fait un modèle mathématique que l’on appelle l’estimation des moindres carrés, qui nous donne des paramètres permettant l’amplitude des résidus la plus petite possible. En appliquant les coefficients aux 3 graphiques de décomposition et en additionnant les valeurs pour chaque point donné, nous obtenons une courbe qui est très près de notre signal. 

Les noms communs pour ces coefficients sont le ß0 (bêta 0) pour la ligne de base et le ß1 (bêta 1) pour l’activation BOLD. À priori, nous ne connaissons pas ces valeurs. Ce que nous connaissons, c’est la courbe noire, la courbe rouge et la courbe bleue, qui elle a été mesurée. 

Le coefficient ß1 nous indique la taille de la réponse à notre tâche en faisait une mise à l’échelle de celle-ci. Il est possible que nous ayons plus d’une condition d’intérêt et que nous voulions comparer ces deux réponses. À ce moment-là, nous pouvons faire le contraste entre les bêtas associés aux deux conditions en soustrayant ß2 à ß1. L’étape suivante est de faire un test statistique sur ß1 pour savoir si l’activation est significativement plus élevée que l’activation de base ou sur ß1 – ß2 pour savoir s’il y a une différence significative entre l’activation aux deux conditions. 

Ce qui vient d’être expliqué peut être fait à chaque voxel. En ce sens, chaque voxel possède une activation différente, et donc, a un ß0 et un ß1 différent. Ainsi, il est possible de faire des cartes statistiques à l’aide de cette méthode. Ici, nous remarquons que nous avons des valeurs fortes dans le cortex frontal et des valeurs négatives en périphérie du cortex occipital. Le terme exact pour ce type de carte est un modèle linéaire massivement univarié, car on va aller regarder un voxel à la fois plutôt que de regarder des regroupements de voxels. 

## Cartes statistiques de groupe
```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/mQtO_RwUIaE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```
Ici, on a une représentation différente. Cette représentation a l’avantage de permettre de voir plusieurs « courbes » simultanément de manière claire. En mathématique, on appel ce type de représentation des « matrices ».

On a plusieurs tableaux dans cette représentation. Dans le premier, on a une seule colonne avec plein de lignes, ensuite on a un tableau qui a le même nombre de lignes que le premier mais avec 4 colonnes et un dernier tableau avec seulement 3 lignes et une colonne. Dans les deux premiers tableaux, chaque ligne correspond à un sujet et chaque colonne correspond à un type de variable. Il faut préciser que l’on n’a pas pris le scan cérébral complet pour le premier tableau. En fait, on a pris le même voxel chez tous les participants (à l’aide d’un recalage).

Les tons de gris représentent en fait des valeurs numériques. Or, pour aider à la visualisation, nous avons utilisé une échelle de couleurs qui représente ces valeurs. 

Le premier tableau représente les valeurs des cartes cérébrales, qui sont les valeurs que l’on cherche à expliquer. Les tableaux à droite du « = » représentent les valeurs qui permettent d’expliquer les valeurs des cartes cérébrales. 
Ici, on a deux vecteurs qui cotent pour le sexe de nos participants et un autre qui représente le score de dépression pour chacune de nos observations (dans le premier tableau). 

Cette représentation est plutôt simple, nous avons une formule ressemblant à y = mx+b, donnant une relation linéaire. À gauche on a le y, c’est ce qu’on cherche à modéliser. Le tableau à droite, on a les paramètres explicatifs. Pour le sexe, on a mis un 1 quand le sexe correspondait au sujet et un 0 lorsqu’il ne correspondait pas. Ainsi, on remarque que, ici, la moitié des sujets étaient des hommes et l’autre moitié étaient des femmes. La variable de dépression est mesurée à l’aide de questionnaires et le score est représenté ici dans la 3e colonne du 2e tableau. Le 3e tableau représente l’amplitude des différentes facteurs explicatifs que l’on peut changer afin de mieux expliquer nos valeurs IRMf. Ceci revient à la même chose qui a été vue dans les graphiques présentés plus tôt. Ainsi, le score que l’on tente d’expliquer pour un sujet (une ligne) sera obtenu à l’aide de la formule suivante : le score « homme » du sujet x le coefficient « homme » + le score « femme » du sujet x le coefficient « femme » + le score « dépression » du sujet x le coefficient « dépression ». Ce qui reste et qui n,est pas expliqué par cette formule correspondra aux résidus. Tel que vu plus tôt, la formule avec les coefficients auront comme but de minimiser les résidus le plus possible. 

Ici, on a un exemple un peu plus complexe. À gauche, on a ce qu’on vient de voir et au centre, on a séparé le score de dépression pour les femmes et celui pour les hommes. 

Dans l’exemple précédent, le coefficient de dépression était le même pour les hommes et les femmes. On prétendait alors que le niveau d’influence de la dépression sur le cerveau des femmes et celui des hommes était pareil. Dans le tableau du centre, nous attribuions un coefficient différent aux scores de dépression des hommes et celui des femmes, prétendant alors que l’influence de la dépression sur le cerveau pourrait différer en fonction du sexe. Ici, on test alors le principe d’interaction. En statistiques classiques, on pourrait comparer ce modèle a une ANOVA.

En réalité, ce modèle se nomme le modèle linéaire général car on peut pas mal tout tester. Si on veut faire un test-t, on peut le faire à l’aide de ce modèle. 

Si on prend deux coefficients de notre modèle, on peut regarder la différence entre ces deux coefficients. Par exemple, on peut regarder si l’influence de la dépression sur le cerveau chez les femmes (ß1) diffère de celle de la dépression sur le cerveau chez les hommes (ß2). 

Ca donnerait quelque chose comme ça et nous donnerait une carte de contraste statistique qui nous permet de contraster l’influence de la dépression chez les femmes et chez les hommes. 
Ce qui va changer d’un voxel à l’autre ce n’est pas les facteurs explicatifs, ce sont les y (les mesures d’activation). On n’aura ainsi pas les mêmes bêtas et les mêmes valeurs de contraste. C’est aussi appelé une approche massivement univariée. 

On peut parler d’une analyse de niveau 1 pour les analyses individuelles et les analyses de niveau 2 pour les analyses de groupe. 

## Conclusion 

En générale quand on parle de l’IRMf ou même de la VBM, on trouve des blobs qui présentent des effets significatifs. Ce qui est important de se rappeler est toute la série d’étapes qui mènent à ce type de carte. 
1. La première, l’hypothèse psychologique : 	On avait commencé le cours avec ces deux tâches avec les visages qui expriment les émotions et des stimuli contrôles. Notre est hypothèse est que ce sont les visages qui expliquent le patron d’activation observé.  
2. Ensuite, on a des hypothèses au niveau neuronal : On émet des hypothèses au sujet du type de réponse neuronale observé. En IRMf, on émet l’hypothèse que l’activation atteint son plafond quand la stimulation est débutée et qu’elle retombe à 0 une fois le bloc terminé. 
3. Finalement, on a des hypothèses hémodynamiques : On va supposer que l’activité BOLD enregistrée en IRMf va correspondre à l’activité neuronale. 

À la fin, on aura des étapes d’analyses d’images, de recalage, de débruitage et de modélisation statistique. 

Ainsi, il y a beaucoup de choses, de choix et d’hypothèses qui vont derrière ce petit blob rouge qui ressort dans des cartes statistiques. 
