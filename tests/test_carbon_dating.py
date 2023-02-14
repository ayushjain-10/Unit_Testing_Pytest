import unittest
import pytest
import math
from ..carbon_dating import get_age_carbon_14_dating

# Write a unit test which feed 0.35 to the function.
# The result should be '8680.34'. Does the function handles
# every possible input correctly? What if the input is zero
# or negative?
# Add the necessary logic to make sure the function handle
# every possible input properly. Then write a unit test againt
# this special case.

def test_get_age_carbon_14_dating():
    # test the get_age_carbon_14_dating function with mock data
    carbon_14_ratio = 0.35
    age = get_age_carbon_14_dating(carbon_14_ratio)
    # remove all numbers after two decimal places
    age = math.trunc(age*100)/100
    assert age == 8680.34

# test for if carbon_14_ratio is zero return exception
def test_get_age_carbon_14_dating_exception():
    carbon_14_ratio = 0
    with pytest.raises(ValueError):
        age = get_age_carbon_14_dating(carbon_14_ratio)

# test for if carbon_14_ratio is negative return exception
def test_get_age_carbon_14_dating_exception_negitive():
    carbon_14_ratio = -1
    with pytest.raises(ValueError):
        age = get_age_carbon_14_dating(carbon_14_ratio)

