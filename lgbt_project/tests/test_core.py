import time

from lgbt.core import lgbt
from gui_test import gui_test
from lgbt.consts import HEROES, BIG_FLAGS, HAND_KEYS

modes = lgbt.modes()

def test_heroes():
	assert lgbt.heroes() == list(HEROES.keys())

def test_modes():
	assert lgbt.modes() == list(BIG_FLAGS.keys())

@gui_test
def test_legacy():
	for m in modes:
		for i in lgbt(range(100), desc=f'{m}',mode=m):
			time.sleep(0.01)

@gui_test
def test_advanced():
	import math
	x = lgbt.tracker()
	dx = 0.2
	y = 0.0
	for m in modes:
		x.item = 0.0
		for i in lgbt(range(1000), desc=f'Cosinus',mode=m, tracker=x, fix=False):
			x.item = math.cos(y)
			y += dx
			time.sleep(0.1)
			lgbt.step(x)


@gui_test
def test_update():
	bar = lgbt(total=100)
	for i in range(100):
		time.sleep(0.1)
		bar.update(1)


if __name__ == "__main__":
	#test_heroes()
	#test_modes()
	#test_legacy()
	test_advanced()
	#test_update()
