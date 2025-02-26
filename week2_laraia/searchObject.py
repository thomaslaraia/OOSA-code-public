
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
    #plt.plot(self.arr, 'b-')
    plt.plot(self.sorted, 'r-')
    plt.savefig('plotted.png')

  def plot_with_threshold(self):
    plt.figure()
    plt.plot(self.sorted, 'r-')
    plt.plot([self.threshold,self.threshold],[0,1], 'b--')
    plt.savefig('plotted_with_threshold.png')

  def binarySearch(self,target):
    S = self.sorted.copy()
    #print(S)
    indices = np.arange(len(S))
    while len(S) >= 3:
      index = round((len(S)-1)/2)
      a = S[index]
      if a == target:
        S = indices[index]
      elif a <= target:
        S = S[index:]
        indices = indices[index:]
      else:
        S = S[:index+1]
        indices = indices[:index+1]
    if len(S) == 2:
      if S[0] == target:
        self.threshold = indices[0]
      elif S[1] == target:
        self.threshold = indices[1]
      else:
        midpoint = (target - S[0])/(S[1] - S[0])
        self.threshold = indices[0] + midpoint

  def binaryRecursion(self, target, left, right):
  '''Performs a binary search on a sorted array recursively'''
    print(self.sorted, target, left, right)
    index = (left+right)//2
    value = self.sorted[index]

    if (right - left) <= 1:
      midpoint = (target - self.sorted[left])/(self.sorted[right] - self.sorted[left])
      #print(target, left, right)
      #print(index,midpoint)
      self.threshold = index + midpoint
      print(self.threshold)
      return

    if value < target:
      self.binaryRecursion(target,index,right)
    elif value > target:
      self.binaryRecursion(target,left,index)
    else:
      print(index)
      self.threshold = index
      return

if __name__ == '__main__':

  array = dataSorter(10)
  array.sortArray()
  #array.binarySearch(0.5)
  array.binaryRecursion(0.5,0,array.numb-1)
  array.plot_with_threshold()
