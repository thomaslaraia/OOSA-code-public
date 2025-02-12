
'''
A class to build on 
and produce a binary
search algorithm
'''

import numpy as np
from sys import exit
from matplotlib import pyplot as plt

#####################################

class dataSorter(object):
  '''A class to hold data and provide examples of search algorithms'''

  def __init__(self,numb=100):
    '''Class initialiser'''
    self.numb=numb
    self.arr=np.random.random((numb))

  def sortArray(self):
    '''Sort an array of data'''
    self.sorted=np.sort(self.arr)
    return

  def plot(self):
    plt.figure()
    plt.plot(self.arr, 'b-')
    plt.plot(self.sorted, 'r-')
    plt.savefig('plotted.png')
