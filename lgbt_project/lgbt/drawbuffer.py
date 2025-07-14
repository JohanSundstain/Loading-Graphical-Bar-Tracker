import os
import time
import sys


class Brush():
	def __init__(self):
		self._var = 10
		self._buffer = []

def say_fast():
	buffer = []
	for i in range(1000):
		buffer.append("hello this is some big and long long long text ")
	sys.stdout.write("".join(buffer))

def say():
	for i in range(1000):
		sys.stdout.write("hello this is some big and long long long text ")

if __name__ == "__main__":
	start = time.time() 
	say_fast()
	end = time.time() - start
	print("")
	print(end)