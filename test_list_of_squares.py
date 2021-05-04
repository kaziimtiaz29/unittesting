import pytest
import list_of_squares

def test_sqaures():
    assert list_of_squares.list_of_squares(2) == {1:1 , 2:4}

print(test_sqaures())