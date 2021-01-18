import numpy as np
import matplotlib.pyplot as plt


def polyfit(x, y, degree):
    results = {}

    coeffs = np.polyfit(x, y, degree)

    # Polynomial Coefficients
    results['polynomial'] = coeffs.tolist()

    # r-squared
    p = np.poly1d(coeffs)
    # fit values, and mean
    yhat = p(x)  # or [p(z) for z in x]
    ybar = np.sum(y) / len(y)  # or sum(y)/len(y)
    ssreg = np.sum((yhat - ybar) ** 2)  # or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = np.sum((y - ybar) ** 2)  # or sum([ (yi - ybar)**2 for yi in y])
    results['determination'] = ssreg / sstot

    return results


filename = "Data/EpaisseurVsOrdre.txt"

x1 = np.loadtxt(filename, usecols=0)
y1 = np.loadtxt(filename, usecols=1)
y2 = np.loadtxt(filename, usecols=2)

x2 = np.loadtxt(filename, usecols=3, max_rows=3)
y3 = np.loadtxt(filename, usecols=4, max_rows=3)

x_regression = np.arange(0, 11, 0.01)
x_reg = np.arange(0, 3, 0.01)
a = polyfit(x1, y1, 1)
z = np.polyfit(x1, y1, 1)
f = np.poly1d(z)

a2 = polyfit(x1, y2, 1)
z2 = np.polyfit(x1, y2, 1)
f2 = np.poly1d(z2)

a3 = polyfit(x2, y3, 1)
z3 = np.polyfit(x2, y3, 1)
f3 = np.poly1d(z3)

pltTransExp = plt.errorbar(x1, y1, linestyle="", marker="o", markersize=7, capsize=3, ecolor='k',
                           markeredgecolor='k', markerfacecolor='k', label='Couche de PbCl2 #1')
pltTransExp2 = plt.errorbar(x1, y2, linestyle="", marker="o", markersize=7, capsize=3, ecolor='k',
                           markeredgecolor='k', markerfacecolor='w', label='Couche de PbCl2 #2')
pltTransExp3 = plt.errorbar(x2, y3, linestyle="", marker="o", markersize=7, capsize=3, ecolor='k',
                           markeredgecolor='k', markerfacecolor='r', label='Couche de PbCl2 #3')
plt.plot(x_regression, f(x_regression), 'b', linewidth=1.5,
         label="Régression linéaire sur les données (R²=0.9999); \n L'équation est d = 116.77p - 10.50.")
plt.plot(x_regression, f2(x_regression), 'g', linewidth=1.5,
         label="Régression linéaire sur les données (R²=0.9999); \n L'équation est d = 115.81p + 19.59.")
plt.plot(x_reg, f3(x_reg), 'r', linewidth=1.5,
         label="Régression linéaire sur les données (R²=0.9997); \n L'équation est d = 125.50p + 18.67.")
plt.xlim([0, 11.5])
plt.ylim([0, 1400])
plt.yticks(fontsize=16)
plt.xticks(fontsize=16)
plt.xlabel("Ordre d'interférence p", fontsize=18)
plt.ylabel("Épaisseur d de la couche [nm]", fontsize=18)
plt.legend(fontsize=13)
#plt.grid()
plt.minorticks_on()
fig = plt.gcf()
fig.set_size_inches(12, 7)
fig.savefig('EpaisVsOrdre.pdf', bbox_inches = 'tight', dpi=600)
plt.show()
print(f)
print(a)
print(f2)
print(a2)
print(f3)
print(a3)
