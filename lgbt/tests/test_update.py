import lgbt.lgbt
import pytest
import lgbt

def test_without_total():
	try:
		temp = lgbt.lgbt()
	except TypeError:
		assert True
	else:
		assert False
   

def test_with_total():
	try:
		temp = lgbt.lgbt(total=100)
	except TypeError:
		assert False
	else:
		assert True
