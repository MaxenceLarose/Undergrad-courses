import matplotlib.pyplot as plt
import logging
from typing import Tuple
from scipy.stats import norm, rayleigh
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.mlab as mlab


def get_mass_within_radius(
        radius: np.ndarray,
        fractal_dimensionality: float,
        arbitrary_constant: float
) -> np.ndarray:
    """
    This functions returns the mass of a cluster given the radius of this cluster, its fractal dimensionality and an
    arbitrary constant.

    Parameters
    ----------
    radius (np.ndarray): Radius of the clusters.
    fractal_dimensionality (float): Fractal dimensionality of the clusters.
    arbitrary_constant (float): An arbitrary constant used for the fit.

    Returns
    -------
    mass (np.ndarray): Mass of the cluster. The mass of a cluster is equal to the number of walkers added to this
                       cluster.
    """
    mass = arbitrary_constant*radius**fractal_dimensionality

    return mass


def plot_fractal_dimension(
        radius: list,
        mass: list,
):
    """
    This functions returns the mass of a cluster given the radius of this cluster, its fractal dimensionality and an
    arbitrary constant.

    Parameters
    ----------
    radius (list): Radius of the clusters.
    mass (list): Mass of the clusters. The mass of a cluster is equal to the number of walkers added to this
                 cluster.

    Returns
    -------
    Fig and axes.
    """
    param, param_covariance = curve_fit(
        f=get_mass_within_radius,
        xdata=radius,
        ydata=mass
    )

    logging.info(f"Fractal Dimensionality is {param[0]}")
    radius_array = np.arange(np.asarray(radius).min() - 1, np.asarray(radius).max() + 1, 1)

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(1, 1, 1)

    line1, = ax.plot(
        np.log(radius_array),
        np.log(get_mass_within_radius(radius_array, *param)),
        linestyle='--',
        color='k',
        lw=2
    )

    line2 = ax.scatter(
        np.log(radius),
        np.log(mass),
        color='k',
        edgecolors='k',
        s=30
    )

    # ax.set_title("Dimension fractale", fontsize=18)
    ax.set_xlabel("Logarithme du rayon de l'agrégat", fontsize=16)
    ax.set_ylabel("Logarithme du nombre de particules \ndans le rayon donné", fontsize=16)
    ax.legend([f"Dimension fractale: {param[0]:.3f} \nCorrélation $R^2$: {param_covariance[0]:.3f}"], fontsize=16)
    ax.minorticks_on()
    ax.set_xlim([min(np.log(radius_array)), max(np.log(radius_array))])
    ax.tick_params(axis='both', labelsize=12)
    plt.tight_layout()
    ax.grid()
    save_name = "Fractal_Dimensionality"
    plt.savefig(f"{save_name}.pdf", dpi=300)
    plt.show()


def plot_mean_displacement(distance, nb_steps, number_of_walkers):
    show_properties(nb_steps=nb_steps)
    n, bins, patches = plt.hist(distance, histtype='stepfilled', alpha=0.5, bins=30, density=True)
    loc, sigma = rayleigh.fit(data=distance)
    logging.info(f"loc: {loc} and sigma: {sigma}")
    x = np.linspace(0, distance.max()+5, 100)
    pdf_fitted = rayleigh.pdf(x, loc, sigma)
    plt.plot(x, pdf_fitted, color='r')
    rms = np.sqrt(nb_steps)
    rms_exp = np.sqrt(np.mean(np.asarray(distance)**2))
    var_exp = (sigma ** 2) * ((4 - np.pi) / 2)
    std_exp = np.sqrt(var_exp)
    mean_exp = sigma*np.sqrt(np.pi/2)
    plt.vlines(rms, 0, pdf_fitted.max(), linestyle='--', color='k', linewidth=1)
    plt.vlines(rms_exp, 0, pdf_fitted.max(), linestyles='--', color='grey', linewidth=1)
    plt.xlabel('Distance moyenne parcourue')
    plt.ylabel('Probabilité [-]')
    plt.title(f'Distance moyenne parcourue pour {number_of_walkers} marches aléatoires ')
    plt.legend([f'Rayleigh $\sigma =$ {sigma}', f'$N$ = {nb_steps}', f'RMS = {rms}',
                f'RMS (exp) = {rms_exp}'])
    logging.info(f'Var (exp) = {var_exp}')
    logging.info(f'Valeur moyenne (exp) = {mean_exp}')
    logging.info(f'Écart-type (exp) = {std_exp}')
    plt.show()


def show_properties(nb_steps):
    rms = np.sqrt(nb_steps)
    sigma_theo = rms/np.sqrt(2)
    var_theo = (sigma_theo**2)*((4-np.pi)/2)
    std_theo = np.sqrt(var_theo)
    mean_theo = sigma_theo*np.sqrt(np.pi/2)
    logging.info(f"RMS (theorie) = {rms}")
    logging.info(f"$\sigma$ (theorie) = {sigma_theo}")
    logging.info(f"Variance (theorie) = {var_theo}")
    logging.info(f"Écart-type (theorie) = {std_theo}")
    logging.info(f"Valeur moyenne (theorie) = {mean_theo}")

