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


filename = "Data/T_ordre_p.txt"

x1 = np.loadtxt(filename, usecols=0)
y1 = np.log(np.loadtxt(filename, usecols=1))
y2 = np.loadtxt(filename, usecols=3)

x1_regression = x1[len(x1)-8:]
x2_regression = x1[len(x1)-8:]
y1_regression = y1[len(y1)-8:]
y2_regression = y2[len(y2)-8:]

x_reg = np.arange(4, 11, 0.01)
x_regression = np.arange(4, 11, 0.01)
a = polyfit(x1_regression, y1_regression, 1)
z = np.polyfit(x1_regression, y1_regression, 1)
f = np.poly1d(z)

a2 = polyfit(x2_regression, y2_regression, 1)
z2 = np.polyfit(x2_regression, y2_regression, 1)
f2 = np.poly1d(z2)

pltTransExp = plt.errorbar(x1, y1, linestyle="",
                           marker="o", markersize=6, label="Couche de PbCl2 #1", capsize=3, ecolor='k',
                           markeredgecolor='k', markerfacecolor='k')
pltTransExp2 = plt.errorbar(x1, y2, linestyle="",
                           marker="o", markersize=6, label="Couche de PbCl2 #3", capsize=3, ecolor='k',
                           markeredgecolor='k', markerfacecolor='w')
plt.plot(x_regression, f(x_regression), 'b', linewidth=1.5,
         label="Régression linéaire sur les données (R²=0.9802); \n L'équation est ln($T_p$) = -0.0526p + 4.621.")
plt.plot(x2_regression, f2(x2_regression), 'r', linewidth=1.5,
         label="Régression linéaire sur les données (R²=0.9859); \n L'équation est ln($T_p$) = -0.0385p + 4.732.")
#plt.xlim([0, 1500])
#plt.ylim([0, 70])
plt.yticks(fontsize=16)
plt.xticks(fontsize=16)
plt.xlabel("Ordre d'interférence p", fontsize=18)
plt.ylabel("ln($T_p$)", fontsize=18)
plt.legend(fontsize=14, loc='lower left')
#plt.grid()
plt.minorticks_on()
fig = plt.gcf()
fig.set_size_inches(12, 7)
fig.savefig('TVsOrdre.pdf', bbox_inches = 'tight', dpi=600)
plt.show()
print(f)
print(a)
print(f2)
print(a2)
