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
(imagerie-optique-chapitre)=
# Imagerie optique

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Xanthylajoie">
        <img src="https://avatars.githubusercontent.com/u/90349544?v=4?s=100" width="100px;" alt=""/>
        <br /><sub><b>Xanthy Lajoie</b></sub>
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
        <a title="Révision du texte">👀</a>
    </td>
  </tr>
</table>

```{warning}
Ce chapitre est en cours de développement. Il se peut que l'information soit incomplète, ou sujette à changement.
```
L'imagerie optique cérébrale, encore appelée spectroscopie proche infrarouge fonctionnelle, est une technique qui permet de mesurer les corrélats vasculaires de l'activité cérébrale, de manière assez similaire à l'IRMf. En revanche elle repose sur un principe physique très différent: la diffusion et l'absorption de la lumière dans les tissus cérébraux. Ses limites et faiblesses sont aussi bien distinctes de l'IRMf.

```{figure} imagerie_optique/fnirs.jpg
---
width: 600px
name: fnirs-fig
---
Système d'imagerie optique [NTS gowerlabs](https://www.gowerlabs.co.uk/nts-main). Image tirée de [wikipedia](https://en.wikipedia.org/wiki/Functional_near-infrared_spectroscopy#/media/File:Blonde_fNIRS_lady.jpg) sous licence [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0).
```

Les objectifs spécifiques de ce chapitre sont :
 * Principes physiques et physiologiques de l'imagerie optique.
 * Génération d'images en imagerie optique.
 * Application de l'imagerie optique en neuroscience cognitive.

## Principes physiques et physiologiques

### Lumière infrarouge et tissus biologiques
```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/61rWjVkpgh0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
```

La lumière pénètre et diffuse au travers des tissus biologiques. Cela peut être observé facilement, par exemple en plaçant une lampe de poche derrière votre main. Votre main est en partie transparente et la lumière peut la pénétrer. Certains tissus vont plus absorber la lumière que d'autres, et permettre de voir le genre de tissus présent à l’intérieur de notre main. Mais quel genre de tissus exactement? cela va dépendre du genre de lumière... La lumière proche infra-rouge est intéressante de ce point de vue, car elle est particulièrement absorbée par l'hémoglobine. La vidéo ci-dessus permet ainsi d'observer assez clairement la vascularisation de la main avec de la lumière (et une caméra) proche-infrarouge. Karl von Vierordt en 1876 avait déjà pu observer qu'il était possible d'observer la diminution d'oxyhémoglobine dans la main avec cette technique, en limitant l'arrivée de sang dans la main au moyen d'une ligature. L'imagerie optique cérébrale repose aussi sur les propriétés physiques de la lumière proche infra-rouge dans les tissus biologiques.

### Spectre d'absorption des tissus
```{figure} imagerie_optique/spectre_hemoglobine.png
---
width: 600px
name: spectre-hemoglobine-fig
---
Niveau d'absorption de la lumière par l'oxy- et la déoxy-hémoglobine, en fonction de la longueur d'onde. La région proche infrarouge (NIR, near infra-red) est indiquée. Image tirée de [Abtahi et al. (2017)](https://doi.org/10.3390/healthcare5020020) sous licence [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0).
```
Ce diagramme représente quelles longueurs d'ondes de la lumière sont absorbées par l'oxy- et la déoxy-hémoglobine, donc HbO2 (hémoglobine oxygénée en rouge) et Hb (hémoglobine non oxygénée en bleu). On peut voir qu'il y a des longueurs d'onde pour lesquelles le niveau d'absorption HbO2 vs Hb est très différent. Par exemple, à 700 nanomètres la lumière est plus absorbée par Hb, alors qu'à 900 nanomètres la lumière est plus absorbée par HbO2. Si on peut mesurer le niveau d'absorption dans le sang pour ces deux couleurs, en les comparant, on va pouvoir essayer de dissocier les concentrations en HbO2 et Hb. Un autre point important: ces longueurs d'onde sont très peu absorbées par l'eau, et la lumière proche infra-rouge va bien pénétrer dans les tissus biologiques. Donc, juste en étudiant la quantité d'absorption de deux longueurs d'onde proche infrarouge dans le cerveau, on va pouvoir quantifier le contenu en HbO2 et HB! Mais reste à savoir comment on peut faire cette mesure de manière localisée dans une petite région du cerveau.

### Diffusion de la lumière
```{figure} imagerie_optique/nir-diffusion.png
---
width: 300px
name: nir-diffusion-fig
---
Mesure localisée dans le cerveau en imagerie optique. Un *émetteur* de lumière proche infrarouge est appliquée sur le scalp. Cette lumière est diffusée dans le cerveau. Après avoir traversé une petite portion de tissus cérébraux, elle va être émise de nouveau à la surface du scalp, et mesurée par un *récepteur* Image tirée de [Abtahi et al. (2017)](https://doi.org/10.3390/healthcare5020020) sous licence [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0).
```
Dans le premier exemple que l'on a vu, avec une lampe qui illumine la main, la lumière traverse notre main en ligne droite depuis la lampe, jusqu'à notre oeil. Si l'on applique le même principe au cerveau, la lumière va traverser l'ensemble des tissus, et on ne pourra pas identifier quelle région du cerveau a absorbé la lumière. On ne pourra jamais faire des images avec cette méthode.
Mais si on envoie de la lumière dans le cerveau, une partie de cette lumière va se diffuser, selon un principe de marche aléatoire. Si on regarde le scalp autour de l'émetteur de lumière, la lumière diffusée va pouvoir être mesurée. Plus on va loin de l’émetteur, et plus cette lumière a traversé loin dans le cerveau. Si on va trop loin, de nombreux tissus seront mélangés. Si on va trop près, la lumière diffusée n'aura pas pénétré jusqu'au cerveau. Mais si on met notre détecteur à la bonne distance de l’émetteur (quelques cms), cette lumière aura traversé une région spécifique du cerveau, qui aura une forme en "U".

```{admonition} Attention!
:class: caution attention
:name: nirs-warning
Seules les régions cérébrales proches du scalp pourront être mesurées précisément avec l'imagerie optique. Pour mesurer de la lumière qui a pénétré très profondément dans le cerveau, il faudra que celle ci traverse de nombreux tissus, et on n'aura pas une mesure spécifique des tissus profonds.
```

### Couplage neurovasculaire
On a maintenant vu principe physique qui nous permet de mesurer la concentration en HbO2 et Hb dans une région (superficielle) du cerveau. Le principe physiologique sur lequel repose l'imagerie optique est le même que pour l'IRMf, c'est à dire le **couplage neurovasculaire**. Vous pouvez vous référez à la [section](couplage-neurovasculaire-section) du chapitre sur l'IRMf pour plus de détails. Brièvement, l'activité neuronale, notamment post-synaptique, requiert une consommation d'oxygène au niveau des cellules gliales, immédiatement à proximité des neurones concernés. Cette consommation d'oxygène va entrainer une augmentation d'HbO2 et une diminution relative d'HB à proximité des populations de neurones activés. C'est ce phénomène de couplage neurovasculaire qu'on mesure à la fois en IRMf et en imagerie optique.

## Acquisitions en imagerie optique

### Montage
Ici, c'est vraiment la diffusion de la lumière qui va compter donc ici à gauche vous avez une IRM T1, à droite vous avez un T1 segmentée donc en violet on a on a une segmentation de matière grise, en vert l'extérieur du cerveau et en bleu on a la matière blanche. On peut essayer de modéliser les caractéristiques biophysiques de ces tissus-là alors comment elles reflètent la lumière et à partir de ça on peut prédire comment la lumière va diffuser dépendamment d’où on va mettre notre émetteur. Ça va aussi dépendre de la longueur d’onde. Donc à droite, vous avez une simulation d’où positionner votre émetteur et le récepteur pour augmenter la sensibilité. Évidemment, on ne peut pas prendre des mesures profondes puisque la lumière va diffuser dans tout les sens et on n’aura pas des mesures spécifiques du tissu. Les mesures d’imagerie optique sont très localisées spatialement, mais ce sont des mesures superficielles du cortex. Il y a beaucoup de procédures d’optimisation sur comment bien placer nos sources et récepteurs. Bien sûr, ça dépend de l’anatomie de chaque participant mais aussi des règles générales connues.
Ici, ça représente un montage où on va avoir différents canaux qui peuvent être activés en pairs (récepteur + émetteur) de façon dynamique. Ça crée un maillage sur la tête comme avec un EEG et à partir des mesures qu'on a sur les différents canaux, on peut aller interpoler. Donc, calculer une moyenne de ces récepteurs en donnant plus d'importance aux récepteurs qui sont plus proche des canaux (proches d'un point donné du scan) Avec ça, on peut faire une image de l'activité au niveau du scalp.  Par la suite, on va essayer de reconstruire l'image au niveau du cortex individuel, en prenant en compte l’IRM T1. Ce n’est pas fait de manière standard du tout en imagerie optique. Donc, on parle de tomographie optique diffuse.
Tomographie : reconstruire une image à partir de différentes projections, ici les productions sont au niveau du scalp. Ici, le principe physique qu'on cherche à inverser, c'est la diffusion de la lumière. Donc c'est pour ça qu'on parle de ta de tomographie optique diffuse. C’est aussi une étape qui va jouer un rôle dans la chaîne de traitement de données.
Ici, c'est le même montage présenté ci-desus. Alors, on a disposé un certain nombre de canaux sur le cortex et on vient stimuler la main droite des participants. On sait que ça va venir activer principalement le cortex sensorimoteur gauche (controlatéral). L'essentiel de l'activation qu’on va observer, que ce soit le contrôle moteur ou les réponses à des stimulations sensorielles, c'est plutôt au niveau du cortex sensorimoteur gauche. C’est un paradigme de blocs de 10 secondes. En termes d'analyse, ils ont fait de la moyenne mobile, ce qu’on ne doit pas faire. Beaucoup de biais statistiques ne s'appliquent pas à l'imagerie optique.

## Application en neuroscience cognitive

Ici, ce qu'on fait, c'est vraiment ce que je vous ai dit qu'on ne devrait pas faire. C'est qu'on a mis une source infrarouge d'un côté et un système de détection de l'autre. Donc, en fait, on va vraiment s'intéresser à la vascularisation de l'ensemble du cerveau pas une zone en particulier. C’est donc nul pour faire de l'imagerie fonctionnelle. Par contre, on est en 1977, c’est encore nouveau donc on le fait quand même. Jobsis et ses collaborateurs avaient l’idée de faire de l’hypercapnie. Ce qui veut dire qu’on va se forcer à respirer très très vite donc en fait on augmente la concentration en oxygène dans le sang et ça cause un peu l'effet inverse de l'activité neuronale. Quand l’activité neuronale monte il y a plus de désoxyhémoglobine localement à ce moment-là et le vaisseau tout seul se dilate mais si on augmente la quantité d'oxygène dans le sang les capillaires, ce qu’ils ont tendance à faire spontanément c’est de se contracter. C’est un processus d’homéostasie de base : quand il y a trop d’oxygène, les capillaires se dilatent et quand il n’y a pas assez de désoxygène, les capillaires se contractent. Alors, quand on fait de l’hypercapnie, on augmente évidemment l'oxygénation du sang mais ça fait que la quantité de sang dans le cerveau va diminuer parce que les capillaires se contractent. Donc, la concentration en oxyhémoglobine va diminuer aussi, même s'il y a plus d’oxyhémoglobine à cause de la contraction il y en a moins ! Ce sont des mécanismes de contrôle, d’homéostasie.
Dans le graphique, l’axe des x représente le temps, le temps qui s’écoule après qu’on a fait l’hypercapnie et sur l’axe des y, c’est la quantité de photons qu’on récupère par rapport à la quantité envoyé. Si on récupère plus de photons à la sortie, ça veut dire qu’il y en a moins qui ont été absorbé. Ça veut dire qu’il y avait moins d’hémoglobine globalement, le volume sanguin était donc plus faible. C’est ce qu’on observe au cours du temps (axe x). L’augmentation de la courbe indique qu’il y a plus de lumière qui traverse, donc il y avait moins de sang dans le cerveau à la suite d’une hyperventilation.

Sur l’axe des X vous avec le temps (s) donc c'est une expérience d'à peu près 5 min, sur l’axe des y c’est le changement en concentration. Donc ici on va avoir des mesures de volume cérébral total donc est ce que ça absorber beaucoup ou pas et après en travaillant avec les différentes longueurs d'onde on peut essayer de différencier la concentration en oxyhémoglobine de la concentration en désoxyhémoglobine. Quelque chose qu’on ne peut pas faire avec l’IRMf. Ici, on peut vraiment séparer le total vs l’oxygène et désoxygène. Avec l’IRMf ce sont seulement des changements relatifs qu’on est capable de détecter. Donc, dans le graphique on peut voir que suivant la stimulation, le volume augmente. Ça ce sont nos petits capillaires qui se dilatent en réponse à l'augmentation de l’extraction d'oxygène à cause des cellules gliales (ou astrocytes). On peut voir que ça corrèle énormément à la concentration en oxy, ça anti-corrèle avec la concentration de déoxy relative et puis sinon en bas comme mesure contrôle. Le flux sanguin au niveau de la peau est complètement indépendant de ce qui se passe au niveau du cerveau. Ils auraient pu utiliser une région contrôle dans le cerveau aussi. Cette modulation vasculaire est extrêmement fine au niveau spatial non seulement elle se passe Au niveau du cortex en fait elle se passe au niveau des régions exacts impliqués dans la tâche au niveau du cortex frontal et même si on avait la résolution comme on ira fonctionnelle on pourrait distinguer ce qui se passe au niveau dernières différentes couches du cortex certain que ça cette modulation vasculaire spatialement elle est organisée de manière très fine. Oui,  il y a des gros canaux, des grosses veines, dans lequel on va avoir une accumulation des faits, mais au niveau des capillaires et des microcapillaires, le contrôle se passe de manière très très fin. C’est la fameuse réponse hémodynamique qu’on connait très bien. On a un principe physique : diffusion de la lumière + absorption sélective de lumière par différents composés chimiques. Principe physiologique : couplage neurovasculaire. C’est deux choses ensemble sont l’imagerie optique.
Ici, on peut voir des fluctuations périodiques qui vont suivre la respiration. Donc, on a le temps en secondes et si on regarde comme 20 secondes de signal étant donné que c’est de l'optique, on peut prendre plein de points de mesure et vraiment suivre notre signal de manière très fine. Tandis qu'en IRMf, pour prendre un point de mesure, vu qu’on fait la totalité du cerveau, ça peut nous prendre 1, 2 ou 3 secondes. Ici, on peut prendre un point de mesure toutes les millisecondes et on peut voir ces variations très rapides et notamment ses variations systématiques liées à la respiration. Donc, évidemment c'est des choses qu’en corrigeant, on les enlèverait. Dans quelques diapositives on va parler de paradigme fonctionnel où typiquement on va regarder des blocs d'activité, comme en IRMf, avec des durées similaires, parce qu'on regarde une réponse vasculaire. Donc, on s'intéresse à peu près au même phénomène temporel avec des blocs qui vont durer 10-20 secondes. Alors, ces fluctuations-là sont quasiment négligeables, mais reste qu'elles sont présentes. Ici, on peut facilement les voir et on peut facilement les enlever/les modéliser avec du filtrage. De plus, l'imagerie optique c'est très portable et très flexible de ce point de vue-là, mais malgré tout, ça reste sensible au mouvement. Ça ne veut pas dire qu'on ne peut pas avoir des artefacts de mouvement, il y a des gens qui utilisent l'imagerie optique dans le cadre de de l'exercice physique! Ce qui faut savoir c’est quand on bouge la tête de façon importante, ça va créer des artefacts de mouvement. C’est représenté ici, on voit une grande modification du signal (Motion Artifact) parce que le capteur et le récepteur se sont un petit peu déplacé. Alors, on ne mesure plus exactement la même zone du cerveau et ça crée des grands changements dans les mesures qu'on obtient.   
On va faire de la régression du filtrage et de la régression de facteurs de confusion sur les séries temporelles très similaires à ce qu’on fait en IRMf. On va aller essayer de détecter les pics de mouvement et les retirer.

Les 3 colonnes correspondent à des tâches différentes. La première colonne est une tâche d’opposition de doigts, donc c'est du contrôle moteur, ça va venir directement activer la région motrice primaire. Quand on bouge la main droite, on s’attends à une grosse activation à gauche. C’est effectivement ça qui se passe (blob rouge), une augmentation du sang oxygéné. Augmentation de l’activité neuronale -> augmentation du flux sanguin-> augmentation du volume sanguin-> augmentation concentration relative en oxyhémoglobine. Si on regarde du côté ipsilatéral, on s’attends à une activation beaucoup moins forte. Dans la 2ème colonne, c’est une tâche sensorielle. On va toucher la main droite du participant et au lieu d’activer de façon antérieur le cortex sensorimoteur, on vient activer postérieur au sillon central, dans le cortex sensoriel primaire. Dernière colonne, on vient stimuler le nerf médian au niveau du poignet. L’activation est moins forte mais observe le même phénomène que dans les 2 autres conditions. C’est une belle démonstration de la spécificité spatiale de la réponse. Le patron spatial est très similaire, mais moins fort au niveau sensoriel que moteur. Elles sont de part et d’autre du sillon centrale, ce ne sont vraiment pas les mêmes cortex. Cependant, en IRMf, on va très facilement distinguer ces deux cortex. Ici, on le voit moins, on voit la réponse, mais c’est sûr que la banane de diffusion de la lumière va passer à travers les 2 cortex et ça va être difficile de distinguer ce qui est en avant et en arrière du sillon central. Donc, voilà une limitation quant à la résolution spatiale de l’appareil. Pour ce qui est de la désoxyhémoglobine, c’est la même chose sauf dans le négatif.
Un avantage d’utiliser l’imagerie optique par rapport à l’IRMf, c’est qu’on peut distinguer les contributions de l’oxy et de la désoxyhémoglobine. Tandis qu’on voit un mélange des 2 dans l’IRMf.
Sur l’axe des X on a le temps et le bloc orange nous indique la durée de la stimulation et 4 courbes séparent l’hémoglobine (oxygénée, désoxygénée, controlatéral, ipsilatéral).
Pour la main droite et gauche, on a exactement les mêmes réponses, les courbes sont très similaires.
Un avantage de l’imagerie optique c’est le fait d’avoir beaucoup de points de mesure répétées et on a beaucoup de détails. On a une excellente résolution de mesure mais en termes de courbes, on observe quelque chose de très similaire avec l’IRMf, mais avec plus de points. La résolution temporelle intrinsèque de la méthode capture le même type de phénomène que l’IRMf, l’activité neuronale.

## Conclusions
La flexibilité expérimentale du dispositif.
    1. On combine l’imagerie optique à l’EEG
    2. Montage conçu pour les bébés, aucun risque pour la santé du bébé.
    3. Le système de contrôle est sur batterie et le participant peut bouger comme il le souhaite.
