import unittest
from unittest import mock
import pytest
import math
# import all functions from calculate_grades.py
from ..calculate_grades import *

def test_calculate_stat():
    # test the calculate_stat function with mock data
    grade_list = [1, 2, 3, 4, 5]
    mean, sd = calculate_stat(grade_list)
    assert mean == 3
    assert sd == math.sqrt(2)


def test_read_input():
    """Test read_input function."""
    with mock.patch('builtins.input', side_effect=[1, 2, 3, 4, 5]):
        grade_list = read_input()
        assert grade_list == [1, 2, 3, 4, 5]

# test for if grade_list has a string return exception
def test_read_input_exception():
    with mock.patch('builtins.input', side_effect=['a', 2, 3, 4, 5]):
        with pytest.raises(ValueError):
            grade_list = read_input()

# test for if grade_list has a negative number return exception
def test_read_input_exception():
    with mock.patch('builtins.input', side_effect=[-1, 2, 3, 4, 5]):
        with pytest.raises(ValueError):
            grade_list = read_input()
