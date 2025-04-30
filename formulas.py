import numpy as np  
def ideal_gas():
    l = np.loadtxt("l")
    h = np.loadtxt("h")
    v = ( (np.pi * pow((11.4/2), 2) * l ) + 1.01 ) / 100 
    p = ((1013 *0.1) + h*0.1333)
    np.savetxt("datay", v, delimiter=' ')
    np.savetxt("datax", p, delimiter=' ')
    return 0
