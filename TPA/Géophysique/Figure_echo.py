import numpy as np
import matplotlib.pyplot as plt

filename = "Data/tunnel_0.5-1.5.txt"

time = np.loadtxt(filename, usecols=0, delimiter=',', skiprows=2)
Voltage1 = np.loadtxt(filename, usecols=1, delimiter=',', skiprows=2)
Voltage2 = np.loadtxt(filename, usecols=2, delimiter=',', skiprows=2)

plt.plot(time, Voltage2, 'b', linewidth=1.5,
         label="Mesures obtenues au géophone \n placé à 0.5 m de l'impact")
plt.plot(time, Voltage1, 'r', linewidth=1.5,
         label="Mesures obtenues au géophone \n placé à 1.5 m de l'impact")
plt.xlim([0, 0.025])
# plt.ylim([0, 14.3])
plt.yticks(fontsize=16)
plt.xticks(ticks=[0, 0.005, 0.01, 0.015, 0.02, 0.025], labels=[0, 5, 10, 15, 20, 25], fontsize=16)
plt.xlabel("Temps écoulé depuis l'impact de la masse sur le sol [ms]", fontsize=18)
plt.ylabel("Tension mesurée à l'oscilloscope [V]", fontsize=18)
plt.legend(fontsize=18)
#plt.grid()
plt.minorticks_on()
fig = plt.gcf()
fig.set_size_inches(12, 7)
fig.savefig('Tunnel_0_5__1_5.pdf', bbox_inches = 'tight', dpi=600)
plt.show()