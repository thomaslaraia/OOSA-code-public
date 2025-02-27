# Identify start and end nodes from a list of nodes

# Identify the node that is the furthest perpendicularly from the line
# connecting them

# If the distance from the line is beyond a threshold, that node subdivides
# the polyline, and we call function recursively twice with (start,mid) and
# (mid,end)

# If distance from line is within the threshold, returns that no
# subdivision occurs

# Need to keep track of which nodes have been subdivided on

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('../week3/data/squirrel.csv')

print(data.sort_values('time'))

#def douglar_peucker(nodes):
