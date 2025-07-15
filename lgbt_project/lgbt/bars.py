import os
import time

from math import sin

from lgbt.basicobjects import ClassicBar, TextLabel, ConsoleObject, LegacyBar, GPUBar, CPUBar
from lgbt.histogram import Histogram, Window
from lgbt.consts import paint, HAND_KEYS

# [DESC] [PERCENT] [BAR] [TIME, ITER]
class DynemicBar(ConsoleObject):
	def __init__(self, total, desc='', hero='rainbow', mode='white'):
		super(DynemicBar, self).__init__()
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
			self._short_bar.flush(self._buffer)
		else:
			self._long_bar.draw()
			self._long_bar.flush(self._buffer)

class AdvancedBar(ConsoleObject):
	def __init__(self, total, desc='', desc_hist='', hero='rainbow', mode='white', device_id=0, max_value=0.5, fix=True, coord=(1,1)):
		super(AdvancedBar, self).__init__(coord=coord)
		self._timer = time.perf_counter()
		self._window = Window(Histogram(max_value=max_value, fix=fix), coord=coord)
		shift_column = self._window.size[1] + coord[0]
		shift_row = self._window.size[0] + coord[1]
		window_label = TextLabel(desc=desc_hist, hero='histogram', coord=(coord[0]+4, shift_row), n=self._window.size[1]-8)
		self._stat_bar = StatBar(total=total, desc=desc, hero=hero, mode=mode, device_id=device_id, coord=(coord[0] + shift_column, coord[1] + 1))
		self._objects_to_draw = [self._stat_bar, self._window, window_label]
		self._objects_to_update = [window_label, self._stat_bar]

	@property
	def desc(self):
		return self._stat_bar.desc
	
	@desc.setter
	def desc(self, value):
		self._stat_bar.desc = value
	
	def update_tracker(self, value):
		self._window.update(value) 

	def draw(self):
		for obj in self._objects_to_draw:
			obj.draw()
			obj.flush(self._buffer)

	def update(self, value):
		anim_speed = (time.perf_counter() - self._timer) * 5

		for obj in self._objects_to_update:
			if type(obj) == TextLabel:
				obj.update(anim_speed)
			else:
				obj.update(value)

	def next(self):
		self._window.next()

	def reset_time(self):
		start_time = time.perf_counter()
		self._stat_bar.reset_time(start_time)

class StatBar(ConsoleObject):
	def __init__(self, total, desc='', hero='rainbow', mode='white', device_id=0, coord=(1,1)):
		super().__init__(coord=coord)
		self._timer = time.perf_counter()

		self._bar_label = TextLabel(desc=desc, hero=hero, coord=coord)
		shift = len(self._bar_label) + 1
		gpu_bar_label = TextLabel(desc='GPU', hero='gpu', coord=(coord[0], coord[1] + 2))
		cpu_bar_label = TextLabel(desc='CPU', hero='cpu', coord=(coord[0], coord[1] + 4))

		self._bar = ClassicBar(total=total, mode=mode, type='short', coord=(coord[0] + shift, coord[1]) )
		gpu_bar = GPUBar(device_id=device_id, coord=(coord[0] + shift, coord[1] + 2))
		cpu_bar = CPUBar(coord=(coord[0] + shift, coord[1] + 4))

		self._objects_to_draw = [ self._bar_label, gpu_bar_label, cpu_bar_label, self._bar, gpu_bar, cpu_bar]
		self._objects_to_update = [self._bar, gpu_bar, cpu_bar, self._bar_label]

	@property
	def desc(self):
		return self._bar_label.desc
	
	@desc.setter
	def desc(self, value):
		self._bar_label.desc = value

	def draw(self):
		for obj in self._objects_to_draw:
			obj.draw()
			obj.flush(self._buffer)

	def update(self, value):
		anim_speed = (time.perf_counter() - self._timer) * 5

		for obj in self._objects_to_update:
			if type(obj) == TextLabel:
				obj.update(anim_speed)
			elif type(obj) != Window:
				obj.update(value)

	def reset_time(self, value):
		self._bar.time = value