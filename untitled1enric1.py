import matplotlib.pyplot as plt
import scipy.stats as stat
import numpy as np
from funcionsenric import*

#Introduim els paràmetres que volem controlar:

rang_matriu = int(5)
temperature = float(input("Introdueix la Temperatura inicial: "))
passos = int(input("Introdueix el nombre de passos de l'algoritme de Metropolis: "))
x=[0]
y=[0]

#definim la matriu quadrada 20x20

spin_array = initial_matrix(rang_matriu, rang_matriu) #Matriu random
spin_array0 = zeros_matrix(rang_matriu, rang_matriu)

#Apliquem l'algoritme de Metròpolis:
# 1. Partim de la matriu d'spins a l'atzar. Calculem l'energia e0 d'aquest estat:

for i in range(0, rang_matriu):
   for j in range(0, rang_matriu):
        e0 = energia(spin_array, rang_matriu, i, j)
        
#2. Apliquem l'algoritme en si

for k in range(0, passos):
    
    for i in range(0, rang_matriu):
        
        for j in range(0, rang_matriu):
            
            spin_array0[i, j] = spin_array[i, j]
            spin_array[i, j] = spin_array[i, j] * canvi()       #Apliquem el canvi aleatori a la matriu
            e1 = energia(spin_array, rang_matriu, i, j)         #Calculem la nova energia deguda al canvi
            q=np.exp(-1 * (e1-e0)/temperature)                  #Calculem la funció de partició
            
            #Funció que accepta amb una certa probabilitat
            
            def accept():                                       
                return stat.bernoulli.rvs(q,size=1)
                
            if e1 <= e0:
                spin_array[i, j] *= 1
              
            else:
                if accept() < 0.5:
                    spin_array[i, j] = spin_array0[i, j]
                    
                else:
                    spin_array[i, j] *= 1
               
    
    #print(spin_array)
    mag = sum(sum(spin_array))
    x.append(k)
    y.append(mag)
    plt.plot(x[k],y[k])
    #print ('Magnetització: ',mag)

   # a.append(t_step)
   # b.append(rang)

plt.plot(x,y)
plt.title('La TEMPERATURA és igual a %s K'%(temperature))
plt.xlabel('Temps (passos)')
plt.ylabel('Magnetització')

plt.show()