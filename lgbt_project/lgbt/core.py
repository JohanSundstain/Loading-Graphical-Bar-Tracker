import time
import inspect
import os

from lgbt.bars import DynemicBar, AdvancedBar
from lgbt.basicobjects import Tracker
from lgbt.consts import HEROES, BIG_FLAGS

class lgbt():
	__instances = {}

	@staticmethod
	def tracker():
		return Tracker(0.0)
	
	@staticmethod
	def step(tracker):
		if type(tracker) != Tracker:
			raise ValueError("Invalid type of tracker")
		lgbt.__instances[id(tracker)]._next()
	
	@staticmethod
	def heroes():
		return list(HEROES.keys())

	@staticmethod
	def modes():
		return list(BIG_FLAGS.keys())

	def __new__(cls, iterable=None, **kwargs):
		tracker = kwargs.get('tracker', None)

		if tracker and id(tracker) in cls.__instances:
			os.system("cls")
			instance = cls.__instances[id(tracker)]
			instance._iterable = iterable
			instance._bar.desc = kwargs.get('desc', '')
			instance._bar.reset_time()
			return instance
		
		instance = super().__new__(cls)
		return instance

	def __init__(self, iterable=None, **kwargs):
		
		if hasattr(self, '_initialized'):
			return
		tracker = kwargs.get('tracker', None)

		if tracker == None:
			self.__init__legacy__(iterable=iterable, **kwargs)
		else:
			lgbt.__instances[id(tracker)] = self
			self.__init__advanced__(iterable=iterable, **kwargs)

		self._initialized = True

	def __init__advanced__(self, iterable=None, 
						   total=None, desc="",
						   desc_hist="red:+ blue:-",
						   miniter=2500,
						   mininterval=0.1,
						   hero='rainbow', 
						   mode='white',
						   tracker=None,
						   fix=True,
						   max_value=0.5):
		self._iterable = iterable
		self._total = total
		if inspect.isgenerator(self._iterable):
			if self._total == None:
				raise ValueError('The generator was received, but the total is not specified')
		if self._total == None:
			self._total = len(self._iterable)

		if type(tracker) == Tracker:
			self._tracker = tracker
			self._bar = AdvancedBar(total=self._total,
						            hero=hero,
									desc=desc,
									desc_hist=desc_hist,
									mode=mode, 
									fix=fix, 
									max_value=max_value)
		else:
			raise ValueError("Invalid type of tracker")
		
		self.__init__base__(miniter=miniter, mininterval=mininterval)

	def __init__legacy__(self, iterable=None, 
					  	 total=None, 
						 desc="", 
						 miniter=2500, 
						 mininterval=0.1, 
						 hero='rainbow', 
						 mode='white', 
						 tracker=None):
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

		self._bar = DynemicBar(total=self._total, hero=hero, desc=desc, mode=mode)
		self._tracker = tracker

		self.__init__base__(miniter=miniter, mininterval=mininterval)

	def __init__base__(self, miniter, mininterval):
		self._miniter = miniter
		self._mininterval = mininterval
		self._current_iter = 0
		self._is_end = False

		self._miniter = max(1, round(self._total/self._miniter))

	def _next(self):
		self._bar.next()

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
		if hasattr(self._bar, "update_tracker"):
			self._bar.update_tracker(self._tracker.item)
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