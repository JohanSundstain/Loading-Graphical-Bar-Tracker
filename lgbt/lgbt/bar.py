from abc import ABC, abstractmethod

from consts import RESET, CLEAN, BIG_FLAGS, HEROES, ARROW_ANIM
from consts import create_string_anim

class Bar():
	def __init__(self):
		pass

	@abstractmethod
	def show(self):
		pass

	def translate_time(self, sec):
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
		
	def translate_count(self, iter):
		if iter > 1000000:
			return f'{iter/1000000:.0f}M'
		if iter > 1000:
			return f'{iter/1000:.0f}K'
		return f'{iter:.0f}'
	

class Anim():
	def __init__(self, list_anim):
		self.anim = list_anim
		self.n = len(self.anim)

	def __call__(self, iter):
		return self.anim[iter%self.n]


# [DESC] [PERCENT] [BAR] [TIME, ITER]
class CommonBar(Bar):
	def __init__(self, total, desc, hero, mode):
		self.bar = BIG_FLAGS[mode].split(RESET)
		self.bars = []
		self.total = total
		self.desc = desc 
		self.hero = HEROES[hero]
		self.bar_width = 63
		self.decs_anim = None 

		if len(self.desc) >= 11:
			self._desc_func = self._desc_gt
			self.decs_anim = Anim(create_string_anim(self.desc))
		else:
			self.desc = desc + (" " * (11-len(desc)))
			self._desc_func = self._desc_le	

		self.arrow_anim = Anim(ARROW_ANIM)

		self._fill_bar()

	def _desc_gt(self, iter):
		"""
		Formating description string if it's too long
		"""
		return self.decs_anim(iter)[:11]
	
	
	def _desc_le(self, iter):
		return self.desc


	def _fill_bar(self):
		n = len(self.bar)
		curr_str = ""
		for i, simb in enumerate(self.bar, 1):
			curr_str += simb
			self.bars.append((curr_str + RESET) + (" " * (n-i)))
	
	def show(self, total_time, current_iter):
		anim_speed = int(total_time * 5)

		speed = current_iter / total_time
		remaining =  (self.total - current_iter) / speed 
		filled =  round(current_iter / self.total * (self.bar_width-1))

		current_desc = self._desc_func(anim_speed)
		percent = (current_iter / self.total) * 100  

		part_of_bar = self.bars[filled]

		processed_iter = self.translate_count(current_iter)
		total_iter = self.translate_count(self.total)

		elapsed_time = self.translate_time(total_time)
		anim = self.arrow_anim(anim_speed)
		remainning_time = self.translate_time(remaining)

		iter_per_second = self.translate_count(speed) + "it/s"
	
		return f"\r{self.hero} {current_desc}{percent:03.0f}% {part_of_bar} {processed_iter}/{total_iter} [{elapsed_time}{anim}{remainning_time}, {iter_per_second}]{CLEAN}"

	
	def __len__(self):
		return len(self.bar)


