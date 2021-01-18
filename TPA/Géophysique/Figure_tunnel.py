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


filename = "Data/Tunnel.txt"
filename2 = "Data/Terrain_tunnel_3m.txt"

x_tunnel = np.loadtxt(filename, usecols=0)
y_tunnel = np.loadtxt(filename, usecols=1)
y_tunnel_err = np.loadtxt(filename, usecols=2)

x_rock = np.loadtxt(filename2, usecols=0)
y_rock = np.loadtxt(filename2, usecols=1)
y_rock_err = np.loadtxt(filename2, usecols=2)

x_tunnel_surface = x_tunnel[:4]
y_tunnel_surface = y_tunnel[:4]
x_tunnel_rock = x_tunnel[len(x_tunnel)-5:]
y_tunnel_rock = y_tunnel[len(y_tunnel)-5:]

x_tunnel_surface_regression = np.arange(0.5, 2, 0.01)
a_tunnel_surface = polyfit(x_tunnel_surface, y_tunnel_surface, 1)
z_tunnel_surface = np.polyfit(x_tunnel_surface, y_tunnel_surface, 1)
f_tunnel_surface = np.poly1d(z_tunnel_surface)

x_tunnel_rock_regression = np.arange(2.5, 5, 0.01)
x_tunnel_rock_regression_continuity = np.arange(1.638, 2.5, 0.01)
a_tunnel_rock = polyfit(x_tunnel_rock, y_tunnel_rock, 1)
z_tunnel_rock = np.polyfit(x_tunnel_rock, y_tunnel_rock, 1)
f_tunnel_rock = np.poly1d(z_tunnel_rock)

x_rock_regression = np.arange(0.5, 5, 0.01)
a_rock = polyfit(x_rock, y_rock, 1)
z_rock = np.polyfit(x_rock, y_rock, 1)
f_rock = np.poly1d(z_rock)

pltTransExp = plt.errorbar(x_tunnel, y_tunnel, yerr=y_tunnel_err, xerr=0.1, linestyle="",
                           marker="o", markersize=4, label="Mesures au-dessus du tunnel", capsize=3, ecolor='k',
                           markeredgecolor='k', markerfacecolor='k')
pltTransExp2 = plt.errorbar(x_rock, y_rock, yerr=y_rock_err, xerr=0.1, linestyle="",
                           marker="o", markersize=4, label="Mesures à côté du tunnel", capsize=3, ecolor='k',
                           markeredgecolor='k', markerfacecolor='w')
plt.plot(x_tunnel_surface_regression, f_tunnel_surface(x_tunnel_surface_regression), 'r', linewidth=1.2,
         label='Lissage linéaire des données de \n la couche supérieure prises \n au-dessus du tunnel (R²=0.9991)')
plt.plot(x_tunnel_rock_regression, f_tunnel_rock(x_tunnel_rock_regression), 'b', linewidth=1.2,
         label='Lissage linéaire des données de \nla couche inférieure prises \n au-dessus du tunnel (R²=0.9839)')
plt.plot(x_tunnel_rock_regression_continuity, f_tunnel_rock(x_tunnel_rock_regression_continuity), 'b--',
         linewidth=1)
plt.plot(x_rock_regression, f_rock(x_rock_regression), 'y', linewidth=1.2,
         label='Lissage linéaire des données de \nla couche supérieure prises \n à côté du tunnel (R²=0.9842)')
plt.annotate('V$_{1, tunnel}$ ≈ 316 m/s', xy=[0.75, 3.2], fontsize=15)
plt.annotate('V$_{2, tunnel}$ ≈ 445 m/s', xy=[4, 11], fontsize=15)
plt.annotate('V$_{1, terrain}$ ≈ 292 m/s', xy=[3.4, 16.5], fontsize=15)
plt.xlim([0.3, 5.2])
plt.ylim([1.5, 19])
plt.vlines(x=1.638, ymin=0, ymax=6.75, colors='dimgrey', linewidth=1.2)
plt.yticks(fontsize=16)
plt.xticks(ticks=[1, 1.638, 2, 3, 4, 5], labels=[1, 'D$_{critique}$ \n (~1.64 m)', 2, 3, 4, 5], fontsize=16)
plt.xlabel("Distance entre l'impact et le géophone [m ± 0.1]", fontsize=18)
plt.ylabel("Temps de propagation [ms]", fontsize=18)
plt.legend(fontsize=13.2)
#plt.grid()
plt.minorticks_on()
fig = plt.gcf()
fig.set_size_inches(12, 7)
fig.savefig('Tunnel.pdf', bbox_inches = 'tight', dpi=600)
plt.show()
print(f_tunnel_surface)
print(a_tunnel_surface)
print(f_tunnel_rock)
print(a_tunnel_rock)
print(f_rock)
print(a_rock)
