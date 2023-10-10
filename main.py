import matplotlib.pyplot as plt
import scipy.stats as stat
import numpy as np
from funcions import*

malla = int(20)
temperatura = float(input("Introdueix la Temperatura inicial: "))
escombratges = int(1000)

spin_array = init_spin_array(malla, malla)

#Mètode Monte Carlo:

y=[0]
x=[0]
#a,b = [], []

for i in range(0, malla):
   for j in range(0, malla):
        e0 = energy(spin_array, malla, i, j)

for escombratge in range(0, escombratges):
    for i in range(0, malla):
        for j in range(0, malla):
            spin_array[i, j] *= canvi()
            e1 = energy(spin_array, malla, i, j)
            q=np.exp(-1 * (e1-e0)/temperatura)
            def accept():
                s = stat.bernoulli.rvs(q,size=1)
                if s<0.5:
                    return -1
                else:
                    return 1
            if e1 <= e0:
                spin_array[i, j] *= 1
            
    #           
            else:
                spin_array[i, j] *= accept()
    #           
    
    #print(spin_array)
    mag = sum(sum(spin_array))
    x.append(escombratge)
    y.append(mag)
    #plt.plot(x[escombratge],y[escombratge])
    #print ('Magnetització: ',mag)

  
plt.plot(x,y)
plt.title('T=  %s Kelvin.'%(temperatura))
plt.xlabel('Escombratges')
plt.ylabel('Magnetització')

plt.show()

#plt.imshow(x[escombratge],y[escombratge])


