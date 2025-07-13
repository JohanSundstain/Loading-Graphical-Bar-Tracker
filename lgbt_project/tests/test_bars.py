from lgbt.core import lgbt
import time

def test_advanced():
	import math
	func = lambda x: math.cos(x)
	y = 0.0
	dx = 0.25
	x = lgbt.tracker()
	for e in range(10):
		x.item = 0.0
		for i in lgbt(range(50000), desc="COS", mode='ita', tracker=x):
			x.item = func(y)
			y += dx
			lgbt.step(x)
			time.sleep(0.1)

if __name__ == "__main__":
	test_advanced()