import time
import sys
import inspect
import os

from bar import DynemicBar, AdvancedBar
from basicobjects import LegacyBar

class Tracker:
	def __init__(self, number=None):
		if type(number) in [float, int, type(None)]:
			self._number = number
		elif type(number) == type(self):
			self = number
		else:
			raise ValueError("Not correct type of variable")

	@property
	def item(self):
		return self._number
	
	@item.setter
	def item(self, value):
		if type(value) in [float, int, type(None)]:
			self._number = value
		elif type(value) == type(self):
			self = value
		else:
			raise ValueError("Not correct type of variable")

	
	def __str__(self):
		return str(self._number)
	
	def __add__(self, value):
		if type(value) == type(self):
			return Tracker(self._number + value.item())
		elif type(value) in [float, int]:
			return Tracker(self._number + value)
		else:
			raise ValueError("Not correct type of variable")
		
	def __sub__(self, value):
		if type(value) == type(self):
			return Tracker(self._number - value.item())
		elif type(value) in [float, int]:
			return Tracker(self._number - value)
		else:
			raise ValueError("Not correct type of variable")
		
	def __mul__(self, value):
		if type(value) == type(self):
			return Tracker(self._number * value.item())
		elif type(value) in [float, int]:
			return Tracker(self._number * value)
		else:
			raise ValueError("Not correct type of variable")
		
	def __truediv__(self, value):
		if type(value) == type(self):
			return Tracker(self._number / value.item())
		elif type(value) in [float, int]:
			return Tracker(self._number / value)
		else:
			raise ValueError("Not correct type of variable")
		
	def __floordiv__(self, value):
		if type(value) == type(self):
			return Tracker(self._number // value.item())
		elif type(value) in [float, int]:
			return Tracker(self._number // value)
		else:
			raise ValueError("Not correct type of variable")
		
	def __mod__(self, value):
		if type(value) == type(self):
			return Tracker(self._number % value.item())
		elif type(value) in [float, int]:
			return Tracker(self._number % value)
		else:
			raise ValueError("Not correct type of variable")
		
	def __pow__(self, value):
		if type(value) == type(self):
			return Tracker(self._number ** value.item())
		elif type(value) in [float, int]:
			return Tracker(self._number ** value)
		else:
			raise ValueError("Not correct type of variable")
		
	def __eq__(self, value):
		if type(value) == type(self):
			return self._number == value.item()
		elif type(value) in [float, int, type(None)]:
			return self._number == value
		else:
			raise ValueError("Not correct type of variable")

	def __ne__(self, value):
		if type(value) == type(self):
			return self._number != value.item()
		elif type(value) in [float, int, type(None)]:
			return self._number != value
		else:
			raise ValueError("Not correct type of variable")
		
	def __lt__(self, value):
		if type(value) == type(self):
			return self._number < value.item()
		elif type(value) in [float, int]:
			return self._number < value
		else:
			raise ValueError("Not correct type of variable")

	def __gt__(self, value):
		if type(value) == type(self):
			return self._number > value.item()
		elif type(value) in [float, int]:
			return self._number > value
		else:
			raise ValueError("Not correct type of variable")
	
	def __le__(self, value):
		if type(value) == type(self):
			return self._number <= value.item()
		elif type(value) in [float, int]:
			return self._number <= value
		else:
			raise ValueError("Not correct type of variable")
		
	def __ge__(self, value):
		if type(value) == type(self):
			return self._number >= value.item()
		elif type(value) in [float, int]:
			return self._number >= value
		else:
			raise ValueError("Not correct type of variable")
		
	def __iadd__(self, value):
		if type(value) == type(self):
			self._number += value.item()
			return self
		elif type(value) in [float, int]:
			self._number += value
			return self
		else:
			raise ValueError("Not correct type of variable")
		
	def __isub__(self, value):
		if type(value) == type(self):
			self._number -= value.item()
			return self
		elif type(value) in [float, int]:
			self._number -= value
			return self
		else:
			raise ValueError("Not correct type of variable")
		
	def __imul__(self, value):
		if type(value) == type(self):
			self._number *= value.item()
			return self
		elif type(value) in [float, int]:
			self._number *= value
			return self
		else:
			raise ValueError("Not correct type of variable")
		
	def __itruediv__(self, value):
		if type(value) == type(self):
			self._number /= value.item()
			return self
		elif type(value) in [float, int]:
			self._number /= value
			return self
		else:
			raise ValueError("Not correct type of variable")
		
	def __ifloordiv__(self, value):
		if type(value) == type(self):
			self._number //= value.item()
			return self
		elif type(value) in [float, int]:
			self._number //= value
			return self
		else:
			raise ValueError("Not correct type of variable")
		
	def __ipow__(self, value):
		if type(value) == type(self):
			self._number **= value.item()
			return self
		elif type(value) in [float, int]:
			self._number **= value
			return self
		else:
			raise ValueError("Not correct type of variable")
		
	def __pos__(self):
		self._number = +self._number
		return self
	
	def __neg__(self):
		self._number = -self._number
		return self

	def __abs__(self):
		return +self



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
