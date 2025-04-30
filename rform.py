import numpy as np  

l = np.loadtxt("l")
h = np.loadtxt("h")
v = ( (np.pi * pow((11.4/2), 2) * l ) + 1.01 ) / 100 
p = ((1013 *0.1) + h*0.1333)
t = 303
n = 0.9536
R = (p*v)/(n*t)
np.savetxt("r", R, delimiter=' ')
print(R)
