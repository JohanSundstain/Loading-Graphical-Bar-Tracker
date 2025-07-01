import time
import sys
import inspect

from bar import CommonBar


class lgbt():
	def __init__(self, iterable=None, desc="", miniters=2500, minintervals=0.1, hero='rainbow', total=None, mode='default', type=None):
		self.iterable = iterable
		self.total = total
		if inspect.isgenerator(self.iterable):
			if self.total == None:
				raise ValueError('The generator was received, but the total is not specified')
		
		if self.total == None:
			self.total = len(self.iterable)
		self.miniters = miniters
		self.minintervals = minintervals

		if type == None:
			self.bar = CommonBar(total=self.total, hero=hero, desc=desc, mode=mode)
		else:
			self.bar = type

		self.start = None
		self.current_iter = 0
		self.is_end = False

		self.miniters = max(1, round(self.total/self.miniters))

	def update(self, n=1):
		self.iterations += n
		if self.is_end:
			return
		if self.iterations > self.total:
			self.is_end = True
			sys.stdout.write("\n")
			return
		if self.start == None:
			self.start = time.perf_counter()
		self._draw()

	
	def _draw(self):
		total_time = time.perf_counter() - self.start
		sys.stdout.write(self.bar.show(total_time=total_time, current_iter=self.current_iter))
		sys.stdout.flush()


	def __call__(self, iterable, **kwargs):
		self.__init__(iterable, **kwargs)
		return self
	

	def __iter__(self):
		"""
		Progress bar
		iterable    - list of elements
		desc        - description
		miniters    - minimal iterations between update screen
		placeholder - symbol which used in progress bar 
		hero        - сhoose your smiley face
		"""

		self.start = time.perf_counter()
		last_update = self.start

		for self.current_iter, data in enumerate(self.iterable, 1):
			yield data
			interval = time.perf_counter() - last_update

			if self.current_iter % self.miniters == 0 or interval >= self.minintervals:
				self._draw()
				last_update = time.perf_counter()
		sys.stdout.write("\n")
