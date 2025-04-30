import numpy as np 

r = np.loadtxt("r")
std = np.std(r)
mn=np.mean(r)

print(mn, "+/-", std)
