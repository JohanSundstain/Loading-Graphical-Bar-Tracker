import pytest
import lgbt.lgbt

def my_gen(max):
    current = 0
    while current < max:
        yield current
        current += 1

def test_init_gen_without_total():
    try:  
        temp = lgbt.lgbt(my_gen(100))
    except (ValueError):
        assert True
    else:
        assert False

def test_init_gen():
    temp = lgbt.lgbt(my_gen(100), total=100)
    assert temp._total == 100

def test_init_list():
    temp = lgbt.lgbt([0,1,2,3,4,5,6,7,8,9])
    assert temp._total == 10





