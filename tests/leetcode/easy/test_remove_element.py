import pytest
from src.leetcode.easy import remove_element

sol = remove_element.Solution()


def test_case_1_slow():
    # arrange
    nums = [3, 2, 2, 3]

    # act
    sol.removeElementSlow(nums, 3)

    # assert
    assert nums == [2, 2]


def test_case_2_slow():
    # arrange
    nums = [0, 1, 2, 2, 3, 0, 4, 2]

    # act
    sol.removeElementSlow(nums, 2)

    # assert
    assert nums == [0, 1, 3, 0, 4]


def test_case_1_fast():
    # arrange
    nums = [3, 2, 2, 3]

    # act
    sol.removeElementFast(nums, 3)

    # assert
    assert nums == [2, 2]


def test_case_2_fast():
    # arrange
    nums = [0, 1, 2, 2, 3, 0, 4, 2]

    # act
    sol.removeElementFast(nums, 2)

    # assert
    assert nums == [0, 1, 3, 0, 4]
