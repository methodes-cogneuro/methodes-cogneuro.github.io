---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
(imagerie-optique-chapitre)=
# Imagerie optique

## Objectifs
L'imagerie optique cérébrale, encore appelée spectroscopie proche infrarouge fonctionnelle, est une technique qui permet de mesurer les corrélats vasculaires de l'activité cérébrale, de manière assez similaire à l'IRMf. En revanche, elle repose sur un principe physique très différent: la diffusion et l'absorption de la lumière dans les tissus cérébraux. Ses limites et faiblesses sont aussi bien distinctes de l'IRMf.

```{figure} imagerie_optique/fnirs.jpg
---
width: 600px
name: fnirs-fig
---
Système d'imagerie optique [NTS gowerlabs](https://www.gowerlabs.co.uk/nts). Image par Elisenicolegray tirée de [wikimedia](https://commons.wikimedia.org/wiki/File:Blonde_fNIRS_lady.jpg) sous licence [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0).
```

Les objectifs spécifiques de ce chapitre sont :
 * Principes physiques et physiologiques de l'imagerie optique.
 * Acquisition et traitement d'images en imagerie optique.
 * Applications de l'imagerie optique en neuroscience cognitive.

## Principes physiques et physiologiques

### Lumière infrarouge et tissus biologiques
```{code-cell} ipython 3
:tags: ["hide-input"]

from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")

# Youtube
HTML('<iframe width="560" height="315" src="https://www.youtube.com/embed/61rWjVkpgh0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>')
```

La lumière pénètre et diffuse au travers des tissus biologiques. Cela peut être observé facilement, par exemple en plaçant une lampe de poche derrière votre main. Votre main est en partie transparente et la lumière peut la pénétrer. Certains tissus vont plus absorber la lumière que d'autres, et permettre de voir le genre de tissus présent à l’intérieur de notre main. Mais quel genre de tissus exactement? cela va dépendre du genre de lumière... La lumière proche infra-rouge est intéressante de ce point de vue, car elle est particulièrement absorbée par l'hémoglobine. La vidéo ci-dessus permet ainsi d'observer assez clairement la vascularisation de la main avec de la lumière (et une caméra) proche-infrarouge. Karl von Vierordt en 1876 avait déjà pu remarquer qu'il était possible d'observer la diminution d'oxyhémoglobine dans la main avec cette technique, en limitant l'arrivée de sang dans la main au moyen d'une ligature. L'imagerie optique cérébrale repose aussi sur les propriétés physiques de la lumière proche infrarouge dans les tissus biologiques.

### Spectre d'absorption des tissus
```{figure} imagerie_optique/spectre_hemoglobine.png
---
width: 600px
name: spectre-hemoglobine-fig
---
Niveau d'absorption de la lumière par l'oxy- (HbO2) et la désoxyhémoglobine (HbR, notée Hb sur la figure), en fonction de la longueur d'onde. La région proche infrarouge (NIR, near infra-red) est indiquée. Image tirée de [Abtahi et al. (2017)](https://doi.org/10.3390/healthcare5020020) sous licence [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0).
```
Ce diagramme représente quelles longueurs d'ondes de la lumière sont absorbées par l'oxy- et la désoxy-hémoglobine, donc HbO2 (hémoglobine oxygénée en rouge) et HbR (hémoglobine non oxygénée en bleu). On peut voir qu'il y a des longueurs d'onde pour lesquelles le niveau d'absorption HbO2 et HbR est très différent. Par exemple, à 700 nanomètres la lumière est plus absorbée par HbR, alors qu'à 900 nanomètres la lumière est plus absorbée par HbO2. Si on peut mesurer le niveau d'absorption dans le sang pour ces deux couleurs, en les comparant, on va pouvoir essayer de dissocier les concentrations en HbO2 et HbR.  Un autre point important: ces longueurs d'onde sont très peu absorbées par l'eau, et la lumière proche infra-rouge va bien pénétrer dans les tissus biologiques. Donc, juste en étudiant la quantité d'absorption de deux longueurs d'onde proche infrarouge dans le cerveau, on va pouvoir quantifier le contenu en HbO2 et HbR! En pratique, on mesure comment l'absorption change au cours du temps à chacune des deux longueurs d'onde, et on convertit ces deux mesures en variations de concentration d'HbO2 et d'HbR, au moyen d'une relation physique appelée loi de Beer-Lambert modifiée. Mais reste à savoir comment on peut faire cette mesure de manière localisée dans une petite région du cerveau.

### Diffusion de la lumière
```{figure} imagerie_optique/nir-diffusion.png
---
width: 300px
name: nir-diffusion-fig
---
Mesure localisée dans le cerveau en imagerie optique. Un *émetteur* de lumière proche infrarouge est appliquée sur le scalp. Cette lumière est diffusée dans le cerveau. Après avoir traversé une petite portion de tissus cérébraux, elle va être émise de nouveau à la surface du scalp, et mesurée par un *récepteur* Image tirée de [Abtahi et al. (2017)](https://doi.org/10.3390/healthcare5020020) sous licence [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0).
```
Dans le premier exemple que l'on a vu, avec une lampe qui illumine la main, la lumière traverse notre main en ligne droite depuis la lampe, jusqu'à notre œil. Si l'on applique le même principe au cerveau, la lumière va traverser l'ensemble des tissus, et on ne pourra pas identifier quelle région du cerveau a absorbé la lumière. On ne pourra jamais faire des images avec cette méthode.
Mais si on envoie de la lumière dans le cerveau, une partie de cette lumière va se diffuser, selon un principe de marche aléatoire. Si on regarde le scalp autour de l'émetteur de lumière, la lumière diffusée va pouvoir être mesurée. Plus on s'éloigne de l'émetteur, plus la lumière qui ressort a pénétré profondément dans les tissus. Si on va trop près, la lumière diffusée n'aura pas pénétré jusqu'au cerveau. Si on va trop loin, presque toute la lumière aura été absorbée en chemin, et ce qui ressort sera trop faible pour être mesuré. Mais si on met notre récepteur à la bonne distance de l'émetteur (environ 3 cm chez l'adulte), cette lumière aura traversé une région spécifique du cerveau, en forme de banane, qui atteint le premier ou les deux premiers centimètres de cortex.

Le trajet de la lumière dépend aussi de l'épaisseur du scalp et du crâne, et de la forme des plis du cortex, qui varient d'une personne à l'autre. Un même montage, placé au même endroit sur la tête, ne mesure donc pas exactement la même région du cerveau chez deux participants.

```{admonition} Attention!
:class: caution attention
:name: nirs-warning
Seules les régions cérébrales proches du scalp pourront être mesurées précisément avec l'imagerie optique. Pour mesurer la lumière qui a pénétré très profondément dans le cerveau, il faudra que celle-ci traverse de nombreux tissus, et on n'aura pas une mesure spécifique des tissus profonds.
```

### Couplage neurovasculaire
On a maintenant vu le principe physique qui nous permet de mesurer la concentration en HbO2 et HbR dans une région (superficielle) du cerveau. Le principe physiologique sur lequel repose l'imagerie optique est le même que pour l'IRMf, c'est-à-dire le **couplage neurovasculaire**. Vous pouvez vous référer à la [section](#couplage-neurovasculaire-irmf-section) du chapitre sur l'IRMf pour plus de détails. Brièvement, l'activité post-synaptique des neurones entraîne une demande métabolique locale, et l'extraction d'oxygène dans les micro-capillaires. En réponse, le flux sanguin local augmente, bien au-delà de ce que cette consommation requiert: paradoxalement, la concentration en HbO2 augmente, et celle en HbR diminue, à proximité des populations de neurones activés. C'est ce phénomène de couplage neurovasculaire qu'on mesure à la fois en IRMf et en imagerie optique.

Les deux techniques ne mesurent pourtant pas la même chose. Le signal BOLD de l'IRMf dépend surtout de la désoxyhémoglobine (voir la [section](#signal-bold-section) sur le signal BOLD), et ne permet pas de séparer les deux formes de l'hémoglobine. L'imagerie optique mesure séparément les variations de concentration en HbO2 et en HbR.

## Acquisition et traitement


### Recalage avec l'anatomie
```{figure} imagerie_optique/fiducials.png
---
width: 800px
name: fiducials-fig
---
Points de repère sur la tête et alignement imagerie optique / IRM. Haut à gauche: installation d'un montage d'imagerie optique sur un jeune participant. Haut à droite: différents points de repères standards sont identifiés sur la tête du participant. Bas: ces mêmes points de repère sont manuellement identifiés sur une reconstruction 3D du visage en IRM. Ces points de repères sont utilisés pour recaler la position des émetteurs / récepteurs d'imagerie optique avec l'IRM structurelle du participant. Figure tirée de [LLoyd-Fox et al. (2014)](https://doi.org/10.1117/1.nph.1.2.025006) sous licence [CC Attribution unported 3.0](https://creativecommons.org/licenses/by/3.0/).
```
Afin de localiser l'activité cérébrale mesurée, il est courant d'utiliser une IRM structurelle du participant de recherche. Il est alors important de pouvoir situer les émetteurs et récepteurs de lumière proche infrarouge par rapport aux différentes régions du cerveau. Deux techniques principales sont utilisées. La première technique consiste à utiliser certains points de repères anatomiques sur la tête du participant, tel qu'illustré dans la {numref}`fiducials-fig`. Ces points de repère sont aussi visibles dans l'IRM structurelle, et permettent de mettre en correspondance les deux types de mesure. La deuxième approche consiste à utiliser un système de **neuronavigation**, comme par exemple ce [système](https://www.neurocaregroup.com/brainsight-nirs) qui utilise des caméras pour mettre en correspondance la position des émetteurs et récepteurs de lumière proche infrarouge avec l'IRM structurelle.

### Montage
```{code-cell} ipython 3
:tags: ["hide-input", "remove-output"]
# Importe les librairies
import os.path as op
import numpy as np
import matplotlib.pyplot as plt
from itertools import compress
import mne

# Charge les données
fnirs_data_folder = mne.datasets.fnirs_motor.data_path()
fnirs_cw_amplitude_dir = op.join(fnirs_data_folder, 'Participant-1')
raw_intensity = mne.io.read_raw_nirx(fnirs_cw_amplitude_dir, verbose=True)
raw_intensity.load_data()
subjects_dir = op.join(mne.datasets.sample.data_path(), 'subjects')

# Améliore les annotations du jeu de données
raw_intensity.annotations.set_durations(5)
raw_intensity.annotations.rename({'1.0': 'CTL',
                                  '2.0': 'Gauche',
                                  '3.0': 'Droite'})
unwanted = np.nonzero(raw_intensity.annotations.description == '15.0')
raw_intensity.annotations.delete(unwanted)

# Visualise le montage
# La génération de la figure est désactivée lors de la compilation du livre:
# le rendu 3D fait planter le noyau. L'image fnirs-montage.png a été produite
# une fois en exécutant ces lignes, et n'est plus régénérée.
#brain = mne.viz.Brain(
#    'fsaverage', subjects_dir=subjects_dir, background='w', cortex='0.5')
#brain.add_sensors(
#    raw_intensity.info, trans='fsaverage',
#    fnirs=['channels', 'pairs', 'sources', 'detectors'])
#brain.show_view(azimuth=20, elevation=60, distance=400)
#brain.save_image('imagerie_optique/fnirs-montage.png')
```

```{figure} imagerie_optique/fnirs-montage.png
---
width: 600px
name: fnirs-montage-fig
---
Un montage d'émetteurs/récepteurs en imagerie optique cérébrale. La position des émetteurs de lumière est indiquée en rouge, la position des récepteurs est indiquée en noir. Chaque trait blanc relie un émetteur à un récepteur et forme un canal; le point milieu de chaque canal, qui sert à localiser la mesure, est indiqué en orange. Cette figure a été générée par du code python adapté d'un [tutoriel](https://mne.tools/stable/auto_tutorials/preprocessing/70_fnirs_processing.html#sphx-glr-auto-tutorials-preprocessing-70-fnirs-processing-py) de la librairie [MNE python](https://mne.tools) (cliquer sur + pour voir le code), et est distribuée par L. Bellec sous licence [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).
```

On voit dans la {numref}`fnirs-montage-fig` un montage composé de plusieurs émetteurs et récepteurs. Chaque paire émetteur–récepteur forme un **canal**: la lumière mesurée a traversé les tissus situés sous le segment qui les relie, et le point milieu de ce segment (en orange) sert à localiser la mesure. Différents montages existent, qui varient aussi bien par le nombre d'émetteurs et de récepteurs que par leur disposition. Ces montages vont donner plus ou moins de résolution spatiale et de couverture du cortex, et seront aussi plus ou moins dispendieux et complexes à installer selon le nombre de capteurs utilisés. Entre les canaux, il n'y a aucune mesure: une région du cortex qui n'est sous aucun canal est tout simplement invisible.

### Artefact de mouvement

```{code-cell} ipython 3
:tags: ["hide-input", "remove-output"]
from mne.preprocessing.nirs import (optical_density,
                                    temporal_derivative_distribution_repair)
raw_od = optical_density(raw_intensity)
new_annotations = mne.Annotations([31, 187, 317], [8, 8, 8],
                                  ["Movement", "Movement", "Movement"])
raw_od.set_annotations(new_annotations)
plt_od = raw_od.plot(n_channels=15, duration=400, show_scrollbars=False)
plt_od.savefig("imagerie_optique/fnirs-od.png")

raw_tddr = temporal_derivative_distribution_repair(raw_od)
plot_tddr = raw_tddr.plot(n_channels=15, duration=400, show_scrollbars=False)
plot_tddr.savefig("imagerie_optique/fnirs-tddr.png")

# Make figure
from matplotlib import pyplot as plt
import imageio
fig1, ax = plt.subplots(1, 2, figsize=(12, 6), dpi=200,
                        subplot_kw={'xticks': [], 'yticks': []})
fig1.subplots_adjust(hspace=0.3, wspace=0.05)
im = imageio.imread("imagerie_optique/fnirs-od.png")
ax.flat[0].imshow(im, interpolation='antialiased')
ax.flat[0].set_title('Signal brut')
im = imageio.imread("imagerie_optique/fnirs-tddr.png")
ax.flat[1].imshow(im, interpolation='none')
ax.flat[1].set_title('Après correction de mouvement')

fig1.savefig(
  "imagerie_optique/fnirs-motion-fig.png",
  dpi=300,
  bbox_inches="tight",
  pad_inches=0
)
```
```{figure} imagerie_optique/fnirs-motion-fig.png
---
name: fnirs-motion-fig
width: 800px
---
Corrections des artefacts de mouvement dans une acquisition d'imagerie optique. Figure générée par du code python adapté d'un [tutoriel MNE python](https://mne.tools/stable/auto_examples/preprocessing/fnirs_artifact_removal.html#sphx-glr-auto-examples-preprocessing-fnirs-artifact-removal-py) par L. Bellec sous licence [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).
```
Tout comme les données d'IRMf, les données d'imagerie optique sont sensibles au mouvement. Il est possible de tirer parti de l'excellente résolution temporelle de l'imagerie optique (typiquement une dizaine de mesures par seconde, contre une image toutes les une à deux secondes en IRMf) pour identifier des changements brusques dans le signal, indicateurs de mouvement. Ces changements brusques peuvent alors être corrigés, tel qu'illustré dans la {numref}`fnirs-motion-fig`.

### Filtrage
```{code-cell} ipython 3
:tags: ["hide-input", "remove-output"]

# Une même échelle pour les deux panneaux, pour que la comparaison soit honnête
scalings = dict(hbo=1e-6, hbr=1e-6)

# Reconstruction des données d'hémoglobine
raw_od = optical_density(raw_intensity)
raw_tddr = temporal_derivative_distribution_repair(raw_od)
raw_haemo = mne.preprocessing.nirs.beer_lambert_law(raw_tddr, ppf=6)
plot_hemo = raw_haemo.plot(n_channels=15, scalings=scalings,
              duration=400, show_scrollbars=False)
plot_hemo.savefig('imagerie_optique/fnirs-hbo2.png')

# filtrage des données
raw_haemo = raw_haemo.filter(0.05, 0.7, h_trans_bandwidth=0.2,
                             l_trans_bandwidth=0.02)
plot_hemo = raw_haemo.plot(n_channels=15, scalings=scalings,
              duration=400, show_scrollbars=False)
plot_hemo.savefig('imagerie_optique/fnirs-filtered.png')

# Make figure
from matplotlib import pyplot as plt
import imageio
fig1, ax = plt.subplots(1, 2, figsize=(12, 6), dpi=200,
                        subplot_kw={'xticks': [], 'yticks': []})
fig1.subplots_adjust(hspace=0.3, wspace=0.05)
im = imageio.imread("imagerie_optique/fnirs-hbo2.png")
ax.flat[0].imshow(im, interpolation='antialiased')
ax.flat[0].set_title('Signal hémodynamique')
im = imageio.imread("imagerie_optique/fnirs-filtered.png")
ax.flat[1].imshow(im, interpolation='none')
ax.flat[1].set_title('Après filtrage')

fig1.savefig(
  "imagerie_optique/fnirs-filtrage-fig.png",
  dpi=300,
  bbox_inches="tight",
  pad_inches=0
)

```

```{figure} imagerie_optique/fnirs-filtrage-fig.png
---
name: fnirs-filtrage-fig
width: 800px
---
Filtrage des données HbO2 pour éliminer les dérives lentes et les battements cardiaques. Les deux panneaux utilisent la même échelle (2 µM). Les bandes de couleur indiquent les évènements de la tâche. Figure générée par du code python adapté d'un [tutoriel MNE python](https://mne.tools/stable/auto_tutorials/preprocessing/70_fnirs_processing.html#sphx-glr-auto-tutorials-preprocessing-70-fnirs-processing-py) par L. Bellec sous licence [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).
```
Un autre point commun avec l'IRMf est la présence de différentes sources de bruit, qui peuvent être réduites par des techniques de filtrage. Ces techniques sont plus efficaces en imagerie optique qu'en IRMf, car on dispose d'une meilleure résolution temporelle. Il est possible de supprimer les dérives lentes, comme on l'avait vu en IRMf, mais aussi d'éliminer les battements cardiaques (environ une fois par seconde), ce qui est difficile à faire en IRMf, où le TR est généralement supérieur à 1 seconde.

Une source de bruit propre à l'imagerie optique ne peut pas être éliminée par filtrage. Avant d'atteindre le cerveau, puis en ressortant, la lumière traverse le scalp, qui est lui aussi irrigué par des vaisseaux sanguins. Les variations de circulation sanguine dans le scalp, par exemple quand la pression artérielle change, se mélangent donc au signal cérébral, dans les mêmes fréquences que la réponse hémodynamique. Pour les mesurer, on ajoute au montage des **canaux courts**, où le récepteur est placé à moins d'un centimètre de l'émetteur: la lumière n'y a pas le temps d'atteindre le cerveau, et ces canaux ne mesurent que le scalp. Ce signal peut ensuite être retiré des canaux habituels.

## Application en neuroscience cognitive

### Réponse hémodynamique
```{code-cell} ipython 3
:tags: ["hide-input", "remove-output"]
reject_criteria = dict(hbo=80e-6)
tmin, tmax = -5, 15
events, event_dict = mne.events_from_annotations(raw_haemo)

epochs = mne.Epochs(raw_haemo, events, event_id=event_dict,
                    tmin=tmin, tmax=tmax,
                    reject=reject_criteria, reject_by_annotation=True,
                    proj=True, baseline=(None, 0), preload=True,
                    detrend=None, verbose=True)

evoked_dict = {'Droite/HbO': epochs['Droite'].average(picks='hbo'),
               'Droite/HbR': epochs['Droite'].average(picks='hbr'),
              }

# Renomme les canaux pour corriger la fréquence dans ch_name
for condition in evoked_dict:
    evoked_dict[condition].rename_channels(lambda x: x[:-4])

color_dict = dict(HbO='#AA3377', HbR='b')

plot_hrf = mne.viz.plot_compare_evokeds(evoked_dict, combine="mean", ci=0.95,
                             colors=color_dict)
plot_hrf[0].savefig('imagerie_optique/fnirs-evoked.png')
```

```{figure} imagerie_optique/fnirs-evoked.png
---
width: 600px
name: fnirs-evoked-fig
---
Réponse HbO2 et HbR évoquée par un mouvement du doigt à `droite` (tapping), moyennée sur l'ensemble des canaux.
Cette figure est générée par du code python adapté d'un [tutoriel](https://mne.tools/stable/auto_tutorials/preprocessing/70_fnirs_processing.html#sphx-glr-auto-tutorials-preprocessing-70-fnirs-processing-py) de la librairie [MNE python](https://mne.tools) (cliquer sur + pour voir le code) et est distribuée par L. Bellec sous licence [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).
```
L'imagerie optique permet de réaliser des expériences cognitives similaires à ce que l'on peut faire en IRMf.
Dans la {numref}`fnirs-filtrage-fig`, on voit une série d'**évènements** qui ont été annotés.
Ces évènements sont de trois types: mouvement du doigt à `gauche`, mouvement du doigt à `droite` et condition de `contrôle`.
La figure ci-dessus présente la **réponse évoquée** par la condition `droite`: de petites fenêtres de signal allant de 5 secondes avant chaque événement à 15 secondes après chaque événement ont été extraites et moyennées.
Les données de l'ensemble des canaux ont aussi été moyennées.
Les mesures HbO2 et HbR ont en revanche été séparées.
On voit un profil caractéristique de réponse hémodynamique en HbO2.
Comme attendu, le HbR suit un profil inversé avec un pic plus tardif et beaucoup plus petit (en valeur absolue).

### Carte d'activation
```{code-cell} ipython 3
:tags: ["hide-input", "remove-output"]

times = np.arange(-3.5, 13.2, 4.0)
topomap_args = dict(extrapolate='local', res=50)
plot_epochs = epochs['Droite'].average(picks='hbo').plot_joint(
    times=times, topomap_args=topomap_args)
plot_epochs.set_dpi(400)

plot_epochs.savefig(
  "imagerie_optique/fnirs-activation-fig.png",
  dpi=300,
  bbox_inches="tight",
  pad_inches=0
)

```
```{figure} imagerie_optique/fnirs-activation-fig.png
---
name: fnirs-activation-fig
width: 800px
align: center
---
Réponse HbO2 évoquée par un mouvement du doigt à `droite`, pour chacun des 28 canaux. La petite tête en haut à gauche du graphe indique, par sa couleur, la position de chaque canal sur le scalp: deux groupes, un par hémisphère. Pour différents instants, une carte topographique (la tête vue de dessus, le nez en haut) indique le niveau d'activité évoquée, interpolé entre les canaux. Cette figure est générée par du code python adapté d'un [tutoriel](https://mne.tools/stable/auto_tutorials/preprocessing/70_fnirs_processing.html#sphx-glr-auto-tutorials-preprocessing-70-fnirs-processing-py) de la librairie [MNE python](https://mne.tools) (cliquer sur + pour voir le code), et est distribuée par L. Bellec sous licence [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).
```

La réponse évoquée par un mouvement du doigt à `droite` peut aussi être estimée indépendamment pour chacun des canaux. Il est ainsi possible de reconstruire une carte d'activité évoquée au cours du temps. En IRMf, ce type de carte est généralement résumé avec un seul paramètre d'amplitude de la réponse, mais la résolution temporelle supérieure de l'imagerie optique permet d'étudier la dynamique de la réponse vasculaire de manière plus fine.

Cette carte demande à être lue avec prudence. Les canaux ont été disposés au-dessus du cortex sensorimoteur des deux hémisphères, et tous présentent une réponse évoquée en HbO2, d'amplitude comparable à gauche et à droite. On ne voit donc pas, sur ces données d'un seul participant, une réponse nettement plus forte dans l'hémisphère gauche, qui commande la main droite. Par ailleurs, la carte est interpolée: elle attribue des valeurs à toute la surface comprise entre les canaux, y compris au centre de la tête, entre les deux groupes, où aucun canal ne mesure quoi que ce soit.


### Flexibilité expérimentale
```{figure} imagerie_optique/fnirs-high-altitude.jpg
---
width: 300px
name: fnirs-high-altitude-fig
---
Mesure de l'oxygénation cérébrale à haute altitude avec un système d'imagerie optique portatif (PortaLite, Artinis Medical Systems). Image tirée de [wikipédia](https://upload.wikimedia.org/wikipedia/commons/5/5b/Picture_of_NIRS_measurement_at_high_alltitude.jpg) sous licence [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en).
```
Une des grandes forces de l'imagerie optique par rapport à l'IRMf est la flexibilité expérimentale. Un système d'imagerie optique est aussi beaucoup moins coûteux à acheter et à faire fonctionner qu'un IRM, et certains sont portatifs. Même si les artefacts de mouvement peuvent être un problème, il est possible d'enregistrer l'activité d'un athlète en mouvement ({numref}`fnirs-high-altitude-fig`). Il est aussi possible d'enregistrer l'activité du cerveau d'un [musicien qui pratique son instrument](https://upload.wikimedia.org/wikipedia/commons/transcoded/3/33/Imaging-Brain-Function-with-Functional-Near-Infrared-Spectroscopy-in-Unconstrained-Environments-Video2.ogv/Imaging-Brain-Function-with-Functional-Near-Infrared-Spectroscopy-in-Unconstrained-Environments-Video2.ogv.480p.vp9.webm), ou bien encore de [deux musiciens qui jouent ensemble](https://upload.wikimedia.org/wikipedia/commons/transcoded/b/bd/Imaging-Brain-Function-with-Functional-Near-Infrared-Spectroscopy-in-Unconstrained-Environments-Video3.ogv/Imaging-Brain-Function-with-Functional-Near-Infrared-Spectroscopy-in-Unconstrained-Environments-Video3.ogv.360p.vp9.webm) (une technique appelée hyper-scanning). Même s'il est possible de [jouer du violoncelle dans un IRM](https://ieeexplore.ieee.org/document/6688614), ce type d'expérience est bien plus facile de mise en oeuvre avec l'imagerie optique. Cette technique est aussi plus simple à mettre en oeuvre chez des sujets qui ont des difficultés à rester immobiles, comme les très jeunes enfants ({numref}`fiducials-fig`).

## Conclusions
Dans ce cours, nous avons vu les principes de l'imagerie optique. Plus précisément, nous avons vu:
- Comment la lumière proche infrarouge permet de mesurer le couplage neurovasculaire.
- Comment l'utilisation d'un montage d'émetteurs et de récepteurs sur le scalp permet d'acquérir des signaux couvrant une portion du cerveau.
- Comment les signaux d'imagerie optique sont nettoyés pour améliorer la qualité.
- Comment on peut générer une carte d'activation en réponse à une série d'événements.

## Exercices
```{admonition} Exercice 1
Vrai/faux. Les données d’imagerie optique sont …
 1. Des données plus interprétables que l’IRMf.
 2. Des données plus flexible à recueillir que l’IRMf.
 3. Des données moins chères à recueillir que l’IRMf.
 4. Des données qui donnent une image détaillée de l’activité neuronale dans le cortex.
```

```{admonition} Exercice 2
Vrai/faux. On souhaite enregistrer l’activité cérébrale d’un patient en imagerie optique au niveau du cortex sensorimoteur.
 1. On peut positionner précisément l’activité au niveau du scalp du participant.
 2. On peut positionner précisément l’activité au niveau du cerveau du participant.
 3. La qualité des données dépendra du positionnement des capteurs et émetteurs.
 4. Une IRM T1 individuelle du sujet permet d’améliorer la localisation de l’activité dans le cerveau.
```

```{admonition} Exercice 3
Choisissez la bonne réponse. En imagerie optique cérébrale, la lumière proche infrarouge…
 1. peut traverser les tissus biologiques sur une longue distance, même d’un bout à l’autre de la tête.
 2. diffuse dans les tissus biologiques et peut être observée à proximité de la source.
 3. est absorbée par la désoxyhémoglobine et l’oxyhémoglobine.
 4. réponses 2 et 3.
 5. réponses 1, 2 et 3.
```

```{admonition} Exercice 4
Choissez la bonne réponse. En imagerie optique, la résolution spatiale …
 1. est identique chez tous les sujets, si on utilise le même appareil pour l’acquisition.
 2. dépend du placement des émetteurs et récepteurs.
 3. correspond au profil de diffusion de la lumière dans les tissus.
 4. réponses 2 et 3.
 5. réponses 1, 2 et 3.
```

```{admonition} Exercice 5
On souhaite mesurer l’activité du cortex moteur durant la vie quotidienne d’une personne âgée, de manière longitudinale tous les jours pour une semaine. Citez un avantage, une limitation et une considération éthique pertinents pour l’utilisation de l’imagerie optique pour ce projet.
```

```{admonition} Exercice 6
On souhaite étudier l’activité spontanée du cerveau chez un bébé de 3 semaines. On utilise un montage en imagerie optique, et on mesure l’activité au repos dans les bras d’un parent.
Le bébé bouge la tête de manière soudaine, est ce que la résolution temporelle de l’imagerie optique va présenter un avantage par rapport à l’IRMf pour tenir compte de ces mouvements?
On observe des fluctuations lentes d’activité au niveau du cortex temporal. Est ce que la résolution temporelle de l’imagerie optique va présenter un avantage par rapport à l’IRMf pour caractériser ces fluctuations?
```

```{admonition} Exercice 7
Pour répondre aux questions de cet exercice, lisez d'abord l'article *Distinct hemispheric specializations for native and non-native languages in one-day-old newborns identified by fNIRS* de Vannasing et collaborateurs (disponible en [accès libre](https://doi.org/10.1016/j.neuropsychologia.2016.01.038) sous licence CC-BY-NC-ND et publié dans le journal Neuropsychologia en 2016. Les questions suivantes requièrent des réponses à développement court.
- Quelle technique de neuroimagerie est utilisée? S'agit-il d'une technique structurelle ou fonctionnelle?
- Quel montage d'imagerie optique a été utilisé?
- Quels types de stimuli ont été utilisés?
- Quel contrôle de qualité a été appliqué sur les données?
- Comment est générée l'activité évoquée?
```

## Contributeurs

🤔 Contenu | 💻 Code | 🧩 Quizz | 👀 révision du texte

::::{grid}
:::{grid-item}
![Lune Bellec](https://avatars.githubusercontent.com/u/1670887?v=4?s=100)
[Lune bellec](https://github.com/lunebellec) 🤔💻🧩👀
:::

:::{grid-item}
![Eddy Fortier](https://avatars.githubusercontent.com/u/72314243?v=4?s=100)
[Eddy Fortier](https://github.com/e-fortier)
👀
:::

:::{grid-item}
![Xanthy Lajoie](https://avatars.githubusercontent.com/u/90349544?v=4?s=100)
[Xanthy Lajoie](https://github.com/Xanthylajoie)
🤔👀
:::

:::{grid-item}
![François Lespinasse](https://avatars.githubusercontent.com/u/38385719?v=4?s=100)
[François Lespinasse](https://github.com/sangfrois)
👀
:::

:::{grid-item}
![Marie-Eve Picard](https://avatars.githubusercontent.com/u/77584086?v=4?s=100)
[Marie-Eve Picard](https://github.com/me-pic)
👀
:::

:::{grid-item}
![Andréanne Proulx](https://avatars.githubusercontent.com/u/65092948?v=4?s=100)
[Andréanne Proulx](https://github.com/anproulx)
👀
:::

::::
