import time

from lgbt.core import lgbt
from gui_test import gui_test
from lgbt.bars import StatBar, AdvancedBar, DynemicBar

modes = lgbt.modes()

@gui_test
def test_advanced():
	import math
	func = lambda x: math.cos(x)
	y = 0.0
	dx = 0.25
	for m in modes:
		a = AdvancedBar(100, "test advanced", "histogram", coord=(1,2), mode=m)
		for i in range(1, 101):
			a.update(i)
			a.update_tracker(func(y))

			a.draw()
			a.flush()
			a.next()
			y += dx
			time.sleep(0.01)

@gui_test
def test_dynemic():
	for m in modes:
		d = DynemicBar(total=100, desc="Test dynemic bar", mode=m)
		for i in range(1, 101):
			d.update(i)
			d.draw()
			d.flush()
			time.sleep(0.01)
		print("")

@gui_test
def test_stat():
	for m in modes:
		s = StatBar(total=100, desc="test stat func", mode=m, coord=(4,5))
		for i in range(1, 101):
			s.update(i)
			s.draw()
			s.flush()
			time.sleep(0.1)

if __name__ == "__main__":
	test_advanced()
	#test_stat()
	#test_dynemic()