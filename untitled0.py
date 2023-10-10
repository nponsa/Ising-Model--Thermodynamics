import matplotlib.pyplot as plt
import scipy.stats as stat
#import matplotlib as mpl
import numpy as np
#import matplotlib.mlab as mlab
#import math
import random
#from scipy.stats import norm


def init_spin_array(rows, cols):
    return np.random.choice((-1, 1), size=(rows, cols))

def find_neighbors(spin_array, lattice, x, y):
    left = (x , y - 1 if y - 1 > 0 else lattice - 1)
    right = (x, y + 1 if y + 1 < (lattice - 1) else 0)
    bottom = (x - 1 if x - 1 > 0 else lattice - 1, y)
    top = (x + 1 if x + 1 < (lattice - 1) else 0, y)

    return [spin_array[left[0], left[1]],
            spin_array[right[0], right[1]],
            spin_array[top[0], top[1]],
            spin_array[bottom[0], bottom[1]]]

def energy(spin_array, lattice, x ,y):
    return -1*spin_array[x, y]*sum(find_neighbors(spin_array, lattice, x, y))

p=0.5
def canvi():#funció que fa canviar estocàsticament un spin.
    r = stat.bernoulli.rvs(p,size=1)
    if r<0.5:
        return 1
    else:
        return -1


lattice = int(input("Enter lattice size: "))
temperature = float(input("Enter the temperature: "))
sweeps = int(input("Enter the number of Monte Carlo Sweeps: "))
spin_array = init_spin_array(lattice, lattice)

#Mètode Monte Carlo:

y=[0]
x=[0]

for i in range(lattice):
       for j in range(lattice):
            e0 = energy(spin_array, lattice, i, j)

for sweep in range(sweeps):
    for i in range(lattice):
        for j in range(lattice):
            spin_array[i, j] *= canvi()
            e1 = energy(spin_array, lattice, i, j)
            q=np.exp(-1 * (e1-e0)/temperature)
            def accept():#funció que accepta un canvi.
                s = stat.bernoulli.rvs(q,size=1)
                if s<0.5:
                    return -1
                else:
                    return 1
            if e1 <= e0:
                spin_array[i, j] *= 1
            
#            elif np.exp(-1 * (e1-e0)/temperature) > random.randint(0, 1):
#                spin_array[i, j] *= -1
            else:
                spin_array[i, j] *= accept()
#            else:
#                spin_array[i, j] *= +1
    
   # print(spin_array)
    mag = sum(sum(spin_array))
    x.append(sweep)
    y.append(mag)
    plt.plot(x[sweep],y[sweep])
    #data.append(sweep)
    #print ('Magnetització: ',mag)


plt.plot(x,y)
plt.suptitle('La temperatura és %s Kelvin.'%(temperature))
plt.xlabel('Passos')
plt.ylabel('Magnetització')

plt.show()