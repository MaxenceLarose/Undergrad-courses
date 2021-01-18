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


filename = "Data/Terrain.txt"

x1 = np.loadtxt(filename, usecols=0)
y1 = np.loadtxt(filename, usecols=1)
y_err = np.loadtxt(filename, usecols=2)

x_surface = x1[:12]
y_surface = y1[:12]
x_rock = x1[len(x1)-6:]
y_rock = y1[len(y1)-6:]

x_surface_regression = np.arange(0.0, 2.4, 0.01)
x_surface_regression_continuity = np.arange(0.0, 2.862, 0.01)
a_surface = polyfit(x_surface, y_surface, 1)
z_surface = np.polyfit(x_surface, y_surface, 1)
f_surface = np.poly1d(z_surface)

x_rock_regression = np.arange(5, 10, 0.01)
x_rock_regression_continuity = np.arange(2.862, 5, 0.01)
a_rock = polyfit(x_rock, y_rock, 1)
z_rock = np.polyfit(x_rock, y_rock, 1)
f_rock = np.poly1d(z_rock)

pltTransExp = plt.errorbar(x1, y1, yerr=y_err, xerr=0.1, linestyle="",
                           marker="o", markersize=4, label="Temps mesuré à chaque distance", capsize=3, ecolor='k',
                           markeredgecolor='k', markerfacecolor='k')
plt.plot(x_surface_regression, f_surface(x_surface_regression), 'r', linewidth=1.5,
         label='Lissage linéaire des données \n de la couche supérieure (R²=0.9907)')
plt.plot(x_surface_regression_continuity, f_surface(x_surface_regression_continuity), 'r--', linewidth=1)
plt.plot(x_rock_regression, f_rock(x_rock_regression), 'b', linewidth=1.5,
         label='Lissage linéaire des données \n de la couche inférieure (R²=0.9749)')
plt.plot(x_rock_regression_continuity, f_rock(x_rock_regression_continuity), 'b--', linewidth=1)
plt.annotate('V$_1$ ≈ 343 m/s', xy=[0.5, 7], fontsize=15)
plt.annotate('V$_2$ ≈ 1466 m/s', xy=[6, 12.5], fontsize=15)
plt.xlim([0, 10.4])
plt.ylim([0, 14.3])
plt.vlines(x=2.862, ymin=0, ymax=8.8, colors='dimgrey', linewidth=1.2)
plt.yticks(fontsize=16)
plt.xticks(ticks=[0, 2, 2.862, 4, 6, 8, 10], labels=[0, 2, 'D$_{critique}$ \n (~2.86 m)', 4, 6, 8, 10], fontsize=16)
plt.xlabel("Distance entre l'impact et le géophone [m ± 0.1]", fontsize=18)
plt.ylabel("Temps de propagation [ms]", fontsize=18)
plt.legend(fontsize=18)
#plt.grid()
plt.minorticks_on()
fig = plt.gcf()
fig.set_size_inches(12, 7)
fig.savefig('Terrain.pdf', bbox_inches = 'tight', dpi=600)
plt.show()
print(f_surface)
print(a_surface)
print(f_rock)
print(a_rock)
