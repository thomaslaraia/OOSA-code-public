import numpy as np
spaces = []
for i in range(1,9):
    for j in range(1,9):
        spaces.append((i,j))
for i in range(len(spaces)):
    for j in range(i+1,len(spaces)):
        print(f'Distance from {spaces[i]} to {spaces[j]}: {np.sqrt((spaces[i][0]-spaces[j][0])**2+(spaces[i][1]-spaces[j][1])**2)}')
