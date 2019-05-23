import numpy as np
import matplotlib.pyplot as plt

barctiempos=[73,28,59,52,39,137]
barcposx=[4,10,12,80,50,40]

def velocidad(xf,tf):
    velo= (xf)/(tf)
    return float(velo)
def Metropolis(iteraciones,paso):
    
	VELOCIDADES=np.zeros(iteraciones)
	VELOCIDADES[0]=np.random.random()
	for i in range(iteraciones-1):
       
        fa=velocidad(barcposx[j],barctiempos[j])
        propuesta = fa+np.random.normal()*paso
        ratio=propuesta/fa
        rr=np.random.uniform()
        if(rr < ratio):
            VELOCIDADES[i+1]=propuesta
        else:
            VELOCIDADES[i+1]=fa         
    return VELOCIDADES
