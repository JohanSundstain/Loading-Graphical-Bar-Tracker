import time
import inspect

from lgbt.consts import FLAGS
from lgbt.bar import Bar

class lgbt():	

	@staticmethod
	def modes():
		return list(FLAGS.keys())

	def __init__(self, iterable, total=None, miniter=2500,  mininterval=0.1, **kwargs):
		self._iterable = iterable

		if inspect.isgenerator(self._iterable):
			if total == None:
				raise ValueError('The generator was received, but the total is not specified')
		try:
			if total == None:
				total = len(self._iterable)
		except TypeError:
			total = 0.0

		self._miniter = miniter
		self._mininterval = mininterval
		self._current_iter = 0
		self._is_end = False

		self._miniter = max(1, round(total/self._miniter))

		self._bar = Bar(total=total, **kwargs)


	@property
	def iterable(self):
		return self._iterable
	
	@iterable.setter
	def iterable(self, value):
		self._iterable = value

	def update(self, n=1):
		self._current_iter += n
		if self._is_end:
			return
		if self._current_iter > self._total:
			self._is_end = True
			print("")
			return
		
		self._draw()


	def _draw(self):
		self._bar.update(self._current_iter)
		self._bar.draw()
		self._bar.flush()

	def __call__(self, iterable, **kwargs):
		self.__init__(iterable, **kwargs)
		return self
	
	def __iter__(self):
		"""
		Progress bar
		iterable    - list of elements
		desc        - description
		miniter    - minimal iterations between update screen
		placeholder - symbol which used in progress bar 
		hero        - сhoose your smiley face
		"""

		last_update = time.perf_counter()

		for self._current_iter, data in enumerate(self._iterable, 1):
			yield data
			interval = time.perf_counter() - last_update

			if self._current_iter % self._miniter == 0 or interval >= self._mininterval:
				self._draw()
				last_update = time.perf_counter()
		print("")