import pytest
import lgbt.lgbt

def test_init_class():
    temp = lgbt.lgbt(total=1)
    assert temp.__class__.__name__ == "lgbt"
