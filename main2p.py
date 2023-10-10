import matplotlib.pyplot as plt
import scipy.stats as stat
#import matplotlib as mpl
import numpy as np
from funcions import*

malla = int(input("Introdueix la mida de la malla: "))
temperatura = float(input("Introdueix la Temperatura inicial: ")) #recomano una poc per sota 2.3
escombratges = int(input("Introdueix els escombratges de Montecarlo: "))
passos_temp = int(input("Punts que vols graficar "))#recomano una per poc sobre 2.3
temperatura_f=float(input("Introdueix la Temperatura final: "))
spin_array = init_spin_array(malla, malla)

#Mètode Monte Carlo:

y=[0]
x=[0]

a,b = [], []

temp_step=(temperatura_f-temperatura)/passos_temp
for temperatures in range (0, passos_temp):

   

    for i in range(0, malla):
       for j in range(0, malla):
            e0 = 0
    
    for escombratge in range(0, escombratges):
        for i in range(0, malla):
            for j in range(0, malla):
                spin_array[i, j] *= canvi()
                e1 = energy(spin_array, malla, i, j)
                q=np.exp(-1 * (e1-e0)/temperatura+temperatures*temp_step)
                def accept():
                    s = stat.bernoulli.rvs(q,size=1)
                    if s<0.5:
                        return -1
                    else:
                        return 1
                if e1 <= e0:
                    spin_array[i, j] *= 1
                
                  
                else:
                    spin_array[i, j] *= accept()
                 
        
        #print(spin_array)
        mag = sum(sum(spin_array))
        x.append(escombratge)
        y.append(mag)
        plt.plot(x[escombratge],y[escombratge])
        #print ('Magnetització: ',mag)
        magnetitzacio = np.mean(mag)
    #plt.plot(x,y)
    #plt.title('La temperatura és %s Kelvin.'%(temperatura))
    #plt.xlabel('Escombratges')
    #plt.ylabel('Magnetització')

    #plt.show()

    a.append(temperatura+temperatures*temp_step)
    b.append(magnetitzacio)



plt.plot(a,b)
axes = plt.gca()
axes.set_xlim([temperatura,temperatura_f])
plt.show()
