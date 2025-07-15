import time 
import os

from lgbt.basicobjects import TextLabel, Bar, ClassicBar, LegacyBar, CPUBar, GPUBar
from lgbt.consts import BIG_FLAGS
from lgbt.core import lgbt

from gui_test import gui_test

modes = lgbt.modes()

@gui_test
def test_textlabel():
	tl = TextLabel("Hello world", coord=(1, 2))
	for i in range(100):
		tl.update(i)
		tl.draw()
		tl.flush()
		time.sleep(0.1)

@gui_test
def test_bar():
	line = 2
	for m in modes:
		b = Bar(total=10, mode=m, type='long',coord=(1, line))
		for i in range(1, 11):
			b.update(i)
			b.draw()
			b.flush()
			time.sleep(0.1)
		line += 1 

@gui_test
def test_classic_bar():
	line = 2
	for m in modes:
		b = ClassicBar(total=100, mode=m, type='short',coord=(1, line))
		for i in range(1, 101):
			b.update(i)
			b.draw()
			b.flush()
			time.sleep(0.01)
		line += 1 

@gui_test
def test_legacy_bar():
	line = 2
	for m in modes:
		b = LegacyBar(total=100, mode=m, type='long')
		for i in range(1, 101):
			b.update(i)
			b.draw()
			b.flush()
			time.sleep(0.01)
		print("")

@gui_test
def test_cpu_bar():
	b = CPUBar(coord=(1,2))
	for i in range(1, 101):
		b.update()
		b.draw()
		b.flush()
		time.sleep(0.1)

@gui_test
def test_cpu_bar():
	b = CPUBar(coord=(1,2))
	for i in range(1, 101):
		b.update()
		b.draw()
		b.flush()
		time.sleep(0.1)

@gui_test
def test_gpu_bar():
	b = GPUBar()
	for i in range(1, 101):
		b.update()
		b.draw()
		b.flush()
		time.sleep(0.1)

if __name__ == "__main__":
	#test_textlabel()
	#test_bar()
	#test_classic_bar()
	test_legacy_bar()
	#test_cpu_bar()
	#test_gpu_bar()