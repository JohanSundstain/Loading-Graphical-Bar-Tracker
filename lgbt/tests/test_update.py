import lgbt.lgbt

import pytest

   

def test_with_total():
	try:
		temp = lgbt.lgbt(total=100)
	except TypeError:
		assert False
	else:
		assert True
