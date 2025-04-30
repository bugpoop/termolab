import Regression
import numpy as np 
import matplotlib.pyplot as plt 
x = np.loadtxt("datax")
y = np.loadtxt("datay")
a = input("Enter x label")
plt.xlabel(a)
c = input("Enter y label")
plt.ylabel(c)
b = Regression.estimate_coef(x, y)
Regression.plot_regression_line(x, y, b)
