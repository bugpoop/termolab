import scipy.optimize as opt
import numpy as np 
import matplotlib.pyplot as plt
import formulas
formulas.ideal_gas()
xd = np.loadtxt("datax")
yd = np.loadtxt("datay") / 100
a = input("Enter x label")
plt.xlabel(a)
c = input("Enter y label")
plt.ylabel(c)
z = np.polyfit(xd, yd, 3)
f=np.poly1d(z)
plt.scatter(xd, yd)
plt.plot(xd, f(xd))
#plt.plot(xd, (10.0 / xd + 2200))
plt.show()
