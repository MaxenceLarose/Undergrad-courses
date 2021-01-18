<img src="Figs\ul_logo.png" alt="ul_logo" align="left" width="200" height="100"/>

<br/><br/><br/><br/>
<h3><center> Cahier de laboratoire </center></h3><br/><br/><br/><br/><br/>
    
<center> Travaux pratiques avancés (GPH-3000) </center> <br /><br/><br/><br/><br/><br/>

<center> présenté à </center>
<center> Simon Rainville et Michel Piché </center> <br /><br/><br/><br/><br/><br/>

<center> par </center>
<center> Maxence Larose (111 188 447 - maxence.larose.1@ulaval.ca) </center>
<center> Pierre-Olivier Janvier (111 187 987 - pierre-olivier.janvier.1@ulaval.ca) </center><br /><br/><br/><br/><br/><br/><br/>

<center> Automne 2020 </center><br/><br/><br/>

<div style="page-break-after: always;"></div>

# Expérience 3 : Techniques de fabrication de couches minces

Protocole de laboratoire [disponible ici](https://sitescours.monportail.ulaval.ca/contenu/sitescours/036/03613/202009/site121785/modules809962/module1031410/page2793327/bloccontenu2672865/Couches%20minces_GPH_A2019.pdf?identifiant=fd52206f43175102140b8b8fb4df72afeaa552c1). pour la version 2019 et [ici](https://sitescours.monportail.ulaval.ca/contenu/sitescours/036/03613/202009/site121785/modules809962/module1031410/page2793327/bloccontenu2672865/Couches_minces_mise_a_jour_A-2020.pdf?identifiant=7b189a49bd2e463a5a37956942037f1d4f4e7f70) pour les modifications 2020.

## Préparation

**Date de préparation :** 01 octobre 2020

**Date de l'expérimentation :** 01 octobre 2020

**But :** Comprendre le fonctionnement d'un système d'évaporation sous vide, de fabriquer des couches diélectriques et des couches métalliques ainsi que les caractériser.

**Objectifs spécifiques:**
- Se familiariser avec le fonctionnement d’un système de dépôt de couches minces par évaporation sous
vide.
- Caractériser le chauffage des bateaux d’évaporation.
- Fabriquer des couches minces diélectriques [PbCl$_2$] et des couches métalliques [Cu].
- Déterminer les conditions expérimentales de fabrication de couches minces : pression dans l’enceinte,
courant de chauffage, vitesse d’évaporation des substances, durée du dépôt...
- Mesurer en cours de fabrication la transmission optique des couches minces.
- Mesurer en cours de fabrication l'épaisseur des couches minces et le taux de variation d'épaisseur en
utilisant un instrument de mesure basé sur le principe d’un quartz oscillant.
- Mesurer la transmission spectrale des couches minces produites en utilisant un spectrophotomètre
informatisé.
- Caractériser le quartz oscillant servant à la mesure de l’épaisseur des couches minces.
- Déterminer les constantes optiques des couches minces diélectriques.
- Mesurer le coefficient d’absorption des couches minces métalliques.

**Matériel nécessaire:**
- Appareil NRC 3114 (comprenant une cloche à vide et un groupe de pompage)
- Système optique de mesure de la transmission des couches minces utilisant le faisceau d'un laser He-Ne
($\lambda$ = 632,8 nm)
- Système de mesure d'épaisseur EDWARDS FTM5 ("Film Thickness Monitor") fonctionnant sur le
principe de la variation de fréquence d'un quartz oscillant *
- Thermocouple et afficheur numérique OMEGA *
- Pico-ampèremètre KEITHLEY 485 *
- Oscilloscope numérique TEKTRONIX TDS-1002 *
- Convertisseur PICOTECH ADC-212 et micro-ordinateur *
- Multimètre numérique de type pince ampèremétrique TES 3090 ("clamp meter")

<div style="page-break-after: always;"></div>

**Texte de préparation : Résumé des Manipulations**

Tout d'abord, procéder à l'inspection des différentes composantes ou instruments utilisés. Premièrement, inspecter le groupe de pompage, repérer et comprendre le rôles des différentes composantes et noter la pression dans la cloche lors du vide. Deuxièmement, inspecter la cloche de l'évaporateur ainsi que ses périphériques tout en se familiarisant avec le processus de changement de substrats. On devrait repérer le circuit d'alimentationdes bateux d'évaporation, le couteau permettant la sélection des bateaux et si les bateaux contiennent la substance à évaporer. Troisièmement, inspecter l'instrumentation de mesurer. Pour ce faire, réaliser le branchement approprié en réalisant un schéma dans le cahier de laboratoire et s'assurer de connaître les paramètres caractérisants les couches minces à l'aide du tableau fourni en annexe du protocole. 

Ensuite, procéder à la fabrication des différentes couches minces. Premièrement, préparer le système à la fabrication de couches minces avec du PbCl$_2$. Il faut s'assurer que le cache est fermé, sélectionner le bateau AVANT, programmer le moniteur FTM5 pour du PbCl$_2$, noter l'écart de fréquence initial entre les quartz oscillants, sélectionner le mode du moniteur pour la plage d'épaisseur nécessaire, régler l'oscilloscope pour avoir un échelle de 0-100 mV à la «transmission optique», de 0-1 V à l'«épaisseur» et pour avoir une échelle de temps conforme aux directives du technicien et on prépare un tableau afin de prendre en note toutes les conditions de chauffage du bateau, soit le temps, le courant au primaire et secondaire ainsi que la température atteinte à chaque étape du chauffage. Deuxièmement, procéder au dépot d'une couche mince #1 (1200-1400 nm). Pour ce faire, chauffer le bateau avec un courant de 2 A (primaire), lorsque la température se stabilise augmenter le courant de 1 A toutes les 2 minutes et noter le courant au secondaire jusqu'à ce que la température atteinte soit un peu plus faible que la température de fusion.Lorsque la température désirée est atteinte, démarrer le balayage de l'oscilloscope et l'ascquisition de Picolog ainsi qu'ouvrir le cache. Lorsque l'épaisseur voulue est atteinte, remener le courant de chauffage à zéro, mettre fin au balayage de l'oscilloscope et à la prise de données dans Picolog. Afin de prendre les données requises, placer les curseurs à l'instant de l'ouverture du cache et de sa fermeture, double-cliquer sur $\textit{PRINT}$, noter la différence de fréquence des quartz compléter le tableau synthèse et mesurer la coordonnées des extrêmes de «Transmission,Épaisseur». Deuxièmement, on réalise le dépôt de la couche #2 (400-480 nm) en actionnant le mécanisme de changement de substrat et en réalisant les mêmes étapes réalisées lors du dépôt précédent. Troisièmement, on réalise les mêmes étapes pour la couche #3 (1300-1500 nm). Finalement, réaliser les préparations nécessaire  et procéder au dépôt de la couche #4 (18-25 nm) de Cu. Dans le cas du cuivre, un courant initial de 2 A  et une augmentation périodique de 2 A sont utilisés pour le chauffage. 

Finalement, en suivant les directives données sur place, réaliser une analyse de spectrophotométrie avec chaque lame pour $\lambda$ = $[400-800] nm$, imprimer les courbes de transmission obtenues, sauvegarder les données à l'ordinateur. Mesurer aussi la transmission optique @633 nm ainsi que les longueurs d'ondes au pics de transmission des différentes couches. Prendre le $\lambda$ des MIN et des MAX de transmission pour le PbCl$_2$.

**(Pour la version 2020, seulement les couches #1 et #2 seront réalisées pour le PbCl$_2$)**

## Réalisation



## Inspection du groupe de pompage
- Le groupe de pompage est inspecté, on remarque que la pression initiale dans la cloche à vide est de 6*10$^{-6}$ Torr.
- Les différentes composantes sont repérées et inspectées.

## Inspection de la cloche de l'évaporateur et de ses périphériques
- Les différentes composantes du circuit d'alimentation et ainsi que ses mécanismes sont observées. Les bateaux contiennent une quantité de substance à évaporer.
- Le fonctionnement du mécanisme de changement de substrat est observé et manipulé afin de se familiariser avec son fonctionnement
.

## Inspection de l'instrumentation de mesure
- Le tableau synthèse remis avec le protocole de laboratoire est étudié afin de connaître les différents paramètres des couches minces à prendre en note.

- L'instrumentation de prise de mesure est inspectée et un schéma du branchement électrique permettant la prise de données est réalisé. Ce schéma est illustré à la figure suivante
<img src="Figs\Schema_el.png" alt="ul_logo" align="center" style="zoom:30%"/>

<center>Figure 1: Schéma électronique du système de dépôt de couche mince. </center>


## Fabrication de couches minces diélectriques - PbCl$_2$

### Couche mince #1 [épaisseur ~ 1200 à 1400 nm de PbCl$_2$]
- Afin de réaliser le dépôt des couches minces, l'instrumentation est programmé. L'oscilloscope possède une plage de 0-1 V et la division verticale est ajustée à 200 mV/div. La plage horizontale de l'oscilloscope est aussi ajustée à 50 s/div sur une plage totale de 300 s.

- Ensuite, le FTM5 est programmé pour la substance à déposer et en fonction de la densité ainsi que de l'impédance acoustique du substrat. Pour le PbCl$_2$ utilisé : PbCl2 = 5.85 g/cm 3 et Z$_𝐴$  = 10.00*10 5 g/cm 2 s. Le mode choisi est le mode #22. Les paramètres décidés pour l'oscilloscope et le FTM5 sont décidés en fonction de l'épaisseur de la couche voulue ainsi que les caractérisitiques du substrat choisi.

- On s'assure que le cache est fermé et on place l'intérrupteur pour manière à sélectionner le bateau AVANT.

- L'écart intial fréquentiel entre les oscillateurs est noté et est de 14.38 kHz. On note aussi la transmission initiale le plaque de verre et la lecture du pico-ampèremètre. On obtient respectivement des 94 % et de 0.4166 mA.

- Un tableau de chauffage est préparé pour caractériser les paramètres du chauffage et de la plaque pendant celui-ci. Lors du chauffage, on augmente le courant primaire de 1 A à chaque 100 secondes, et ce, à partir de 2 A. Chaque intervalle de 100 seconde se déroule comme ceci. Tout d'abord, on ajuste le courant primaire et on prend en note sa valeur ainsi que celle du courant secondaire. Ensuite, on attend 100 secondes. À la fin du 100 secondes on prend en note la température détectée aux bateaux. Finalement, on augmente de le courant primaire de 2 A. Ce processus est répété jusqu'attend que, lors du prochain cycle de chauffage, la température atteinte devrait être celle visée pour le dépot de la couche mince.

|Temps [s]  | Courant primaire [A]  | Courant secondaire [A]  | Température [°C] |
|:---:  |:---:|:---:|:---:|
| 100   | 2   | 48  | 51  |
| 200   | 3   | 75  | 120 |
| 300   | 4   |97.2 | 218 |
| 400   | 5   | 115 | 328 |
| 500   | 5.5 | 126 | 389 | 

<center>TABLEAU 1 : Tableau de chauffage pour la plaque #1. </center>

- Lorsque la température voulue est atteinte (<450-480 °C), le cache est ouvert et avec le système de mesure d'épaisseur on peut s'assurer d'obtenir la bonne épaisseur. La valeur de la température, du courant primaire et du courant secondaire sont pris en note à l'ouverture du cache. Respectivement, ces valeurs sont de 422 °C, 5.8 A et 122.3 A. 

- Lorsque l'épaisseur voulue est obtenue, on ferme le cache ainsi que le courant d'alimentation des bateaux afin d'arrêter le processus de dépôt. À cette fermeture, la valeur de la température, du courant primaire, du courant secondaire, du taux de dépot, de la lecture au pico-mètre et l'épaisseur de la couche sont prises en note dans le tableau synthèse. On reprend aussi juste avant de retirer du système la plaque fabriquée.

- À titre d'exemple, les figures obtenues à l'aide de l'oscilloscope, du pico-ampèremètre et du système d'acquisition de données sont présentées aux figure 2 et 3 ci-dessous.

<img src="Figs\1a).jpg" alt="ul_logo" align="center" style="zoom:20%"/>

<center>Figure 2: Graphique 1 a) obtenu à l'aide de l'oscilloscope, soit la tension (épaisseur) en fonction du temps au canal 1 et la transmission en fonction du temps au canal 2. </center>

<img src="Figs\1b).jpg" alt="ul_logo" align="center" style="zoom:20%"/>

<center>Figure 3: Graphique 1 b) obtenu à l'aide du système d'acquisition de données et de l'ordinateur, soit la transmission en fonction du temps avec ses coordonnées clés identifiées. </center>



### Couche mince # 2 [épaisseur ~ 400 à 480 nm de PbCl$_2$]
- Afin de réaliser le dépôt des couches minces, l'instrumentation est programmé. L'oscilloscope possède une plage de 0-1 V et la division verticale est ajustée à 100 mV/div. La plage horizontale de l'oscilloscope est aussi ajustée à 25 s/div sur une plage totale de 175 s.

- Ensuite, le FTM5 est programmé pour la substance à déposer et en fonction de la densité ainsi que de l'impédance acoustique du substrat. Pour le PbCl$_2$ utilisé : PbCl2 = 5.85 g/cm 3 et Z$_𝐴$  = 10.00*10 5 g/cm 2 s. Le mode choisi est le mode #18. Les paramètres décidés pour l'oscilloscope et le FTM5 sont décidés en fonction de l'épaisseur de la couche voulue ainsi que les caractérisitiques du substrat choisi.

- On s'assure que le cache est fermé et on place l'intérrupteur pour manière à sélectionner le bateau AVANT.

- L'écart intial fréquentiel entre les oscillateurs est noté et est de 78.82 kHz. On note aussi la transmission initiale le plaque de verre et la lecture du pico-ampèremètre. On obtient respectivement des 94 % et de 0.3801 mA.

- Conaissant dorénavant le comportement du PbCl$_2$ à l'aide de la couche précédente, il n'est pas nécessaire de faire un tableau de chauffage. On répète seulement les étapes de chauffage de la plaque précédente pour le chauffage.

- Lorsque la température voulue est atteinte (<450-480 °C), le cache est ouvert et avec le système de mesure d'épaisseur, on peut s'assurer d'obtenir la bonne épaisseur. La valeur de la température, du courant primaire et du courant secondaire sont pris en note à l'ouverture du cache. Respectivement, ces valeurs sont de 411 °C, 5.5 A et 132.4 A. 

- Lorsque l'épaisseur voulue est obtenue, on ferme le cache ainsi que le courant d'alimentation des bateaux afin d'arrêter le processus de dépôt. À cette fermeture, la valeur de la température, du courant primaire, du courant secondaire, du taux de dépot, de la lecture au pico-mètre et l'épaisseur de la couche sont prises en note dans le tableau synthèse. On reprend aussi juste avant de retirer du système la plaque fabriquée.



### Couche mince # 2 [épaisseur ~ 1300 à 1500 nm de PbCl$_2$]

## Fabrication de couches minces métalliques – Le cuivre

### Couche mince # 4 [épaisseur ~ 18 à 25 nm de Cu]
- Afin de réaliser le dépôt des couches minces, l'instrumentation est programmé. L'oscilloscope possède une plage de 0-1 V et la division verticale est ajustée à 200 mV/div. La plage horizontale de l'oscilloscope est aussi ajustée à 25 s/div sur une plage totale de 175 s.

- Ensuite, le FTM5 est programmé pour la substance à déposer et en fonction de la densité ainsi que de l'impédance acoustique du substrat. Pour le Cu utilisé : PbCl2 = 8.94 g/cm 3 et Z$_𝐴$  = 20.20*10 5 g/cm 2 s. Le mode choisi est le mode #6. Les paramètres décidés pour l'oscilloscope et le FTM5 sont décidés en fonction de l'épaisseur de la couche voulue ainsi que les caractérisitiques du substrat choisi.

- On s'assure que le cache est fermé et on place l'intérrupteur pour manière à sélectionner le bateau ARRIÈRE.

- L'écart intial fréquentiel entre les oscillateurs est noté et est de 99.84 kHz. On note aussi la transmission initiale le plaque de verre et la lecture du pico-ampèremètre. On obtient respectivement des 94 % et de 0.4033 mA.

- On refait ensuite un tableau de chauffage afin de connaître le comportement du cuivre lorsque celui-ci chauffe et de pouvoir faire le dépôt de la couche. Il est important de surveiller de près et de réajuster le courant primaire au besoin dans le système lors du chauffage puisque le cuivre étant un très bon conducteur conduit le courant de manière différente en fonction de sa température puisque sa résistance augmente. Puisque le cuivre possède une température de fusion plus grande que le PbCl$_2$ on réalise le tableau de chauffage par intervalle de 2 A.
|Temps [s]  | Courant primaire [A]  | Courant secondaire [A]  | Température [°C] |
|:---:  |:---:|:---:|:---:|
| 100   | 2   | 47.3| 61  |
| 200   | 4   | 91.3| 221 |
| 300   | 6   |131.1| 861 |
| 400   | 7.8 |170  | 1170|

<center>TABLEAU 2 : Tableau de chauffage pour la plaque #3. </center>

- Lorsque la température voulue est atteinte (<1200-1600 °C), le cache est ouvert et avec le système de mesure d'épaisseur on peut s'assurer d'obtenir la bonne épaisseur. La valeur de la température, du courant primaire et du courant secondaire sont pris en note à l'ouverture du cache. Respectivement, ces valeurs sont de 1165 °C, 8.0 A et 176.2 A. 

- Lorsque l'épaisseur voulue est obtenue, on ferme le cache ainsi que le courant d'alimentation des bateaux afin d'arrêter le processus de dépôt. À cette fermeture, la valeur de la température, du courant primaire, du courant secondaire, du taux de dépôt, de la lecture au pico-mètre et l'épaisseur de la couche sont prises en note dans le tableau synthèse. On reprend aussi juste avant de retirer du système la plaque fabriquée.


## Spectrophotométrie
- Tout d'abord,  le système de spectrophotométrie est utilisé avec aucune lame à l'intérieur. Cela permet de trouver la réponse du système en transmission. Les données, coordonnées des pics et et valeurs des pics sont pris en note. Les données sont sauvegardées dans le fichier nommé «MLPO».

- Ensuite, les mesures réalisées pour le système à vide sont réalisées de noveau pour toutes les différentes lames fabriquées. Les données sont enregistrées dans les fichiers correspondant à la plaque. Donc, les données de la plaque #1 sont dans PB1310.csv, les données de la plaque #2 sont dans PB460.csv et les données de la plaque #3 sont dans CU15_7.csv

- À titre d'exemple, le spectre obtenue pour la plaque #1 est présenté à la figure #4.

<img src="Figs\1c).jpg" alt="ul_logo" align="center" style="zoom:20%"/>

<center>Figure 3: Graphique 1 c) obtenu à l'aide du logiciel lié au système de spectrophotométrie, soit la transmission en fonction de $\lambda$. </center>

PbCl2 = 5.85 g/cm$^3$ : Z$_A$ = 10.00*10$^5$g/cm$^2$s 

Cu = 8.93 g/cm$^3$ : Z$_A$ = 20.20*10$^{5}$g/cm$^2$s

|                                              |  Variables      |Unités|  #1     |  #2    |  #3    | 
|:-----------------------------------------    |:----------------|:-----|------   |------  |------  |
|Substance à évaporer                          |                 |      |PbCl$_2$ |PbCl$_2$|Cu      |      
|Épaisseur visée                               |                 |nm    |1360     | 450    |16.4    |      
|**AVANT LE CHAUFFAGE DU BATEAU D'ÉVAPORATION**|                 |      |         |        |        |      
|Mode du FTM5                                  |                 |#     |22       | 18     |6       |      
|Plage de l'épaisseur                          |                 |nm    |mod 1000 |1000    |mod 10  |      
|Écart de fréquence initial                    |$\Delta f_1$     |kHz   |14.38    |78.82   |99.84   |      
|Transmission optique initiale                 |$\tau_{initial}$ |%     |94       |94      |94      |      
|lecture Keithley                              |                 |mA    |0.4166   |0.3801  |0.4033  |      
|**À L'OUVERTURE DU CACHE**                    |                 |      |         |        |        |    
|Température                                   |T$_i$            |°C    |422      |411     |1165    |      
|Courant de chauffage au primaire              |I$_p$            |A     |5.8      |5.5     |8.0     |      
|Courant au secondaire                         |I$_S$            |A     |132.4    |122.3   |176.2   |      
|**À LA FERMETURE DU CACHE**                   |                 |      |         |        |        |      
|Taux de dépôt                                 |                 |nm/s  |5.4      |2.6     |0.1     |      
|Température                                   |T$_f$            |°C    |417      |412     |1154    |      
|Courant de chauffage au primaire              |I$_p$            |A     |60       |5.7     |8.0     |      
|Courant au secondaire                         |I$_S$            |A     |137.7    |122.0   |176.0   |      
|Transmission optique                          |$\tau_{final}$   |%     |62.56    |83.12   |36.67   |      
|lecture Keithley                              |                 |mA    |0.245    |0.297   |0.139   |      
|Épaisseur de la couche                        |e                |nm    |1352     |448     |16.4    |      
|Durée du dépôt                                |t                |s     |286      |169     |129     |      
|Oscilloscope [ Fig. # 1A, 2A,…]               |                 |#     |1a       |2a      |3a      |      
|Picolog [ Fig. #1B, 2B…..]                    |                 |#     |1b       |2b      |3b      |      
|**AVANT DE CHANGER DE SUBSTRAT**              |                 |      |         |        |        |      
|Épaisseur définitive                          |d                |nm    |1362     |450.7   |17.0    |      
|Transmission optique définitive               |$\tau$           |%     |59.35    |88.41   |39.93   |      
|lecture Keithley                              |                 |mA    |0.2324   |0.3159  |0.1489  |      
|Écart de fréquence final                      |$\Delta f_2$     |kHz   |78.82    |99.84   |101.0   |      
|Variation de fréquence                        |$\delta f$       |kHz   |64.44    |21.02   |1.16    |     
|Rapport K / fo2 du quartz oscillant           |d/$\delta f$     |nm/kHz|21.14    |21.4    |14.7    |      
|**SPECTROPHOTOMÉTRIE**                        |                 |      |         |        |        |      
|Figures [ # 1C, 2C,…]                         |                 |#     |1c       |2c      |3c      |      
|Tableaux [ # 1D, 2D,…]                        |                 |#     |1d       |2d      |3d      | 

<center>TABLEAU 3 : Tableau synthèse pour le dépôt de couche mince. </center>
