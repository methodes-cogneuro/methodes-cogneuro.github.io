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
(reproductibilite-controverses-chapitre)=
# Reproductibilité et controverses

Les objectifs de ce cours sont les suivants :
- Comprendre la crise de reproductibilité en neuroscience cognitive
- Comprendre certaines pratiques scientifiques douteuses qui participent
au manque de reproductibilité en neuroscience cognitive
- Connaître certains outils qui peuvent améliorer la reproductibilité

## La crise de reproductibilité

### Une crise?
Dans ces diapos, on voit des résultats d’une étude qui a été publiée dans
Nature en 2016. Ce journal est prestigieux, on verra que ce type de prestige
fait partie du problème. Ils ont fait un sondage dans le but de voir si, dans la
perception des professionnels dans la recherche, il y a une crise de
reproductibilité et si oui, laquelle. Donc le premier graphique qui est à
gauche c’est sur 1500 chercheurs. 52% disent qu’il y a une crise significative
et 38% disent qu’il y a une petite crise. En tout, 90% des chercheurs pensent
qu’il y a effectivement une crise de reproductibilité. Ainsi, on peut dire que la
perception de la crise de reproductibilité est une perception qui est assez
partagée, il y a vraiment une prise de conscience des difficultés reliées à la
reproductibilité. Ce sondage ne porte pas spécifiquement sur la
neuroimagerie, même pas sur les neurosciences, c’est sur la recherche
scientifique en générale. Mais, le domaine de la neuroimagerie est aussi
impacté que les autres domaines de la recherche, voire même un peu plus
car les problèmes qui amènent cette crise de reproductibilité sont exacerbés
en neuroimagerie.
Le manque de reproductibilité, c’est quoi ? C’est simplement que, quand on
lit un papier, est-ce qu’on peut vraiment faire confiance à ce qui est rapporté
? Les résultats peuvent parfois prendre plusieurs formes si on avait accès
aux données derrière ce papier. Est-ce qu’on serait capables de refaire les
analyses et arriver aux mêmes conclusions ? Une autre idée de
reproductibilité est la réplication, si je recrute de nouveaux sujets et que je
fais exactement ce que les autres chercheurs ont fait au niveau des outils
utilisés et les analyses effectuées, est-ce que je vais trouver les mêmes
résultats ? Ce sont les deux grandes idées de la reproductibilité :
1. Refaire exactement les résultats sur les données d’un papier
2. Répliquer les résultats avec des données indépendantes  
Donc, quand on demande aux gens c’est quoi qui amène cette crise de
reproductibilité, les gens listent une série de problèmes. Si on regarde le
graphique, les raisons sont listées de haut en bas par rapport à ce que les
gens jugent comme le plus important dans la crise. En fait, on voit en haut,
que dans les raisons les plus fréquemment mentionnées par les chercheurs
on retrouve la pression à publier et la publication sélective (les gens publient
seulement ce qui fonctionne bien) ainsi que la puissance statistique limitée.
C’est notre top 3.
Tout en bas de l’échelle, on a la raison « pas de chance ».  Tout au long du
cours, on a parlé d’erreur statistique, d’erreur de famille, de taux de fausse
découverte, etc. Ces techniques-là cherchent toutes à quantifier et contrôler
des faux positifs. Intuitivement, les gens se disent qu’on contrôlant pour les
faux positifs à l’aide de statistiques rigoureuses, j’augmente la probabilité
d’être capable de répliquer la découverte. Et donc, si on ne réplique pas,
c’est du a de la malchance. Dans la communauté de recherche, le fait d’avoir
pas de chance c’est le facteur le moins important dans la crise de
reproductibilité. Les gens pensent que le taux de faux positifs n’est pas
quelque chose de central dans cette crise. C’est plein d’autres facteurs
méthodologiques et dans une certaine mesure, sociologiques, qui
contribuent à cette crise.
Avant de rentrer dans les détails de la crise, on doit savoir ce qu’est générer
des connaissances et des découvertes scientifiques.

### Le cycle des découvertes
```{figure} ./reproductibilite/researchcycle_original.png
---
width: 800px
name: researchcycel-original-fig
---
Cette figure illustre le cycle des découvertes scientifiques, selon l'approche de la méthode scientifique décrite par [Karl Popper](https://fr.wikipedia.org/wiki/Karl_Popper#Philosophie_des_sciences). Figure adaptée d'un travail original par [scriberia](https://info.scriberia.com/contact-us) dans le cadre du livre [The Turing way](https://the-turing-way.netlify.app) sous licence [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/), DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807). La figure adaptée par P. Bellec est elle-même disponible sous licence [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).
```
Pour formaliser le processus de génération de connaissances en sciences, on va se référer à la théorie de [Karl Popper](https://fr.wikipedia.org/wiki/Karl_Popper#Philosophie_des_sciences), et la façon dont elle est implémentée dans la plupart des communautés de recherche. Ce processus devrait être un cercle vertueux (on l’espère). Nous allons commencer avec les publications. Les publications ce sont les connaissances qui ont été accumulées par d’autres, donc on va les lire et on va apprendre. Et en fonction de ça, on va commencer à essayer de comprendre le monde qui nous entoure et faire des hypothèses sur des
choses qu’on ne connait pas encore. On va ensuite concevoir notre étude
(devis de recherche : nombre de participants, groupes, tests statistiques) et
faire une prédiction quant aux résultats qu’on va obtenir. Une fois mon
protocole élaboré, il est temps d’aller recueillir les données. Ensuite, on les
analyse et je sais ce que je vais faire car j’avais déjà déterminé les tests lors
de l’élaboration de mon protocole. Ensuite, j’interprète les résultats. Ça, c’est
le plan. Si les choses allaient comme ça, ça ne serait pas si pire. Comme on
utilise des statistiques rigoureuses dans ce plan, on ne génère pas trop de
faux positifs, et donc on fait des découvertes scientifiques avec un petit peu
de bruit, mais dans une quantité raisonnable. Ça, c’est la théorie. En
pratique, ce n’est pas pareil.

### Découverts scientifiques: hacked

#### Publication
Donc, redémarrons depuis nos publications. À sa gauche, on voit la
publication sélective et à sa droite, le biais de publication. La publication est
un de problèmes les plus importants identifiés dans le sondage vu plus tôt.
Cela signifie que l’on ne publie pas les résultats lorsqu’ils ne sont pas
positifs. Quand on regarde ce que publie un laboratoire de recherche,
souvent, ça représente une fraction de ce qui est essayé. On a quand même
de plus en plus de laboratoires qui publient des résultats négatifs. Malgré
cela, ce n’est pas tout qui se retrouve publié.
Ensuite, quand on lit la littérature, on est rarement complètement objectifs.
On va avoir des biais. Un de ces biais est que si l’article est publié dans
Nature, par exemple, il sera considéré comme plus important. En réalité,
beaucoup des articles qui vont avoir un vrai impact ne seront pas publiés
dans des journaux de haut prestige. On a ainsi un biais cognitif par rapport
aux articles que l’on juge comme importants en lien avec leur lieu de
publication.
Ensuite, on élabore nos hypothèses sur la base des papiers qu’on a lu dans
la littérature.

#### Rapport sélectif
Ensuite, dans la conception de l’étude, on ne s’intéresse qu’aux positifs. On
s’intéresse rarement a la taille d’effet ou quand on le fait c’est avec des
modèles qui sont irréalistes ou trop simplistes. Cela veut dire que, même si
on implémente notre étude et qu’il y a quelque chose à trouver, y’a une
chance qu’on ne le trouve pas. Ça aussi, c’était dans le top 3 des problèmes
cités par les gens.

##### p-hacking
Ensuite, une fois qu’on a fait notre conception de l’étude, si on voit que nos
résultats ne correspondent pas à nos attentes, on pourrait se demander si on
a commis une erreur ou peut être qu'on n'a pas choisi la manière la plus
optimale. Cette approche qui consiste à essayer de venir revisiter la manière
dont analyse des données qu'est-ce qu'on n'a pas trouvé ce qu'on cherchait
ça s'appelle le p-hacking, le hacking du petit p. En neuroimagerie il y a plein
de manières de faire du p-hacking, à peu près n'importe quoi qu'on veuille
montrer on n'aura pas trop de problème à démontrer. Il y a 2 autres façons
standards pour améliorer nos résultats. Le premier c'est le contrôle de
qualité sélectif. On va éliminer des personnes de notre échantillon même si
elles ont passées le recrutement et étaient dans le bon groupe si leur
présence dans ce groupe a un effet négatif sur les résultats.  

##### Texas sharp shooter
Ce terme représente une image de tire à la carabine. Pour être bon tireur, ce qu’on peut faire c’est
tirer dans un mur et dessiner la cible autour du trou de balle a posteriori.
Ainsi, on aura tiré exactement au milieu de la cible. L’idée, c’est de redéfinir
les groupes après avoir réalisé que nos groupes initiaux ne permettaient pas
d’identifier l’effet désiré.
Une autre forme de p-hacking qui relève un peu de la publication sélective
est le biais de confirmation. On ne va que rapporter ce qui collait avec nos
hypothèses et, si d’autres hypothèses sont infirmées, nous allons faire
comme si nous ne les avions jamais eu.

#### HARKing
Le dernier phénomène de hacking pour la méthode scientifique c’est le
« HARKing ». Le terme HACK est un acronyme en anglais pour les termes
« Hypothesis after results are known ». Dans cette forme de hacking, on
émet nos hypothèses après avoir eu nos résultats. En fait, c’est une forme
encore plus extrême du biais de confirmation.
Au final, ce cercle vicieux fait en sorte qu’au final, on ne peut pas faire
confiance aux résultats qu’on trouve dans la littérature. Cela veut dire que
les nouveaux chercheurs partent d’une vision biaisée de ce qui se fait dans
la littérature.

## Reproducibilité et neuroimagerie
On va maintenant voir quels problèmes s’appliquent directement à la
neuroimagerie et comment certains problèmes de reproductibilité
spécifiques peuvent ressortir lors de l’utilisation de logiciels en
neuroimagerie.

### Degrés de liberté en recherche
Le premier problème qui est exacerbé en neuroimagerie est le nombre
d’Analyses qu’il faut faire ainsi que le nombre de choix qu’il faut faire en lien
avec ces analyses. Ceci est relié au problème de p-hacking dont on a discuté
plus tôt. Ainsi, toutes les possibilités d’analyses permettent aux chercheurs
d’aller faire ressortir l’effet qu’ils désirent observer d’une façon ou d’une
autre. Cette vaste sélection d’analyses est le résultat de dizaines de
paramètres modifiables qui sont impliqués dans ces analyses. Une étude a
tenté de systématiquement changer des choix de paramètres d’analyse pour
savoir quels résultats ils pouvaient obtenir. En bout de ligne, ils ont obtenu
près de 7000 chaines de traitement qui pouvaient être exécutées. Ensuite,
l’équipe a essayé différents seuils statistiques ce qui a généré près de 35
000 cartes d’activation. Ceci représente la variété des résultats qu’il est
possible d’obtenir en utilisant un simple contraste d’images IRMf. On parle
aussi de Multiverse, dans le sens ou l’histoire statistique peut changer
complètement avec une seule petite modification dans le choix des
paramètres d’analyse. Dans le cas des images d’IRM, on a tellement plus de
données et tellement plus d’analyses a faire que le problème de Multiverse
est d’autant plus prononcé comparativement aux analyses statistiques
traditionnelles.
On voit sur l’image ici que les régions qui présentent la plus haute moyenne
sont aussi les régions qui ont la plus grande variabilité dans les données,
même que l’amplitude de la variation est plus grande que l’amplitude de la
moyenne. Cela suggère qu’il y a beaucoup de variabilité sur les cartes finales
par les différents choix analytiques choisis. Dans ce cas, les changements de
paramètres ont été fait plutôt systématiquement et les gens dans la vraie vie
ne jouent pas autant avec les paramètres.

### Logiciels d'analyse
Maintenant, imaginons qu’on fait les analyses dans un des multiples logiciels
ci bas. Si les résultats escomptés ne sont pas obtenus avec un des logiciels,
on pourrait aller faire les mêmes analyses avec un autre logiciel et obtenir
des résultats différents.
Donc à droite on a les logos des 3 logiciels principaux, AFNI, FSL et SPM. Par
ailleurs, il y a plein de versions de SPM. La première version utilisée de
manière large est la version 95, après il y a eu 96, 99, SPM8 et SMP 12. En
plus, chaque version de SPM a eu des versions mineures qui ne sont pas ici.
En fait, ce qu’il faut retenir, c’est que ce qui a été expliqué en lien avec le
choix des analyses s’applique aussi au choix du logiciel d’analyse utilisé en
IRM. Même si on fait des choix comparables d’analyses dans les différents
logiciels on va se retrouver avec des variations.
Donc une étude de Bowring a tenté de prendre un jeu de données public et
des cartes d’activation qui ont été générées dans un article et ils ont essayé
de reproduire la carte d’Activation de l’article avec les 3 logiciels suivants :
FSL, AFNI, SPM. Les colonnes qu’on voit ici c’est 3 jeux de données différents,
en bas on a la carte d’activation qui a publiée par le groupe dans l’article
original et ce qu’on a dans chaque ligne au-dessus c’est ce qui a été obtenu
avec ces données à l’aide des 3 logiciels. Si on se concentre sur le premier
jeu de données à gauche, on voit que finalement on voit des activations au
niveau du cingulaire antérieur et de l’orbitofrontal ventral et une activation
négative au niveau du cortex cingulaire postérieur. Avec FSL, on retrouve le
même genre d’Activation mais avec des positions et des amplitudes
différentes. Des nouvelles activations ressortent au niveau occipital et au
niveau sous cortical qui ne sont pas là dans la carte d’’activation publiée.
Pour SPM, l’amplitude et la position des activations sont variables
comparativement a l’original. Tant au niveau qualitatif que quantitatif, la
cohérence de ces 4 cartes d’activation est assez faible. C’est une belle
illustration, on voit qu’il y a un impact assez important du logiciel qu’on
utilise pour faire les cartes, ce qui en dit gros sur la reproductibilité. Même
avec les mêmes données, seul le logiciel utilisé pour les analyses peut avoir
un impact important sur les résultats finaux des analyses. Quand on parlait
de p-hacking et du fait qu’on a plein d’étapes qui peuvent être modifiées, le
logiciel utilisé s’insère dans ce problème.

### Environnement de travail
De plus, les gens ont l’habitude de tenir pour acquis que peu importe
l’environnement ou on fait un calcul mathématique, on va obtenir le même
résultat. En effet, si on calcul 4+6 dans Windows, sur mac os ou sur une
calculatrice, le résultat donnera toujours 10. Or, les ordinateurs ne font pas
vraiment des calculs, ce qui change tout. Ils font des approximations avec un
nombre fini de chiffres après la virgule. Parfois, quand les ordinateurs font
des calculs complexes, il y a plusieurs façons de les implémenter. En
pratique, quand on regarde n’importe quelle méthode un peu complexe, il
est possible qu’on ait des différences entre les logiciels et les ordinateurs. Un
papier a regardé l’impact de la version de Mac OS sur les résultats d’une
analyse de morphométrie faite avec Freesurfer. Il y a différentes analyses
rapportées dans ce papier. Ce qu’on a sur ce graphique ce sont différentes
régions générées par Freesurfer. Dans ces barres-là, on a 3 versions de iOS X
(versions majeures et versions mineures). On voit la différence entre les
différentes versions de Mac en utilisant le même logiciel. On voit des
changements de 10% au niveau du cortex enthorinal seulement en fonction
du logiciel du système d’exploitation ! Malheureusement, l’environnement de
travail peut impacter la reproductibilité des résultats. Ce n’est pas propre à
la neuroimagerie mais c’est particulièrement problématique car on a de
grosses chaines de traitement et nos méthodes ne sont pas développées par
des gens qui s’y connaissent en traitement numérique, donc les gens ne sont
pas conscients des variations normales qui peuvent être causées par
l’utilisation d’environnements variables.

### Tailles d'effet
Une autre erreur qu’on voit particulièrement en neuroimagerie c’est
d’interpréter une différence significative comme une différence importante.
Une différence significative signifierait que les populations étudiées sont
complètement différentes. Par exemple, on trouve que les amygdales des
personnes sur le spectre de l’autisme est plus petite que pour les gens
neurotypiques. Cela signifie que la différence de la moyenne des
distributions est différente, pas que tous les individus du groupe des gens
ayant un TSA ont une amygdale plus petite que les gens neurotypiques.
Malheureusement, beaucoup de chercheurs et de professionnels ont
tendance à faire ce genre de conclusion. Une manière d’aller voir la taille de
la différence est en regardant le d de Cohen. Un d de Cohen de 0.1 serait ce
qu’on va trouver si on remarque une différence significative entre nos
moyennes de groupe, tel qu’illustrer avec l’exemple tes TSA plus tôt. Un d de
Cohen de 0.79 décrirait un effet de groupe immense, ou le score de tous les
membres d’un groupe est inférieur au score de tous les membres de l’autre
groupe. Or, si on a un N très grand, même avec un d de Cohen de 0.1, on va
avoir un p de 0.000001. Il est important de comprendre que malgré la
significativité de la différence de groupe, le p ne nous dit rien quant à
l’importance de cette différence. Le vocabulaire est très important a
comprendre, car beaucoup de gens vont dire qu’il y a une forte différence en
raison du p, alors que cette valeur ne nous dit rien au sujet de la taille
d’effet. En fait, ce qu’on doit retenir, c’est que si on score significatif n’a pas
de taille d’effet, elle n’a pas de raison d’être répliqué. Pour répliquer un effet,
il doit être significatif et fort. En neuroimagerie surtout, on fait beaucoup de
tests statistiques alors on se retrouve souvent avec des p qui sont très
faibles. La majorité des papiers ne rapportent même pas les tailles d’effet,
alors au final, personne ne regarde si l’effet est fort. Or, cette question est
très importante car la taille de la différence a un impact sur la
reproductibilité

### Méthodes incomplètes
Une autre chose importante à mentionner sont les méthodes incomplètes.
Cette image a été faite par @redpenblackpen, un artiste de McGill. Il publie
des petits dessins sur le monde universitaire. Celui-ci est très intéressant. Le
rez de chaussé représente le papier publié. On a une maison bien propre et
bien rangée. On va lire le papier et tout est carré et tout est rigoureux.
Parfois, on a du matériel supplémentaire qui est un document qui est moins
regardé par les reviewers, contenant des vieilles affaires et du matériel qui a
été utilisé pour le projet mais qui n’est pas essentiel dans le papier principal.
C’est un peu plus le bazar là-dedans on voit parfois que beaucoup plus de
choses ont été analysées que ce qui a été présenté dans le papier. Ce qui est
intéressant c’est le 2e sous-sol, ou on voit le vrai travail avec les tentacules
multicolore et la pagaille. En réalité, des tonnes de choses ont été essayées,
certaines choses pas terminées et d’autres oui mais oubliées. Au final,
l’auteur lui-même serait incapable lui-même de se souvenir de tout ce qui a
été essayé dans le processus du projet. De plus, la complexité des étapes
d’analyse en neuroimageries rend encore plus difficile de se souvenir et de
comprendre ce qui a été fait. Parfois, le numéro du logiciel utilisé n’est
même pas rapporté dans le papier et est enfoui loin dans la 2e cave. Ce que
cela veut dire, c’est que l’article publié nous donne une idée très peu
détaillée et très peu complète de ce qui a été fait. En fait, si les gens ne
partagent pas leur code et peur processus complet, il sera pratiquement
impossible de répliquer les résultats obtenus, justement en raison de la
profondeur de la 2e cave.

## Des solutions

### Études pré-enregistrées
Solutions permettant de répondre à la crise de la reproductibilité
La première idée, serait de modifier la manière dont on publie les articles. Un
des problèmes dans le cercle présenté au départ, c’est qu’il y a un temps
phénoménal entre l’élaboration des hypothèses et la publication en plus de
ne pas avoir de publication des résultats négatifs. Une manière d’éliminer ça,
c’est la publication des hypothèses et des plans d’analyse. Cela permet aux
reviewers de critiquer la conception de l’étude avant qu’elle soit terminée,
donc permettrait les modifications à priori si nécessaire. De plus, si les
résultats ne collent pas aux hypothèses, ce ne serait pas grave car l’article
serait déjà accepté. Il existe des articles préenregistrés, ou des registered
recall. C’est comme un article normal, il manque seulement les résultats et
la discussion. Une fois que les gens se sont mis d’accord quant a la méthode,
l’article est accepté peu importe les résultats. Cela ne veut pas dire qu’on ne
peut pas présenter des nouvelles analyses auxquelles on n’avait pas pensé
avant. Celles-ci seront alors présentées comme exploratoires comme il se
devrait, plutôt que confirmatoires comme c’est souvent le cas dans les
articles dont la méthode n’est pas acceptée et publiée d’avance., ce qu’on
appelle le HARKing. Ce type d’approche ne colle pas avec tout ce qu’on
souhaiterait publier. Ce ne fonctionne pas vraiment bien avec le travail
méthodologique, non plus avec les analyses plus exploratoires. Par contre,
pour les articles qui suivent la démarche traditionnelle, cela fonctionnerait
bien et répondrait à beaucoup des problèmes vus au début de ce cours.

### Code
Une autre solution serait d’apprendre à coder. Automatiser les analyses
permet de les rendre plus facile pour quiconque de les reproduire. Il peut y
avoir des erreurs dans le code, mais elles peuvent être vues et réparées
avec des traces. Les analyses qui ne reposent pas sur du code représente un
obstacle majeur à la reproductibilité.

### Partage de code
Ensuite, partager ce code est un peu anxiogène. Souvent, les gens sont
réticents a rendre public le code utilisé pour générer un article. Comme c’est
une partie critique du travail de recherche, ça vaut la peine d’apprendre a le
faire comme il faut et de le partager pour aider à réduire le problème de
reproductibilité. Beaucoup de gens qui utilisent Github, une plateforme qui
permet de partager le code et aussi de partager les modifications qui y sont
faites avec le temps. En fait, la principale personne qui bénéficie de la
publicisation de son code est la personne qui le publie, car si le projet évolue
dans le temps il y a traces de ce qui a été fait sur cette plateforme. Le
monstre du 2e sous-sol est alors un peu moins caché et un peu moins
inconnu pour vous et pour les personnes qui vous lisent à la suite de la
publication. De plus en plus, on s’attend que les scripts d’analyse soient
rendus publics lors de la publication des papiers.

### Partage de données
Une autre solution est de partager les données. Cela facilite la vie des
laboratoires car 1 an et 2 ans après avoir publié un papier, il est possible
qu’on ne se souvienne même plus ou se trouvent les données et quelle
version des données qui a été utilisée. Le partage de celles-ci rend plus facile
de se relire et de retrouver nos traces. Malheureusement, ce n’est pas facile
de rendre nos données publiques. De plus en plus de gens poussent pour
rendre le partage de données plus commun et plus facile, mais ce n’est pas
encore fait.
Partager ses données c’est comme un spectre qui est représenté par ce
graphique. Sur l’axe des y on a à quel point c’est utilisable et sur l’axe des x
c’est a quel point c’est beaucoup de données et ça prend du temps a
préparer. En bas, on a les données ADNI ou HCP, des projets ou les gens
publient leurs données brutes et les données prétraitées. Ensuite, on a
d’autres personnes qui partagent uniquement leurs données brutes. Par la
suite, on a des gens qui partagent leurs cartes statistiques. Enfin, les
coordonnées des types d’activation est quelque chose que beaucoup de
gens partagent dans les articles et qui est très utile, bien que beaucoup
moins riche que les cartes elles-mêmes. Le jour ou on arrivera a partager nos
données systématiquement avec nos articles on va avoir de grandes
améliorations au niveau de la reproductibilité.

### Partage d'environnement
Ensuite, on a des outils qui permettent de partager notre environnement de
travail. Une initiative qui est bien appréciée est neurodebian, qui est une
version de Linux qui vient préinstaller avec un appstore pour la
neuroimagerie. On peut installer directement les logiciels et les systèmes
d’opération. Ainsi, quelqu’un qui veut reproduire votre environnement
pourrait le faire. Il y a aussi les containers qui permettent de garder tout
l’environnement de travail sur un seul fichier, cela fonctionne sur Linux et il y
a des manières de le faire fonctionner sur Mac et sur Windows. C’est
beaucoup utilisé pour la programmation Web, et la communauté scientifique
a commencé à l’utiliser pour améliorer la reproductibilité.

### Bonnes pratiques
Certains articles se concentrent sur la formulation de « guides » de bonnes
pratiques pour différentes techniques et méthodes de recherche. Cela
permet de voir ce qui est le plus utile pour contrer la crise de reproductibilité
en fonction des méthodes les plus convoitées en neuroscience cognitive.
Une autre chose qui peut être faite est d’étudier la puissance statistique en
élaborant un projet pour savoir si on doit modifier la taille de notre
échantillon. Cela peut être fait avec différents logiciels et avec le site web
suivant : https://rpsychologist.com/d3/nhst/

### La méthode scientifique revisitée

### Vers une science généralisable

## Conclusions

## Exercices
