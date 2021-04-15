import matplotlib.pyplot as plt
from scipy.stats import norm, rayleigh
import numpy as np
import matplotlib.mlab as mlab


def get_fractal_dimension():
    pass



def plot_mean_displacement(distance, nb_steps, number_of_walkers):
    #plt.hist(distance, histtype='stepfilled', alpha=0.5, bins=20)
    n, bins, patches = plt.hist(distance, histtype='stepfilled', alpha=0.5, bins=20, density=True)
    loc, sigma = rayleigh.fit(data=distance)
    print(f"loc: {loc} and sigma: {sigma}")
    x = np.linspace(0, distance.max()+5, 100)
    pdf_fitted = rayleigh.pdf(x, loc, sigma)
    plt.plot(x, pdf_fitted, color='r')
    rms = np.sqrt(nb_steps)
    plt.vlines(rms, 0, pdf_fitted.max(), linestyle='--', color='k')
    plt.xlabel('Distance moyenne parcourue')
    plt.ylabel('Fréquence')
    plt.title('Distance moyenne parcourue pour {} marches aléatoires '.format(number_of_walkers))
    plt.legend(['Rayleigh $\sigma =$ {}'.format(sigma), '$N$ = {}'.format(number_of_walkers), 'RMS = {}'. format(rms)])
    plt.show()




# Écart-type
# Distance moyenne