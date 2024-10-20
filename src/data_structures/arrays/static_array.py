#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python does not actually have arrays so we will use lists instead. 

class StaticArray():
  def __init__(self, arr: list):
        self.arr = arr
        self.length = len(arr)
        # Set length as capacity because python does not support static arrays.
        self.capacity = self.length
        self.value_count = self.valueCount()


  def removeEnd(self) -> list:
    """
    Overwrite last element with some default value.
    Big O time complexity: O(1)
    """
    if self.length > 0:
        
        # We would also consider the length to be decreased by 1.
        self.arr[self.length - 1] = 0        
    return self.arr

  def removeMiddle(self, i: int) -> list:
      """
      Remove value at index i before shifting elements to the left.
      Assuming i is a valid index.
      """
      # Shift starting from i + 1 to end.
      for index in range(i + 1, self.length):
          self.arr[index - 1] = self.arr[index]
      # No need to 'remove' arr[i], since we already shifted
      # remove last item
      self.arr[self.length - 1] = None
      return self.arr

  def insertEnd(self, n: int)-> list:
    """ Insert n into arr at the next open position.
    value_count is the number of 'real' values in arr, and capacity
    is the size (aka memory allocated for the fixed size array).
    """
    if self.value_count < self.capacity:
      self.arr[self.length - 1] = n
    return self.arr
  
  def insertMiddle(self, i: int, n: int) -> list:
      """
      Insert n into index i after shifting elements to the right.
      Assuming i is a valid index and arr is not full.
      """
      # Shift starting from the end to i.
      for index in range(self.value_count - 1, i - 1, -1):
          self.arr[index + 1] = self.arr[index]
      
      # Insert at i
      self.arr[i] = n
      return self.arr


  def valueCount(self) -> int:
    """
    Get number of real values in an array. 
    """
    value_count = 0
    for i in range(len(self.arr)):
      current_element = self.arr[i]
      if current_element != None:
          value_count = value_count + 1
    return value_count
