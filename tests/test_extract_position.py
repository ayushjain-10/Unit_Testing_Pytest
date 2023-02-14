import pytest
from ..extract_position import extract_position

def test_extract_position():
    """Test extract_position function."""
    line = '|error| numerical calculations could not converge.'
    assert extract_position(line) == None
    line2 = '|update| the positron location in the particle accelerator is x:21.432'
    assert extract_position(line2) == '21.432'

def test_extract_position_exception():
    """Test extract_position function."""
    line = ''
    # pos = none
    assert extract_position(line) == None
