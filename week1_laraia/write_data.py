import numpy as np
filename = 'box.txt'
X,Y = [1,2,2,1],[1,1,2,2]

f=open(filename, 'w')
for x, y in zip(X,Y):
    f.write(f'{x},{y}\n')
f.close()
