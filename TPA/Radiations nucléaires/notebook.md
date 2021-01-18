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

# Expérience 9 : Détecteurs de radiations nucléaires

Protocole de laboratoire [disponible ici](https://sitescours.monportail.ulaval.ca/contenu/sitescours/036/03613/202009/site121785/modules809962/module1031406/page2793319/bloccontenu2672849/GPH-3000-A2019-nucleaire.pdf?identifiant=a81a71c610f8c9cb6289d5c7bca0222496f5cf2c).

## Préparation

**Date de préparation :** 19 novembre 2020

**Date de l'expérimentation :** 19 novembre  2020

**But : Mesurer et étudier les différents types de vibrations trouvées dans une machine tournante** 

**Objectifs spécifiques :**
- Mesurer approximativement la distance que les particules $\alpha$ peuvent parcourir dans l’air avant d’avoir été freinées complètement.
- Calculer le nombre de particules a qui entrent dans la chambre d'ionisation.
- Étudier le comportement des signaux reçus par le compteur pour différentes sources.
- Mesurer le temps mort du détecteur Geiger
- Mesurer l'efficacité de détection du tube de Geiger
- Mesurer le temps de montée avec les scintillateurs
- Analyser spectralement le signal reçu par les scintillateurs

**Matériel nécessaire :**
- Sources radiatives
- Chambre à ionisation
- Source d’américium 241
- Compteur Geiger
- Oscilloscope
- Scintillateurs

**Schéma de montage :

<img src="Figs\Chambre.PNG" alt="ul_logo" align="center"   width="600" height = "300"/>

<center> FIGURE 1 : Montage de la chambre d'ionisation.  </center> <br/>

<img src="Figs\Compteur.PNG" alt="ul_logo" align="center"  width="600" height = "300"/>

<center> FIGURE 2 : Montage du compteur de Geiger-Müller.  </center> <br/>

<img src="Figs\Scintillateur.PNG" alt="ul_logo" align="center"  width="600" height = "300"/>

<center> FIGURE 3 : Schéma explicatif d'un scintillateur .  </center> <br/>

- S'assurer de recalculer la désintégration avec le temps de vie (ex : cobalt à 1 mCurie après 3 ans (Temps de demi-vie = 5 ans) va être rendu à genre 0.7 mCurie

## Réalisation
### Chambre à ionisation

1. Pour cette partie, il est important s'assurer de prendre les mesures en gardant la même position puisque la capacité du détecteur est sensible à son environnment physique. Par ailleurs, il est important de centrer la source sur le détecteur pour maximiser le courant.

2. Le montage de la figure 1 est utilisé et l'échelle est ajusté pour mesurer correctement la présence de particule $\alpha$. Le changement d'échelle modifie légèrement la valeur, avec une variation de $0.1 \times 10^{-9}~$A. L'échelle choisie pour mesurer la distance parcourue par les particules est de $0.01 \times 10^{-11}~$A.

3. On mesure approximativement la distance parcourue par les particules $\alpha$ dans l'air et on obtient $(5.2~\pm~0.1)~$cm.

4. La source est ensuite rapprochée le plus possible de la chambre et la tension est mesurée. L'échelle choisie est de $1 \times 10^{-9}~$A. Le courant mesuré est de $(9.2~\pm~0.2)\times~10^{-10}~$A. La quantité d'ionisation est donc de $\frac{(9.2~\pm~0.2)\times~10^{-10}}{1.602 \times 10^{−19}} = (5.7~\pm~0.1) \times 10^{9}~$ions/s, puisque à chaque fois qu’une molécule se fait ioniser, on obtient deux porteurs de charge dans le gaz : un positif et un négatif.

5. Sachant que l'énergie des particules $\alpha$ émise est de 5.4 MeV et qu'une particule $\alpha$ perd environ 35 eV à chaque ionisation, le nombre de particules $\alpha$ qui pénètrent dans la chambre est donnée par

$$
n_{\alpha} = \frac{n_{\text{ions}} \cdot E_{\text{perdu}}}{E_{\alpha}} = \frac{((5.7~\pm~0.1) \times 10^{9}~\text{ions/s}) \cdot 35~\text{eV}}{5.4 \times 10^{6}~\text{eV}} = (3.7~\pm~0.1) \times 10^{4}~\alpha / s
$$

6. La source est du Américium 241 avec un taux de désintégration de 10 $\mu$Ci. La référence de ce taux est le 1$^\text{er}$ septembre 1995. Le taux de désintégration est donc de $3.7~\times~10^{5}~s^{-1}$. On remarque que le taux trouvé précedemment correspond à seulement 10 % du taux théorique, donc à une efficacité de 0.1. Cette différence peut s'expliquer par le fait que le détecteur ne détecte probablement pas toutes les particules émises par la source. De plus, le taux de désintégration réel de la source est probablement plus faible que celui donné par le fabricant puisque la référence date de 1995!

7. Une source de rayons gamma est placée près de la chambre d'ionisation. On ne détecte aucune ionisation, ce qui est conforme à la théorie.

###  Compteur Geiger

#### Discrimination d’énergie

1. Le détecteur est mis sous tension et l’oscilloscope permet d'observer la forme des impulsions obtenues avec une source de radiation $\gamma$.

2. En remplaçant la source par une autre qui émet un rayonnement d’une énergie différente, il est possible d'analyser les signaux. Il n'est pas possible d'identifier la source du rayonnement puisque le gaz utilisé dans le détecteur est toujours le même. Ce type de détecteur n'est donc pas en mesure de mesurer l'énergie de radiations. Son utilisation est plutôt de détecter la quantité de raditions dans un environnement.

#### Temps mort

1. L’oscilloscope est branché à la sortie du Geiger. Celui-ci est ajusté pour capter un grand nombre d'impulsions. Il est possible de mesurer le temps minimum observable entre deux impulsions, soit le temps mort. On obtient une valeur de $(220~\pm~20)~\mu$s. Ce temps mort provient du temps nécessaire au gaz présent dans le détecteur Geiger pour se déexciter et être à nouveau prêt à s'ioniser, soit le temps de relaxation. La courbe de la réponse du gaz à l'impulsion (soit sa réponse impulsionnelle!) est exponentielle.

2. Ce temps impose une limite au nombre de radiations qui peuvent être détectées par seconde. On mesure que le nombre maximum de radiations est approximativement de 

$$
n_{\text{max}} = \frac{1 s}{220 \mu s} = 4545~\text{radiations/s}
$$

3. On voit que le terme de correction est d’autant plus important que le taux de comptage est élevé. Lorsque votre compteur indique un taux de radiations de 1000 par seconde, le taux réel est de 1282.

4. Il n'est pas possible d’éviter ce temps mort, mais l'utilisation d'un gaz qui possède une fonction de transfert avec un délai plus court pourrait réduire ce temps. Par ailleurs, il est possible d'ajuster les paramètres de l'acquisition afin de réduire l'impact de ce temps.

####  Efficacité de détection du tube Geiger

1. Le compteur Geiger est utilisé pour déterminer le bruit présent dans le laboratoire. Les sources de radiation sont toutes placées loin du compteur Geiger et le nombre d'impulsions est mesuré pendant 597.4 s. On obtient un nombre total d'impulsions de 502 impulsions. Il est important de se rappeler que Le nombre d’impulsions doit être ajuster pour considérer le temps mort. Le nombre d'impulsion réel est donc de 502.09?

2. Une source de radiation de est utilisée et le nombre d’impulsions est mesuré pendant la même période de mesure qu’en 1. Un nombre d'impulsions minimum de 1111 est nécessaire pour avoir une erreur statistique maximale de 3 %. Le temps de comptage correspondant à un tel nombre d'impulsions est de 597.4 s.

3. Les incertitudes correspondent à l'écart-type d'une distribution de poisson que l'on estime être de moyenne égale à 1111 points par 597.4 s. L'écart-type sur ces mesures est donc de $\frac{\sqrt(1111)}{1111} = 0.03$ donc de 3 %. Il est important de se rappeler que Le nombre d’impulsions doit être ajuster pour considérer le temps mort. Le nombre d'impulsion réel est donc de 1111.45?

5. Mesurer l’angle solide sous-tendu par le compteur à partir de la source. L’angle solide correspond au rapport entre l’aire de la section rectangulaire du compteur et l’aire d’une sphère dont le rayon correspond à la distance entre la source et le détecteur. La hauteur du compteur est de $1.8~\pm~0.1~$cm et sa hauteur est de $7.0~\pm~0.1~$cm. L'aire de la section est donc de $12.6~\pm~0.2~\text{cm}^2$. La distance entre la source et la détecteur est de $20.0~\pm~0.5~$cm. L'angle est donc de $0.63~\pm~0.03~$stéradian. La source est à $5.3~\pm~0.1~$cm du sol et le centre du capteur est à $5.8~\pm~0.1~$cm du sol.

6. En se fiant aux données fournies par le fabriquant et le calcul fait en 1, il est possible de calculer le nombre de rayons qui frappent le compteur par unité de temps. Il est bien important de tenir en compte le temps de demi-vie de la source ainsi que sa date de fabrication. Les caractéristiques de la source sont d'ailleurs présentées ici :

<img src="Figs\Co-60.jpg" alt="ul_logo" align="center"   width="300" height = "300"/>

<center> FIGURE 4 : Co-60.  </center> <br/>

7. L’efficacité du compteur pourrait être calculée ici, mais sera réalisé dans le rapport de laboratoire.

### Les scintillateurs

1. L'émission spontannée d'électron par les métaux du tube photomultiplicateur peut entraîner l'apparition de bruit. Toutefois, de façon générale, le bruit sera beaucoup moins intense que les pics provenent des éléments radioactifs.

2. Le détecteur est mis en marche et en utilisant une source monoénergétique à proximité tel que du césium-137, les signaux à la sortie de l’amplificateur sont observés.

#### Étalonnage de l’analyseur spectral

1. Plusieurs éléments sont observés à la sortie de l'amplificateur :

| Élément  | Énergies des gammas émis | Pics observés |
|:---:|:---:|:---:|
| Cs  | 662 keV   | 301  |
| Sodium  | 1275 keV  | 232 annihilation 577  |
| Cobalt 60  | 1173 1332 keV | 533 - 605  |
| Bruit (Potassium 40)  | À déterminer  | 654 |

<center> Tableau 3  : Éléments radioactifs et leur pics observés.  </center> <br/>

2. Les traces de sortie de l'amplificateur sont enregistrées et seront utilisées dans le rapport pour tracer les figures liées au différentes sources radioactives.
