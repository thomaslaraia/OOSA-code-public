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
import argparse

def perp_dist(x1, x2, x3, y1, y2, y3):
  '''
  This function returns the perpendicular distance from a point to a line segme>
    
  (x1,y1) and (x2,y2) define the start and end points of your line.
  (x3, y3) defines a point.
  '''
  if x2==x1:
    return abs(x3-x1)
  m = (y2-y1)/(x2-x1)
  c = y1-m*x1
  d = abs(m*x3 - y3 + c)/(m**2 + 1)**0.5
  return d


#filename = '../week3/data/squirrel.csv'
#data = pd.read_csv(filename)
#print(data.lon[0])


class squirrel:

    def __init__(self, gps_file):
        gps_data = pd.read_csv(gps_file)
        gps_data = gps_data.sort_values('time').reset_index()
        self.x = gps_data.lon
        self.y = gps_data.lat
        self.time = gps_data.time
        self.simple = [len(self.x)-1]

    def douglas_peucker(self, start, end, threshold):
        start_node = (self.x[start], self.y[start])
        end_node = (self.x[end], self.y[end])

        max_distance = 0
        if end - start <= 1:
            self.simple.insert(-1,start)
            return
        for i in range(start+1, end):
            mid_node = (self.x[i], self.y[i])
#            print(a,b)
#            print(a[0],b[0],a[1],b[1])
            d=perp_dist(start_node[0],end_node[0],mid_node[0],
                        start_node[1],end_node[1],mid_node[1])
            #print(d)
            if d > max_distance:
                max_distance = d
                index = i
        if max_distance < threshold:
            self.simple.insert(-1,start)
            return
        else:
            self.douglas_peucker(start,index,threshold)
            self.douglas_peucker(index,end,threshold)
        return

    def plot_squirrel(self):
        plt.figure()
        plt.plot(self.x,self.y,'b-')
        plt.show()

    def plot_both(self):
        plt.figure()
        plt.plot(self.x,self.y,'b-')
        x_simple = [self.x[i] for i in self.simple]
        y_simple = [self.y[i] for i in self.simple]
        plt.plot(x_simple,y_simple,'r-')
        plt.show()

if __name__ == '__main__':

    p = argparse.ArgumentParser()
    p.add_argument('--threshold', type=float, default=.001)
    args = p.parse_args()

    filename = '../week3/data/squirrel.csv'
    Alvin = squirrel(filename)
    Alvin.douglas_peucker(0,len(Alvin.x)-1,args.threshold)
    print(Alvin.simple)
    Alvin.plot_both()
