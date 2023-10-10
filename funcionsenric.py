import numpy as np
import scipy.stats as stat

#Crea la matriu inicial al atzar.

def initial_matrix(rows, cols):
    return np.random.choice((-1, 1), size=(rows, cols))

#Matriu de zeros.

def zeros_matrix(rows, cols):
    return np.random.choice((0, 0), size=(rows, cols))

# Defineix les condicions cícliques.

def find_neighbors(spin_array, malla, x, y): 
    left = (x , y - 1 if y - 1 > 0 else malla - 1)
    right = (x, y + 1 if y + 1 < (malla - 1) else 0)
    bottom = (x - 1 if x - 1 > 0 else malla - 1, y)
    top = (x + 1 if x + 1 < (malla - 1) else 0, y)

    return [spin_array[left[0], left[1]],
            spin_array[right[0], right[1]],
            spin_array[top[0], top[1]],
            spin_array[bottom[0], bottom[1]]]

# Calcula l'energia 

def energia(spin_array, malla, x ,y):
    return -1*spin_array[x, y]*sum(find_neighbors(spin_array, malla, x, y))

#Modifica l'spin amb una probabilitat del 50%
    
def canvi():
    r = stat.bernoulli.rvs(0.5,size=1)
    if r<0.5:
        return 1
    else:
        return -1
