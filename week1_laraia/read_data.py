import numpy as np
from matplotlib import pyplot as plt
filename = 'Wiggle1.txt'
x,y = np.loadtxt(filename, unpack=True, dtype=float, delimiter=',', usecols=(0,1))

plt.scatter(x,y)
plt.savefig('read_data.png')
