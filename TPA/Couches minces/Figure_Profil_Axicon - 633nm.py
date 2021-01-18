import numpy as np
import matplotlib.pyplot as plt
import math


def Reflectivity(r_array, r_max, ext):
    d_array = []

    for r in r_array:
        if -r_max <= r <= 0:
            d = (7*10**-3)*r + 1500
        elif 0 <= r <= r_max:
            d = (-7*10**-3)*r + 1500
        else:
            d = 0
            print('Error')
        d_array.append(d)

    d_array = np.array(d_array)
    num = -0.4609 + 0.3155*np.e**(-0.0538*1j*d_array)
    denum = 1 - 0.1454*np.e**(-0.0538*1j*d_array)

    Gamma = num/denum

    if ext is True:
        k = np.e**(-4.5084*10**-4*d_array)
    else:
        k = 1

    return k*Gamma * np.conjugate(Gamma)


def Transmittivity(r_array, r_max, ext: bool):
    d_array = []

    for r in r_array:
        if -r_max <= r <= 0:
            d = (7*10**-3)*r + 1500
        elif 0 <= r <= r_max:
            d = (-7*10**-3)*r + 1500
        else:
            d = 0
            print('Error')
        d_array.append(d)

    d_array = np.array(d_array)
    num = 0.709*np.e**(-0.0269*1j*d_array)
    denum = 1 - 0.1454*np.e**(-0.0538*1j*d_array)

    tau = num/denum

    if ext is True:
        k = np.e**(-4.5084*10**-4*d_array)
    else:
        k = 1

    return k*1.41*(tau * np.conjugate(tau))


x = np.arange(-200*1000, 200*1000, 10)

plt.plot(x/1000, np.real(Transmittivity(x, 200*1000, False))*100, 'r', linewidth=1.5,
         label="Profil de transmission")
plt.plot(x/1000, np.real(Reflectivity(x, 200*1000, False))*100, 'b', linewidth=1.5,
         label="Profil de réflexion")
plt.plot(x/1000, np.real(Reflectivity(x, 200*1000, False))*100 + np.real(Transmittivity(x, 200*1000, False))*100, 'k', linewidth=1.5,
         label="100(R + T)")
plt.xlim([-200, 200])
plt.ylim([0, 105])
plt.yticks(fontsize=16)
plt.xticks(fontsize=16)
plt.xlabel("Position radiale $r$ [μm]", fontsize=18)
plt.ylabel("Intensité mesurée [%]", fontsize=18)
plt.legend(fontsize=18)
#plt.grid()
plt.minorticks_on()
#fig = plt.gcf()
#fig.set_size_inches(12, 7)
#fig.savefig('Profil_avec_extinction.pdf', bbox_inches = 'tight', dpi=600)
plt.show()