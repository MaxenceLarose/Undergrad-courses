from fractions import Fraction
from sympy.physics.hydrogen import Psi_nlm
from sympy import Symbol
from sympy import integrate, conjugate, pi, oo, sin, cos
import time
start_time = time.time()

# Création des variables utilisées pour les calculs
r = Symbol("r", real=True, positive=True)
phi = Symbol("phi", real=True)
theta = Symbol("theta", real=True)
Z = Symbol("Z", positive=True, integer=True, nonzero=True)

# Passage des coordonnées sphériques aux coordonnées cartésiennes
jacobi = r**2*sin(theta)
x = r*sin(theta)*cos(phi)
y = r*sin(theta)*sin(phi)
z = r*cos(theta)

# Création de tous les états initiaux et finaux
n = 3
n_prime = 2
ini = []
fin = []
tot = 0
for i in range(0, n):
    for j in range(-i, i+1):
        ini.append([n, i, j])
        tot += 1

for i in range(0, n_prime):
    for j in range(-i, i+1):
        fin.append([n_prime, i, j])

# Calcul de la somme des normes au carré en itérant sur toutes les transitions possibles
# On crée d'abord les fonctions d'ondes propres Psi_nlm de l'atome d'hydrogène et on intègre sur tout l'espace.
# La somme est obtenue en multipliant le résultat des intégrales par leur complexe conjugué.
Somme = 0
for i in ini:
    for j in fin:
        fct = Psi_nlm(i[0], i[1], i[2], r, phi, theta, Z=1) * conjugate(Psi_nlm(j[0], j[1], j[2], r, phi, theta, Z=1))
        Moy_x = integrate(fct * jacobi * x, (r, 0, oo), (phi, 0, 2 * pi), (theta, 0, pi))
        Moy_y = integrate(fct * jacobi * y, (r, 0, oo), (phi, 0, 2 * pi), (theta, 0, pi))
        Moy_z = integrate(fct * jacobi * z, (r, 0, oo), (phi, 0, 2 * pi), (theta, 0, pi))
        Somme += Moy_x*conjugate(Moy_x)+Moy_y*conjugate(Moy_y)+Moy_z*conjugate(Moy_z)

Taux_transition = Fraction(1, tot)*(Fraction(1, n_prime**2) - Fraction(1, n**2))**3*Fraction(1, 6)*Somme

print("États initiaux :", ini)
print("États finaux :", fin)
print("Taux de transition moyen =", Taux_transition, "=", float(Taux_transition))
print("Temps de calcul = %s secondes" % (time.time() - start_time))
