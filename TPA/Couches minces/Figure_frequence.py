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


filename = "Data/frequence_epaisseur.txt"

x1 = np.loadtxt(filename, usecols=0)
y1 = np.loadtxt(filename, usecols=1)

x_regression = np.arange(0, 1500, 0.01)
a = polyfit(x1, y1, 1)
z = np.polyfit(x1, y1, 1)
f = np.poly1d(z)

pltTransExp = plt.errorbar(x1, y1, linestyle="", marker="o", markersize=7, capsize=3, ecolor='k',
                           markeredgecolor='k', markerfacecolor='k')
plt.plot(x_regression, f(x_regression), 'b', linewidth=1.5,
         label="Régression linéaire sur les données (R²=0.9986); \n L'équation est $\delta$f = 0.0467d - 0.015.")
plt.xlim([0, 1500])
plt.ylim([0, 70])
plt.yticks(fontsize=16)
plt.xticks(fontsize=16)
plt.xlabel("Épaisseur d de la couche [nm]", fontsize=18)
plt.ylabel("Variation de fréquence $\delta$f [kHz]", fontsize=18)
plt.legend(fontsize=18)
#plt.grid()
plt.minorticks_on()
fig = plt.gcf()
fig.set_size_inches(12, 7)
fig.savefig('FreqVsEpais.pdf', bbox_inches = 'tight', dpi=600)
plt.show()
print(f)
print(a)
