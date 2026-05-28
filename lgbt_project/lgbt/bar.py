from abc import abstractmethod
import time
import sys
import os
from lgbt.consts import FLAGS, HAND_KEYS

class ConsoleObject():
	def __init__(self, coord=(1,1)):
		self._coord = coord
		self._time = None
		self._value = None
		self._buffer = []

	@property
	def time(self):
		return self._time
	
	@time.setter
	def time(self, value):
		self._time = value

	@property
	def coord(self):
		return self._coord
	
	@coord.setter
	def coord(self, value):
		self._coord = value

	@abstractmethod
	def draw(self):
		pass

	@abstractmethod
	def update(self, value):
		if self._time == None:
			self._time = time.perf_counter()
		self._value = value
		
	def cursor(self, column, row):
		self._buffer.append(f"\033[{row};{column}H")

	def put_in_buffer(self, value):
		self._buffer.append(value)

	def flush(self, buffer=None):
		if buffer == None:
			sys.stdout.write("".join(self._buffer))
			sys.stdout.flush()
			self._buffer.clear()
		else:
			buffer.extend(self._buffer)
			self._buffer.clear()
		
	
class Bar(ConsoleObject):
	def __init__(self, desc, total, mode="rainbow", fixed=False):
		if fixed:
			os.system('cls' if os.name == 'nt' else 'clear')  	

		super(Bar, self).__init__()
		self._bar = FLAGS[mode].split(HAND_KEYS['RESET'])
		self._part_bars = []

		self._start_time = None
		self._value = None
		self._max_desc = 10
		self._total = total
		self._width = 63
		self._desc = self._check_desc(desc),

		self._stats = {
			"percent" : 		0.0,
			"filled" : 			0,
			'passed_time':		0.0,
			'remaining_time' : 	0.0,
			'speed' : 			0.0,
			'current_iter': 	0,
			'total_iter' : 		total
			}
		
		self._fill_bar()
	
	def _fill_bar(self):
		n = len(self._bar)
		curr_str = ""
		for i, simb in enumerate(self._bar, 1):
			curr_str += simb
			self._part_bars.append((curr_str + HAND_KEYS['RESET']) + (" " * (n - i)) )

	def _translate_count(self, iter):
		if iter >= 1000000:
			return f'{iter/1000000:.0f}M'
		if iter >= 1000:
			return f'{iter/1000:.0f}K'
		return f'{iter:.0f}'
	
	def _translate_time(self, sec):
		total_seconds = int(sec)
		if total_seconds > 3600:
			hours = total_seconds // 3600
			remaining_seconds = total_seconds % 3600
			minutes = remaining_seconds // 60
			seconds = remaining_seconds % 60
			return f'{hours}:{minutes:02}:{seconds:02}'
		else:
			seconds = total_seconds % 60
			minutes = total_seconds // 60
			return f'{minutes:02}:{seconds:02}'
		
	def _check_desc(self, desc):
		if len(desc) > self._max_desc:
			desc = desc[:(self._max_desc-3)]
			desc += "..."
		return desc
	
	def update(self, value):
		super().update(value)
		self._stats['percent'] = (self._value / self._total) * 100  
		self._stats['filled']  = round(self._value / self._total * (len(self._bar)-1))
		self._stats['passed_time'] = time.perf_counter() - self._time
		self._stats['speed'] = self._value / self._stats['passed_time']
		self._stats['remaining_time'] = (self._total - self._value) / self._stats['speed'] 
		self._stats['current_iter'] = self._value

	def draw(self):
		desc = self._desc
		percent = self._stats['percent']
		filled = self._stats['filled']
		passed_time = self._translate_time(self._stats['passed_time'])
		remaining_time = self._translate_time(self._stats['remaining_time'])
		speed =  self._translate_count(self._stats['speed'])
		current_iter = self._translate_count(self._stats['current_iter'])
		total = self._translate_count(self._stats['total_iter'])
		self.put_in_buffer(f"\r{desc[0]} {percent:03.0f}% {self._part_bars[filled]} {current_iter}/{total} [{passed_time}<{remaining_time}, {speed}it/s]{HAND_KEYS['CLEAN']}")
