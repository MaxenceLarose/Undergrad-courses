from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.optimize import bisect


class Laser:
    def __init__(self):
        self.pumpWaveLength = 809  # nm
        self.activeMediumDiameter = 200  # µm
        self.activeMediumLength = 0.50  # cm

        self.crossSection = 12.8*10**(-19)  # cm^2
        self.lifeTime = 230*10**(-6)  # s
        self.emissionWaveLength = 1064  # nm
        self.spectralWidth = 2*np.pi*120*10**9  # rad/s
        self.refractiveIndex = 1.82
        self.ionsDensity = 1.25*10**20  # cm^-3
        self.thermalCoefficient = 8*10**(-6)  # K^-1
        self.thermalConductivity = 0.13  # W/cmK
        self.lossCoefficient = 0.030

    def getOutputPower(self):
        Power = np.linspace(0.001, 10000, 100000)
        Glin = []
        D=0.001
        h = 6.626*10**(-34)
        c = 3*10**(8)
        L = 0.05
        tau = 230*10**(-6)
        longueurdonde= 1064*10**(-9)
        V=(np.pi*L*(1)**2)/4
        A= np.pi*0.0005**2
        Rp = 2.491*0.8*longueurdonde/(h*c*V)
        N = Rp*tau
        sigma = 2.8*10**(-23)
        Pin = 2.491*0.8
        Psat = h*c*np.pi*D**2/(sigma*tau*longueurdonde*4)
        lnGo=(tau*sigma*longueurdonde/(h*c*A))
        for i in Power:
            def f(G):
                return G - 1 - (Psat) * (lnGo*i -np.log(G))/i
            Glin.append(fsolve(f, 1))

        GdB = 10*np.log10(Glin)
        PowerdBm = 10*np.log10(Power)
    
        plt.plot(PowerdBm, GdB, color='k')
        #plt.xlim(-30, 40)
        #plt.ylim(0, 0.35)
        plt.yticks(fontsize=16)
        plt.xticks(fontsize=16)
        plt.xlabel("Puissace à l'entrée de l'amplificateur [dB]", fontsize = 18)
        plt.ylabel("Gain de l'amplificateur G [dB]", fontsize = 18)
        plt.minorticks_on()
        #fig = plt.gcf()
        #fig.set_size_inches(12, 7)
        #fig.savefig('Devoir1.pdf',bbox_inches = 'tight', dpi=600)
        plt.show()

        Pabs2 = np.linspace(0.00001, 155, 10000)
        Poutlin=[]
        for i in Pabs2:
            def f(Pout):
                return (np.log(Pout/i)+((Pout-i)/Psat))-(i*tau*sigma*longueurdonde/(h*c*A))
            Poutlin.append(float(fsolve(f,1)))
    
    
        plt.plot(Pabs2, Poutlin, color = 'k')
        plt.hlines(35,0,170, color = 'r')
        plt.xlim(0, 80)
        plt.ylim(0,150)
        plt.yticks(fontsize=16)
        plt.xticks(fontsize=16)
        plt.xlabel("Pabs 2 [W]", fontsize = 18)
        plt.ylabel("Pout [W]", fontsize = 18)
        plt.minorticks_on()
        plt.show()
    
        plt.plot(Pabs2/0.8, Poutlin, color = 'g')
        plt.hlines(35,0,170, color = 'r')
        plt.xlim(0, 80)
        plt.ylim(0,150)
        plt.yticks(fontsize=16)
        plt.xticks(fontsize=16)
        plt.xlabel("Posc [W]", fontsize = 18)
        plt.ylabel("Pout [W]", fontsize = 18)
        plt.minorticks_on()
        plt.show()
        return None

    def Beamwidth(self):
        #Lring = np.linspace(0.1, 0.4, 1000) #m
        #f = np.linspace(0.1, 0.4, 1000)
        #f = 10**100
        Pabs = 4 #W
        fth = 41/(100*Pabs)
        D = 200*10**(-6) #m
        A = np.pi*(D**2)/4
        #equation des matrices
        Lring2 = np.linspace(0.10, 0.4, 100) #m
        #focal = np.linspace(0.15, 0.4, 100)
        #Lring2 = 0.4
        list = []

        for i in Lring2:
            def getEffectiveArea(f):
                Aw = (4*f*fth-2*i*fth+i**2-4*i*f)/(4*f*fth)
                Bw = i-(i**2)/(4*f)
                Dw = 1-i/(2*f)
                m = (Aw+Dw)/2
                M = 1/Bw
                if m > 1 or m < -1:
                    MAT = M * ((m ** 2) - 1) ** (1 / 2)
                else:
                    MAT = M * (-(m ** 2) + 1) ** (1 / 2)
                eqn = MAT - 16.9341
                return eqn 
            list.append(fsolve(getEffectiveArea, x0 = 0.11, xtol=0.0001))

        # for x in focal:
        #    for i in Lring2:
        #        list.append(getEffectiveArea(Lring2, x))

        plt.plot(Lring2, list, color='k')
        plt.yticks(fontsize=16)
        plt.xticks(fontsize=16)
        # plt.hlines(-31.5, 0, 80, linestyles="--", colors="dimgrey", linewidth=3)
        plt.xlabel("Longueur de la cavité [m]", fontsize=18)
        plt.ylabel("Distance focale [m]", fontsize=18)
        plt.minorticks_on()
        plt.grid()
        #fig = plt.gcf()
        #fig.set_size_inches(12, 7)
        #fig.savefig('CourbeOptimisation.pdf',bbox_inches = 'tight', dpi=600)
        plt.show()

        return None

    def Beam(self):
        # Lring = np.linspace(0.1, 0.4, 1000) #m
        # f = np.linspace(0.1, 0.4, 1000)
        # f = 10**100
        Pabs = 4  # W
        fth = 41 / (100 * Pabs)
        D = 200 * 10 ** (-6)  # m
        A = np.pi * (D ** 2) / 4
        # equation des matrices
        #Lring2 = np.linspace(0.10, 0.35, 50)  # m
        # focal = np.linspace(0.15, 0.4, 100)
        # Lring2 = 0.4
        list = []

        def getBeamWidth(f):
            i = 0.4

            Aw = (4 * f * fth - 2 * i * fth + i ** 2 - 4 * i * f) / (4 * f * fth)
            Bw = i - (i ** 2) / (4 * f)
            Dw = 1 - i / (2 * f)
            m = (Aw + Dw) / 2
            M = 1 / Bw
            if m > 1 or m < -1:
                MAT = M * ((m ** 2) - 1) ** (1 / 2)
            else:
                MAT = M * (-(m ** 2) + 1) ** (1 / 2)
            w = (1064*10**-9/(abs(MAT)*np.pi))**(1/2)
            return w

        liste =[]
        f1 = np.linspace(0.0001, 1, 100000)

        for i in f1:
            liste.append(getBeamWidth(i))

        plt.plot(f1, np.array(liste)*10**6, color='k')
        plt.yticks(fontsize=16)
        plt.xticks(fontsize=16)
        plt.xlim(0, 0.2)
        plt.hlines(141.42, 0, 80, linestyles="--", colors="dimgrey", linewidth=3)
        plt.xlabel("Distance focale [m]", fontsize=18)
        plt.ylabel("Taille du faisceau [µm]", fontsize=18)
        plt.minorticks_on()
        plt.grid()
        #fig = plt.gcf()
        #fig.set_size_inches(12, 7)
        #fig.savefig('Curve_0.4.pdf',bbox_inches = 'tight', dpi=600)
        plt.show()

        return None

    def getPlotThreshold(self):
        def getThresholdPower(R):
            return 1.19864*(0.030 + np.log(1/R))
        R1 = np.linspace(0.75, 1, 100)
        Power = []
        for i in R1:
            Power.append(getThresholdPower(i))
        plt.plot(R1, Power, color='k')
        plt.xlim(0.75, 1)
        plt.ylim(0, 0.4)
        plt.yticks(fontsize=16)
        plt.xticks(fontsize=16)
        plt.xlabel("Réflectivité R du coupleur de sortie [-]", fontsize=18)
        plt.ylabel("Puissance pompe seuil [W]", fontsize=18)
        plt.minorticks_on()
        plt.grid()
        #fig = plt.gcf()
        #fig.set_size_inches(12, 7)
        #fig.savefig('Pompe_Seuil.pdf',bbox_inches = 'tight', dpi=600)
        plt.show()
        return None

    def getPlotPower(self):
        def getPower(P, R):
            return 0.911*(1-R)*(0.83428*P/(0.030 + np.log(1/R)) - 1)
        P1 = np.linspace(0, 4, 100)
        PowerOut1 = []
        PowerOut2 = []
        PowerOut3 = []
        PowerOut4 = []
        PowerOut5 = []
        PowerOut6 = []
        for i in P1:
            PowerOut1.append(getPower(i, 0.75))
            PowerOut2.append(getPower(i, 0.80))
            PowerOut3.append(getPower(i, 0.85))
            PowerOut4.append(getPower(i, 0.90))
            PowerOut5.append(getPower(i, 0.95))
        plt.plot(P1, PowerOut1, color='k', label='Courbe de puissance avec miroir $R=0.75$')
        plt.plot(P1, PowerOut2, color='b', label='Courbe de puissance avec miroir $R=0.80$')
        plt.plot(P1, PowerOut3, color='r', label='Courbe de puissance avec miroir $R=0.85$')
        plt.plot(P1, PowerOut4, color='g', label='Courbe de puissance avec miroir $R=0.90$')
        plt.plot(P1, PowerOut5, color='y', label='Courbe de puissance avec miroir $R=0.95$')
        plt.xlim(0, 4)
        plt.ylim(0, 2.3)
        plt.yticks(fontsize=16)
        plt.xticks(fontsize=16)
        plt.xlabel("Puissance pompe absorbée [W]", fontsize=18)
        plt.ylabel("Puissance de sortie [W]", fontsize=18)
        plt.legend(fontsize=18)
        plt.minorticks_on()
        plt.grid()
        #fig = plt.gcf()
        #fig.set_size_inches(12, 7)
        #fig.savefig('Puissance_Sortie.pdf',bbox_inches = 'tight', dpi=600)
        plt.show()

        R1 = np.linspace(0.75, 1, 100)
        Ref1 = []
        for i in R1:
            Ref1.append(getPower(4, i))
        plt.plot(R1, Ref1, color='k')
        plt.xlim(0.75, 1)
        #plt.ylim(0, 2.3)
        plt.yticks(fontsize=16)
        plt.xticks(fontsize=16)
        plt.xlabel("Réflectivité du miroir de sortie R [-]", fontsize=18)
        plt.ylabel("Puissance de sortie [W]", fontsize=18)
        plt.minorticks_on()
        plt.grid()
        #fig = plt.gcf()
        #fig.set_size_inches(12, 7)
        #fig.savefig('Puissance_Ref.pdf',bbox_inches = 'tight', dpi=600)
        plt.show()

        return None


Oscillator = Laser()
Oscillator.Beamwidth()
Oscillator.Beam()
Oscillator.getPlotThreshold()
Oscillator.getPlotPower()
Oscillator.getOutputPower()
