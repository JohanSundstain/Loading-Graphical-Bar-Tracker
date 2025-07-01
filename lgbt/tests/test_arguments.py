import pytest
import lgbt

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
    assert temp.total == 100

def test_init_list():
    temp = lgbt.lgbt([0,1,2,3,4,5,6,7,8,9])
    assert temp.total == 10

def test_gen_run():
    temp = lgbt.lgbt(my_gen(100), total=100)
    print("Running with generator:")
    for i in temp:
        pass

def test_list_run():
    temp = lgbt.lgbt([0,1,2,3,4,5,6,7,8,9])
    print("Running with list:")
    for i in temp:
        pass

def test_gen_run_miniters():
    temp = lgbt.lgbt([0,1,2,3,4,5,6,7,8,9], miniters=100)
    print("Running with miniters:")
    for i in temp:
        pass
    
def test_gen_run_hero():
    temp = lgbt.lgbt([0,1,2,3,4,5,6,7,8,9], hero='tralalero')
    print("Running with miniters:")
    for i in temp:
        pass

