import numpy as np
import scipy.stats as stat

def init_spin_array(rows, cols):
    return np.random.choice((-1, 1), size=(rows, cols))

def find_neighbors(spin_array, malla, x, y):
    left = (x , y - 1 if y - 1 > 0 else malla - 1)
    right = (x, y + 1 if y + 1 < (malla - 1) else 0)
    bottom = (x - 1 if x - 1 > 0 else malla - 1, y)
    top = (x + 1 if x + 1 < (malla - 1) else 0, y)

    return [spin_array[left[0], left[1]],
            spin_array[right[0], right[1]],
            spin_array[top[0], top[1]],
            spin_array[bottom[0], bottom[1]]]

def energy(spin_array, malla, x ,y):
    return -1*spin_array[x, y]*sum(find_neighbors(spin_array, malla, x, y))


def canvi():#funció que fa canviar aleatòriament un spin amb probabilitat 0.5
    r = stat.bernoulli.rvs(0.5,size=1)
    if r<0.5:
        return 1
    else:
        return -1
    
axes = plt.gca()