import pytest

from src.data_structures.arrays.static_array import StaticArray


def test_removeEnd():
    # arrange
    array = [1, 4, 6, 9]
    static_array = StaticArray(array)

    # act
    new_array = static_array.removeEnd()

    # assert
    assert new_array == [1, 4, 6, 0]
  
  # TO-DO broken
def test_removeMiddle():
    # arrange
    array = [1, 4, 6, 9]
    index = 0
    static_array = StaticArray(array)

    # act
    new_array = static_array.removeMiddle(i=index)

    # assert
    assert new_array == [4, 6, 9, None]
    
    # arrange
    array = [1, 4, 6, 9]
    index = 2
    static_array = StaticArray(array)

    # act
    new_array = static_array.removeMiddle(i=index)

    # assert
    assert new_array == [1, 4, 9, None]

def test_insertEnd():
    # arrange
    array = [1, 4, 6, None]
    element_to_insert = 9
    static_array = StaticArray(array)

    # act
    new_array = static_array.insertEnd(n=element_to_insert)

    # assert
    assert new_array == [1, 4, 6, 9]

def test_insertMiddle():
    # arrange
    array = [1, 4, 6, None]
    element_to_insert = 11
    index = 0
    static_array = StaticArray(array)

    # act
    new_array = static_array.insertMiddle(i=index, n=element_to_insert)

    # assert
    assert new_array == [11, 1, 4, 6]

    # arrange
    array = [1, 4, 6, None]
    element_to_insert = 11
    index = 2
    static_array = StaticArray(array)

    # act
    new_array = static_array.insertMiddle(i=index, n=element_to_insert)

    # assert
    assert new_array == [1, 4, 11, 6]

def test_valueCount():
    # arrange
    array = [1, 4, 6, None]
    static_array = StaticArray(array)

    # act
    value_count = static_array.valueCount()

    # assert
    assert value_count == 3

    # arrange
    array = [1, 4, 6, 9]
    static_array = StaticArray(array)

    # act
    value_count = static_array.valueCount()

    # assert
    assert value_count == 4
