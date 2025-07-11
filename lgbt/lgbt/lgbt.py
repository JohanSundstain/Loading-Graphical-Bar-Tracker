import time
import sys
import inspect
import os

from .bar import DynemicBar, AdvancedBar
from .basicobjects import Tracker


class lgbt():
	tracked = False
	@staticmethod
	def tracker():
		return Tracker(0.0)

	def __init__(self, iterable=None, total=None, desc="", miniters=2500, minintervals=0.1, hero='rainbow', mode='default'):
		self._iterable = iterable
		self._total = total
		if inspect.isgenerator(self._iterable):
			if self._total == None:
				raise ValueError('The generator was received, but the total is not specified')
			
		try:
			if self._total == None:
				self._total = len(self._iterable)
		except TypeError:
			self._total = 0.0

		self._miniters = miniters
		self._minintervals = minintervals
		self._current_iter = 0
		self._is_end = False
		self._bar = DynemicBar(total=self._total, hero=hero, desc=desc, mode=mode)
		self._miniters = max(1, round(self._total/self._miniters))

	def __init__tracker__(self, iterable=None, total=None, desc="", miniters=2500, minintervals=0.1, hero='rainbow', mode='default', tracker=None):
		if lgbt.tracked:
			raise PermissionError("The object has already been created")
		else:
			os.system("cls")
			lgbt.tracked = True

		self._iterable = iterable
		self._total = total
		if inspect.isgenerator(self._iterable):
			if self._total == None:
				raise ValueError('The generator was received, but the total is not specified')
			
		if self._total == None:
			self._total = len(self._iterable)

		self._miniters = miniters
		self._minintervals = minintervals

		if type(tracker) == Tracker:
			self._tracker = tracker
			self._bar = AdvancedBar(total=self._total, hero=hero, desc=desc, mode=mode)
		else:
			raise ValueError("Invalid type of tracker")

		self._current_iter = 0
		self._is_end = False

		self._miniters = max(1, round(self._total/self._miniters))

	def next(self):
		if not lgbt.tracked:
			raise PermissionError("There is no tracker")
		self._bar.next()

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
		if lgbt.tracked:
			self._bar.update_value(self._tracker.item)
		self._bar.draw()

	@property
	def iterable(self):
		return self._iterable

	@iterable.setter
	def iterable(self, value):
		self._iterable = value

	def __call__(self, iterable, **kwargs):
		tracker = kwargs.get('tracker', None)
		if (not lgbt.tracked) and (tracker != None):
			self.__init__tracker__(iterable, **kwargs)
		elif tracker == None:
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

		last_update = time.perf_counter()

		for self._current_iter, data in enumerate(self._iterable, 1):
			yield data
			interval = time.perf_counter() - last_update

			if self._current_iter % self._miniters == 0 or interval >= self._minintervals:
				self._draw()
				last_update = time.perf_counter()
		print("")
