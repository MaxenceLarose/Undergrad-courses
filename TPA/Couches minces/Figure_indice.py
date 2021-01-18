import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

filename = "Data/Indice_Longueur_1.txt"
filename2 = "Data/Indice_Longueur_2.txt"
filename3 = "Data/Indice_Longueur_3.txt"

x1 = np.loadtxt(filename, usecols=0)
y1 = np.loadtxt(filename, usecols=1)
x2 = np.loadtxt(filename2, usecols=0)
y2 = np.loadtxt(filename2, usecols=1)
x3 = np.loadtxt(filename3, usecols=0)
y3 = np.loadtxt(filename3, usecols=1)


def test(x, a, b):
    return a + b/x**2


param1, param_cov1 = curve_fit(test, x1, y1)
param2, param_cov2 = curve_fit(test, x3, y3)
print("Coefficients:")
print(param1)
print("Covariance of coefficients:")
print(param_cov1)

print("Coefficients2:")
print(param2)
print("Covariance of coefficients2:")
print(param_cov2)

H1 = np.arange(450, 800, 1)
H2 = np.arange(450, 800, 1)


def f_1(x):
    return param1[0] + param1[1]/x**2


def f_2(x):
    return param2[0] + param2[1]/x**2


pltTransExp = plt.errorbar(x1, y1, linestyle="", marker="o", markersize=9, capsize=3, ecolor='k',
                           markeredgecolor='k', markerfacecolor='k', label='Couche de PbCl2 #1')
pltTransExp2 = plt.errorbar(x2, y2, linestyle="", marker="o", markersize=9, capsize=3, ecolor='k',
                           markeredgecolor='k', markerfacecolor='r', label='Couche de PbCl2 #2')
pltTransExp3 = plt.errorbar(x3, y3, linestyle="", marker="o", markersize=9, capsize=3, ecolor='k',
                           markeredgecolor='k', markerfacecolor='w', label='Couche de PbCl2 #3')
plt.plot(H1, f_1(H1), '--', color='k',
         label ='Profil de Cauchy (PbCl2 #1): '' ' r'$n(\lambda) = 2.526 + \frac{6.182 \times 10^4}{\lambda^2}$')
plt.plot(H2, f_2(H2), '--', color='b',
         label ='Profil de Cauchy (PbCl2 #3): '' ' r'$n(\lambda) = 2.298 + \frac{9.202 \times 10^4}{\lambda^2}$')
#plt.xlim([0, 11.5])
#plt.ylim([0, 1400])
plt.yticks(fontsize=16)
plt.xticks(fontsize=16)
plt.xlabel("Longueur d'onde $\lambda$ [nm]", fontsize=18)
plt.ylabel("Indice de réfraction", fontsize=18)
plt.legend(fontsize=13)
#plt.grid()
plt.minorticks_on()
fig = plt.gcf()
fig.set_size_inches(12, 7)
fig.savefig('IndiceVsLongueurOnde.pdf', bbox_inches = 'tight', dpi=600)
plt.show()