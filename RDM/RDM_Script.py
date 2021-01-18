from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

""" Les graphiques s'affichent directement et sont enregistrés en .pdf dans le document où est
    placé le script. Afin de voir apparaître les valeurs des contraintes maximales, il suffit de 
    décommenter toutes les lignes où il est écrit plt.show()."""


class Structure:
    def __init__(self):
        self.poleLinearMass = 155.094
        self.framesLinearMass = 47.378
        self.signDensity = 2790
        self.iceDensity = 920
        self.windPressure = 1755

        self.poleTotalLength = 7
        self.horizontalFramesLength = 4.646
        self.verticalFramesLength = 0.7936
        self.signLength = 4.3
        self.signHeight = 2
        self.signThickness = 0.007
        self.iceThickness = 0.031

        self.horizontalFramesPositionY = 2.577
        self.verticalFrame1PositionY = 1.9
        self.verticalFrame2PositionY = 3.35
        self.verticalFrame3PositionY = 4.8
        self.signPositionX = 0.1051
        self.signPositionY = 2.75
        self.icePositionX = 0.1241
        self.icePositionY = self.signPositionY
        self.windPositionX = self.signPositionX
        self.windPositionY = self.signPositionY
        self.windPositionZ = 6.4

        self.outsideRadius = 0.254
        self.sectionThickness = 0.0127
        self.insideRadius = self.outsideRadius - self.sectionThickness
        self.inertiaMoment = 6.07*10**-4
        self.inertiaPolarMoment = 0.00121
        self.sectionArea = 0.0197

    def getWindForce(self):
        windForce = self.windPressure*self.signLength*self.signHeight
        return windForce

    def getForceAndMomentOnSection(self):
        z = symbols("z")

        poleWeight = (self.poleTotalLength-z)*self.poleLinearMass*9.81

        horizontalFramesWeight = self.horizontalFramesLength*self.framesLinearMass*9.81
        verticalFramesWeight = self.verticalFramesLength*self.framesLinearMass*9.81
        framesTotalWeight = 2*horizontalFramesWeight+3*verticalFramesWeight

        signWeight = self.signLength*self.signHeight*self.signThickness*self.signDensity*9.81
        iceWeight = self.signLength*self.signHeight*self.iceThickness*self.iceDensity*9.81
        structureTotalWeight = poleWeight + framesTotalWeight + signWeight + iceWeight

        shearForceX = self.getWindForce()

        shearForceY = 0

        normalForceZ = structureTotalWeight

        bendingMomentX = 2*self.horizontalFramesPositionY*horizontalFramesWeight + verticalFramesWeight*\
                         (self.verticalFrame1PositionY + self.verticalFrame2PositionY + self.verticalFrame3PositionY)\
                         + self.signPositionY*signWeight + self.icePositionY*iceWeight

        bendingMomentY = -self.signPositionX*signWeight - self.icePositionX*iceWeight + (self.windPositionZ - z)*\
                         self.getWindForce()

        torsionalMomentZ = -self.windPositionY * self.getWindForce()

        print(np.array([shearForceX, shearForceY, normalForceZ, bendingMomentX, bendingMomentY, torsionalMomentZ]))

        return np.array([shearForceX, shearForceY, normalForceZ, bendingMomentX, bendingMomentY, torsionalMomentZ])

    def getShearFormula(self):
        x = symbols("x")

        shearForceX = self.getForceAndMomentOnSection()[0]

        # For x < insideRadius
        sectionThicknessFunc1 = 2*((self.outsideRadius**2 - x**2)**(1/2)-(self.insideRadius**2 - x**2)**(1/2))
        QFunc1 = 2/3*((self.outsideRadius**2 - x**2)**(3/2) - (self.insideRadius**2 - x**2)**(3/2))
        shearFormula1 = (shearForceX*QFunc1)/(self.inertiaMoment*sectionThicknessFunc1)

        # For insideRadius < x < outsideRadius
        sectionThicknessFunc2 = 2*(self.outsideRadius**2 - x**2)**(1/2)
        QFunc2 = 2/3*(self.outsideRadius**2 - x**2)**(3/2)
        shearFormula2 = (shearForceX*QFunc2)/(self.inertiaMoment*sectionThicknessFunc2)

        print(shearFormula1.evalf(subs={x: 0}))

        x1 = np.linspace(0, self.insideRadius - 0.00000001, 1000)
        x2 = np.linspace(self.insideRadius - 0.00000001, self.outsideRadius, 1000)
        x3 = np.linspace(0, -self.insideRadius + 0.00000001, 1000)
        x4 = np.linspace(-self.insideRadius + 0.00000001, -self.outsideRadius, 1000)
        shearFunc1 = []
        shearFunc2 = []
        for d in x1:
            shearFunc1.append(shearFormula1.evalf(subs={x: d}))
        for d in x2:
            shearFunc2.append(shearFormula2.evalf(subs={x: d}))

        plt.plot(x1, np.array(shearFunc1)/10**6, color='k')
        plt.plot(x2, np.array(shearFunc2)/10**6, color='k')
        plt.plot(x3, np.array(shearFunc1)/10**6, color='k')
        plt.plot(x4, np.array(shearFunc2)/10**6, color='k')
        plt.yticks(fontsize=14)
        plt.xticks(fontsize=14)
        plt.xlabel("Position x sur la section[m]", fontsize=16)
        plt.ylabel("Contrainte de cisaillement [MPa]", fontsize=16)
        plt.minorticks_on()
        plt.grid()
        fig = plt.gcf()
        fig.set_size_inches(9, 7)
        fig.savefig('GraphShearFunc.pdf', bbox_inches='tight', dpi=600)
        #plt.show()

        return np.array([shearFormula1, shearFormula2])

    def getTorsionFormula(self):
        x = symbols("x")
        y = symbols("y")

        internalTorque = self.getForceAndMomentOnSection()[5]
        torsionFormula = internalTorque*((x**2 + y**2)**(1/2))/self.inertiaPolarMoment


        def f(r):
            return internalTorque*r/self.inertiaPolarMoment

        x1 = np.linspace(self.insideRadius, self.outsideRadius, 100)
        torsionFunc = []
        for d in x1:
            torsionFunc.append(torsionFormula.evalf(subs={x: d, y: 0}))
        plt.plot(x1, abs(np.array(torsionFunc))/10**6, 'k')
        plt.yticks(fontsize=14)
        plt.xticks(fontsize=14)
        plt.xlabel("Distance r par rapport au centre de la section [m]", fontsize=16)
        plt.ylabel("Contrainte de cisaillement [MPa]", fontsize=16)
        plt.minorticks_on()
        plt.grid()
        fig = plt.gcf()
        fig.set_size_inches(9, 7)
        fig.savefig('GraphTorsionFunc.pdf', bbox_inches='tight', dpi=600)
        #plt.show()

        p = np.linspace(0, 2*np.pi, 1000)
        r = np.linspace(self.insideRadius, self.outsideRadius, 1000)
        R, P = np.meshgrid(r, p)
        X, Y = R * np.cos(P), R * np.sin(P)
        Z = f(R)

        plt.contourf(X, Y, abs(Z/10**6), 100)
        cb = plt.colorbar()
        cb.set_label(label='Contrainte de cisaillement [MPa]', size=16)
        cb.ax.tick_params(labelsize=14)
        plt.yticks(fontsize=14)
        plt.xticks(fontsize=14)
        plt.xlabel('Position y [m]', fontsize=16)
        plt.ylabel('Position x [m]', fontsize=16)
        plt.grid()
        fig = plt.gcf()
        fig.set_size_inches(9, 7)
        fig.savefig('GraphTorsionFunc2D.pdf', bbox_inches='tight', dpi=600)
        #plt.show()

        return torsionFormula

    def getNormalStressFormula(self):
        z = symbols("z")

        internalNormalForce = self.getForceAndMomentOnSection()[2]
        normalStressFormula = internalNormalForce/self.sectionArea

        print(normalStressFormula)

        z1 = np.linspace(0, 5.8, 1000)
        normalStressFunc = []
        for d in z1:
            normalStressFunc.append(normalStressFormula.evalf(subs={z: d}))

        plt.plot(z1, np.array(normalStressFunc)/10**6, color='k')
        plt.yticks(fontsize=14)
        plt.xticks(fontsize=14)
        plt.xlabel("Hauteur z de la section par rapport au sol [m]", fontsize=16)
        plt.ylabel("Contrainte normale [MPa]", fontsize=16)
        plt.minorticks_on()
        plt.grid()
        fig = plt.gcf()
        fig.set_size_inches(9, 7)
        fig.savefig('GraphNormalStressFunc.pdf', bbox_inches='tight', dpi=600)
        #plt.show()

        return normalStressFormula

    def getFlexureFormula(self):
        x = symbols("x")
        y = symbols("y")
        z = symbols("z")

        normalStressX = self.getForceAndMomentOnSection()[3]*y/self.inertiaMoment
        normalStressY = -self.getForceAndMomentOnSection()[4]*x/self.inertiaMoment

        flexureFormula = normalStressX + normalStressY
        print(flexureFormula)

        ratioNoStress = self.getForceAndMomentOnSection()[3]/self.getForceAndMomentOnSection()[4].evalf(subs={z: 0})
        thetaNoStress = np.arctan(float(ratioNoStress))
        thetaMaxStress = thetaNoStress + np.pi/2
        thetaMinStress = thetaNoStress - np.pi/2
        xMaxStress = self.outsideRadius*np.sin(thetaMaxStress)
        yMaxStress = self.outsideRadius*np.cos(thetaMaxStress)
        xMinStress = self.outsideRadius*np.sin(thetaMinStress)
        yMinStress = self.outsideRadius*np.cos(thetaMinStress)

        print(flexureFormula.evalf(subs={x: xMaxStress, y: yMaxStress, z: 0}))
        print(flexureFormula.evalf(subs={x: xMinStress, y: yMinStress, z: 0}))

        def f(r, p, z):
            return -1647.44645799012*r*np.sin(p)*(96100.0621722108 - 15093.0*z) + 43660644.7123584*r*np.cos(p)

        p = np.linspace(0, 2*np.pi, 1000)
        r = np.linspace(self.insideRadius, self.outsideRadius, 1000)
        R, P = np.meshgrid(r, p)
        X, Y = R * np.sin(P), R * np.cos(P)
        Z = f(R, P, z=0)

        fig = plt.contourf(Y, X, Z/10**6, 100)
        cb = plt.colorbar()
        cb.set_label(label='Contrainte normale [MPa]', size=16)
        cb.ax.tick_params(labelsize=14)
        plt.yticks(fontsize=14)
        plt.xticks(fontsize=14)
        plt.xlabel('Position y [m]', fontsize=16)
        plt.ylabel('Position x [m]', fontsize=16)
        plt.annotate("", xy=(yMaxStress, xMaxStress), xycoords='data', xytext=(yMinStress, xMinStress),
                     textcoords='data', arrowprops=dict(arrowstyle="-", connectionstyle="arc3, rad=0"),)
        plt.annotate("", xy=(-xMaxStress, yMaxStress), xycoords='data', xytext=(-xMinStress, yMinStress),
                     textcoords='data', arrowprops=dict(arrowstyle="-", connectionstyle="arc3, rad=0"),)
        plt.grid()
        fig = plt.gcf()
        fig.set_size_inches(9, 7)
        fig.savefig('GraphFlexureFunc2D.pdf', bbox_inches='tight', dpi=600)
        #plt.show()

        # fig = plt.contourf(Y, X, Z/10**6 - 1031353.24525401/10**6, 100)
        # plt.colorbar(label='Contrainte normale totale sur la section du poteau [MPa]')
        # plt.xlabel('Position y [m]', fontsize=12)
        # plt.ylabel('Position x [m]', fontsize=12)
        # plt.annotate("", xy=(yMaxStress, xMaxStress), xycoords='data', xytext=(yMinStress, xMinStress),
        #              textcoords='data', arrowprops=dict(arrowstyle="-", connectionstyle="arc3, rad=0"),)
        # plt.annotate("", xy=(-xMaxStress, yMaxStress), xycoords='data', xytext=(-xMinStress, yMinStress),
        #              textcoords='data', arrowprops=dict(arrowstyle="-", connectionstyle="arc3, rad=0"),)
        # plt.grid()
        # fig = plt.gcf()
        # fig.set_size_inches(9, 7)
        # fig.savefig('GraphNormalStressTotal.pdf', bbox_inches='tight', dpi=600)
        # # plt.show()


        return flexureFormula

    def getMaxShearStress(self):
        x = symbols("x")
        y = symbols("y")

        # For x < insideRadius and y > 0
        totalShearStressXZ = self.getShearFormula()[0] - self.getTorsionFormula()

        # For insideRadius < x < outsideRadius and y > 0
        totalShearStressXY = self.getShearFormula()[1] - self.getTorsionFormula()

        maxShearStressXZ = totalShearStressXZ.evalf(subs={x: 0, y: self.outsideRadius})
        maxShearStressXY = totalShearStressXY.evalf(subs={x: self.outsideRadius, y: 0})

        print("Max Shear Stress XZ = {} MPa at x = {} m, y = {} m".format
              (round(abs(maxShearStressXZ/10**6), 3), 0, round(self.outsideRadius, 4)))

        print("Max Shear Stress XY = {} MPa at x = {} m, y = {} m".format
              (round(abs(maxShearStressXY/10**6), 3), round(self.outsideRadius, 4), 0))

    def getMaxNormalStress(self):
        x = symbols("x")
        y = symbols("y")
        z = symbols("z")

        ratioNoStress = self.getForceAndMomentOnSection()[3]/self.getForceAndMomentOnSection()[4].evalf(subs={z: 0})
        thetaNoStress = np.arctan(float(ratioNoStress))
        thetaMaxStress = thetaNoStress + np.pi/2
        thetaMinStress = thetaNoStress - np.pi/2
        xMaxStress = self.outsideRadius*np.sin(thetaMaxStress)
        yMaxStress = self.outsideRadius*np.cos(thetaMaxStress)
        xMinStress = self.outsideRadius*np.sin(thetaMinStress)
        yMinStress = self.outsideRadius*np.cos(thetaMinStress)

        totalNormalStress = self.getFlexureFormula() + self.getNormalStressFormula()

        maxNormalStress = totalNormalStress.evalf(subs={x: xMinStress, y: yMinStress, z: 0})/10**6

        print("Max Normal Stress = {} MPa in compression at x = {} m, y = {} m and z = {} m".format
              (round(abs(maxNormalStress), 3), round(xMinStress, 4), round(yMinStress, 4), 0))


Sign = Structure()

#Sign.getForceAndMomentOnSection()
#Sign.getShearFormula()
#Sign.getTorsionFormula()
#Sign.getNormalStressFormula()
#Sign.getFlexureFormula()
#Sign.getMaxShearStress()
Sign.getMaxNormalStress()