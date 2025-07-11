import os
import time

from math import sin

from .basicobjects import ClassicBar, TextLabel, ConsoleObject, LegacyBar, GPUBar, CPUBar
from .gist import Gist, Window

# [DESC] [PERCENT] [BAR] [TIME, ITER]
class DynemicBar(ConsoleObject):
	def __init__(self, total, desc, hero, mode):
		super(DynemicBar, self).__init__()
		os.system("cls")
		self._short_bar = LegacyBar(total=total, desc=desc, hero=hero, mode=mode, type='short')
		self._long_bar = LegacyBar(total=total, desc=desc, hero=hero, mode=mode, type='long')
		start_time = time.perf_counter()
		self._short_bar.time = start_time
		self._long_bar.time = start_time
		self._console_width = None
	
	def update(self, value):
		self._console_width = os.get_terminal_size().columns
		self._short_bar.update(value)
		self._long_bar.update(value)

	def draw(self):
		if self._console_width < 120:
			self._short_bar.draw()
		else:
			self._long_bar.draw()

class AdvancedBar(ConsoleObject):
	def __init__(self, total, desc='', hero='rainbow', mode='default'):
		super(AdvancedBar, self).__init__()
		#os.system("cls")
		self._timer = time.perf_counter()

		self._window = Window(Gist())
		self._shift_column = self._window.size[1]

		self._classic_label = TextLabel(desc='train is all you need', hero=hero, coord=(self._shift_column + 2, 2), n=5)
		self._gpu_label = TextLabel("GPU", hero='teddy', coord=(self._shift_column + 2, 4), n=5)
		self._cpu_label = TextLabel("CPU", hero='teddy', coord=(self._shift_column + 2, 6), n=5)

		self._shift_column += len(self._classic_label) + 4
		
		self._classic_bar = ClassicBar(total=total, mode=mode, type='short', coord=((self._shift_column, 2)))
		self._gpu_bar = GPUBar(coord=(self._shift_column, 4))
		self._cpu_bar = CPUBar(coord=(self._shift_column, 6))

	def update_value(self, value):
		self._window.update(value) 

	def draw(self):
		self._window.draw()
		self._classic_label.draw()
		self._gpu_bar.draw()
		self._cpu_bar.draw()

		self._classic_bar.draw()
		self._gpu_label.draw()
		self._cpu_label.draw()

	def update(self, value):
		anim_speed = (time.perf_counter() - self._timer) * 5
		self._classic_label.update(anim_speed)

		self._classic_bar.update(value)
		self._gpu_bar.update()
		self._cpu_bar.update()

	def next(self):
		self._window.next()



