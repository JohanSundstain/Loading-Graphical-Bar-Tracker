import time

from lgbt.core import lgbt
from gui_test import gui_test
from lgbt.histogram import Histogram, Window

@gui_test
def test_histogram():
	import math
	h = Histogram(coord=(1,2), fix=False)
	x = 0.0
	dx = 0.2
	for i in range(100):
		h.update(math.cos(x))	
		h.draw()
		h.flush()
		x += dx
		time.sleep(0.1)
		h.next()

@gui_test
def test_window():
	import math
	h = Histogram(fix=False)
	w = Window(h, coord=(1,2))
	x = 0.0
	dx = 0.25
	for i in range(1, 101):
		w.update(math.cos(x))	


		w.draw()
		w.flush()


		x += dx
		time.sleep(0.1)
		w.next()

if __name__ == "__main__":
	#test_histogram()
	test_window()