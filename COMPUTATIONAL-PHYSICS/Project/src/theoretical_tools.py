import matplotlib.pyplot as plt
from scipy.stats import norm, rayleigh
import numpy as np
import matplotlib.mlab as mlab


def get_fractal_dimension():
    pass



def plot_mean_displacement(distance):
    plt.hist(distance, histtype='stepfilled', alpha=0.5, bins=20)
    # x = np.linspace(0, 26, 1000)
    # X = x[:, np.newaxis]
    # plt.plot(x, pdf(X), )
    plt.xlabel('Distance moyenne parcourue')
    plt.ylabel('Probabilité [-]')
    plt.show()

    n, bins, patches = plt.hist(distance, histtype='stepfilled', alpha=0.5, bins=20, density=True)
    loc, sigma = rayleigh.fit(data=distance)
    print(f"loc: {loc} and sigma: {sigma}")
    x = np.linspace(0, distance.max(), 100)
    pdf_fitted = rayleigh.pdf(x, loc, sigma)
    plt.plot(x, pdf_fitted, color='r')
    plt.show()

    # n, bins, patches = plt.hist(distance, histtype='stepfilled', alpha=0.5, bins=20)
    # (mu, sigma) = rayleigh.fit(distance)
    # y = mlab.normpdf(bins, mu, sigma)
    # l = plt.plot(bins, y, 'r--', linewidth=2)


# Écart-type
# Distance moyenne