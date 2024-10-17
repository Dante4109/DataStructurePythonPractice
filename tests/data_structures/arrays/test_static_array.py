import pytest
from Data_Structures.Arrays.static_array import StaticArray

static_array = StaticArray()

def test_case_1_slow():
    # arrange
    array = [1, 4, 6, 9]

    # act
    array = static_array.removeEnd()

    # assert
    assert array == [1, 4, 6]
