import scipy.optimize as opt
import numpy as np 
import matplotlib.pyplot as plt 
xd = np.loadtxt("datax")
yd = np.loadtxt("datay") / 100
a = input("Enter x label")
plt.xlabel(a)
c = input("Enter y label")
plt.ylabel(c)
#b = Regression.estimate_coef(x, y)
#Regression.plot_regression_line(x, y, b)
#def func(x, a, b):
#    return a / x + b
#bounds = (1.0, [np.inf, np.inf])
#guess= [1, 0.9536*298.15]
#optimizedParameters, pcov = opt.curve_fit(func, xd, yd ) #bounds=bounds, #p0=guess);

z = np.polyfit(xd, yd, 3)
f=np.poly1d(z)

plt.scatter(xd, yd)
plt.plot(xd, f(xd))
#plt.plot(xd, (10.0 / xd + 2200))
plt.show()
