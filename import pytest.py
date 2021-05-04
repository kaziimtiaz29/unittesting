import pytest
import count

def test_count_zeros():
    assert count.count([0,0,0], 0) == 3

def test_count_string():
    assert count.count(["a","a","a"], "a") == 3

def test_count_normalNum():
	assert count.count([1,2,3,4,5,6,6,5,4,3,2,1], 1)==2


print(test_count_string())
print(test_count_zeros())
print(test_count_normalNum())
