#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python does not actually have arrays so we will use lists instead. 

class StaticArray():
  def __init__(self, arr: list):
        self.arr = arr
        self.length = len(arr)

  def removeEnd(arr: list, length: int) -> list:
    """
    Overwrite last element with some default value.
    """
    if length > 0:
        
        # We would also consider the length to be decreased by 1.
        arr[length - 1] = 0
    return arr

  def removeMiddle(arr: list, i: int, length: int) -> list:
      """
      Remove value at index i before shifting elements to the left.
      Assuming i is a valid index.
      """
      # Shift starting from i + 1 to end.
      for index in range(i + 1, length):
          arr[index - 1] = arr[index]
      # No need to 'remove' arr[i], since we already shifted
      return arr

  
  def insertEnd(arr: list, n: int, length: int, capacity: int)-> list:
    """ Insert n into arr at the next open position.
    Length is the number of 'real' values in arr, and capacity
    is the size (aka memory allocated for the fixed size array).
    """
    if length < capacity:
      arr[length] = n
    return arr

