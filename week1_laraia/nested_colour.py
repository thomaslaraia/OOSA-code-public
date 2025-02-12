import numpy as np
spaces = []
for i in range(1,9):
    for j in range(1,9):
        spaces.append((i,j))
for space in spaces:
    if space[0]%2 == space[1]%2:
        colour = 'black'
    else:
        colour = 'white'
    print(f'{space} is {colour}')
