import time
import sys
from tqdm import tqdm

def desc_prep(desc):
	"""
	Formating description string if it's too long
	"""
	length = len(desc)
	if length >= 12:
		new_desc = desc[:9] + "... " 
	else:
		new_desc = desc + (" " * (12-length))
	return "🌈" + new_desc + ":"

def lgbt(iterable, desc=" ", miniters=2500, placeholder='▋'):
	"""
	Progress bar
	iterable    - list of elements
	desc        - description
	miniters    - minimal iterations between update screen
	placeholder - symbol which used in progress bar 
	"""
	colours = ["\033[31m", "\033[38;5;214m", "\033[33m", "\033[32m", "\033[36m", "\033[34m", "\033[35m" ]
	
	desc = desc_prep(desc)
	number_of_colours = len(colours)
	total = len(iterable)
	bar_width = 56  
	step = bar_width // number_of_colours
	miniters = max(1, total/miniters)

	free_spaces = " " * 8
	bar = colours[0] + free_spaces + colours[1] + free_spaces + colours[2] + free_spaces + colours[3] + free_spaces + colours[4] + free_spaces + colours[5] + free_spaces + colours[6] + free_spaces
	
	start = time.perf_counter()
	for i, data in enumerate(iterable, 1):
		yield data

		if i % miniters == 0:
			
			end = time.perf_counter() - start
			filled = round(i / total * bar_width)
			current_colour = colours[(filled-1)//step]
			percent = (i / total) * 100  

			sys.stdout.write(
				f"\r{desc}{current_colour}{percent:03.0f}% {bar.replace(' ', placeholder, filled)}{current_colour}[{i}/{total}] [{end:.2f}s, {i/end:.2f}it/s]  \033[m")
			sys.stdout.flush()
	
for i in lgbt(range(100)):
	time.sleep(0.1)
	j = 0