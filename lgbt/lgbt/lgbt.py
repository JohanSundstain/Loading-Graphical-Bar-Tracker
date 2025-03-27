import time

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
	sticks = bar_width // len(colours)
	miniters = max(1, total/miniters)
	
	start = time.perf_counter()
	for i, data in enumerate(iterable, 1):
		yield data

		if i % miniters == 0:
			end = time.perf_counter() - start
			filled = round(i / total * bar_width) 
			empty = bar_width - filled  

			bar = placeholder * filled + " " * empty  
			percent = (i / total) * 100  

			painted_bar = "".join(colours[i // (bar_width // number_of_colours)]  + c if i % (bar_width // number_of_colours) == 1 else c for i, c in enumerate(bar,1))

			current_colour = colours[(filled-1)//sticks]
			percent_str = f'{current_colour}{percent:03.0f}%'
			time_str = f'[{end:.2f}s, '
			it_per_sec_str = f'{i/end:.2f}it/s]' + (" ") 
			iterations_str = f'[{i}/{total}]'

			print(f"\r{desc}{percent_str} {painted_bar}{current_colour}{iterations_str} {time_str} {it_per_sec_str}\033[0m", end="", flush=True)

	print("\033[0m")  