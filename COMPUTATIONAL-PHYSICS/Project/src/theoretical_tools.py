import matplotlib.pyplot as plt
from scipy.stats import norm, rayleigh
import numpy as np
import matplotlib.mlab as mlab


def get_fractal_dimension():
    pass



def plot_mean_displacement(distance, nb_steps, number_of_walkers):
    #plt.hist(distance, histtype='stepfilled', alpha=0.5, bins=20)
    n, bins, patches = plt.hist(distance, histtype='stepfilled', alpha=0.5, bins=30, density=True)
    loc, sigma = rayleigh.fit(data=distance)
    print(f"loc: {loc} and sigma: {sigma}")
    x = np.linspace(0, distance.max()+5, 100)
    pdf_fitted = rayleigh.pdf(x, loc, sigma)
    plt.plot(x, pdf_fitted, color='r')
    rms = np.sqrt(nb_steps)
    rms_ex = np.sqrt(np.mean(np.asarray(distance)**2))
    plt.vlines(rms, 0, pdf_fitted.max(), linestyle='--', color='k', linewidth=1)
    plt.vlines(rms_ex, 0, pdf_fitted.max(), linestyles='--', color='grey', linewidth=1)
    plt.xlabel('Distance moyenne parcourue')
    plt.ylabel('Probabilité [-]')
    plt.title('Distance moyenne parcourue pour {} marches aléatoires '.format(number_of_walkers))
    plt.legend(['Rayleigh $\sigma =$ {}'.format(sigma), '$N$ = {}'.format(nb_steps), 'RMS = {}'. format(rms),
                'RMS (exp) = {}'.format(rms_ex)])
    plt.show()




# Écart-type
# Distance moyenne