import time
import sys

colours = ["\033[31m", "\033[38;5;214m", "\033[33m", "\033[32m", "\033[36m", "\033[34m", "\033[35m" ]
heroes = {'rainbow': '🌈', 'unicorn':'🦄', 'teddy': '🧸', 'bunny': '🐰', 'kitten':'🐱', 'sakura':'🌸', 'heart':'💖'}

def desc_prep(desc, hero):
	"""
	Formating description string if it's too long
	"""
	length = len(desc)
	if length >= 12:
		new_desc = desc[:9] + "... " 
	else:
		new_desc = desc + (" " * (12-length))
	return heroes[hero] + new_desc + ":"

def fill_bars(bar_width, placeholder):
	free_spaces = " " * 8
	bar = colours[0] + free_spaces + colours[1] + free_spaces + colours[2] + free_spaces + colours[3] + free_spaces + colours[4] + free_spaces + colours[5] + free_spaces + colours[6] + free_spaces
	bars = []
	for i in range(0, bar_width+1):
		bars.append(bar.replace(' ', placeholder, i))
	return bars

def lgbt(iterable, desc=" ", miniters=2500, placeholder='▋', hero='rainbow', total=0):
	"""
	Progress bar
	iterable    - list of elements
	desc        - description
	miniters    - minimal iterations between update screen
	placeholder - symbol which used in progress bar 
	hero        - сhoose your smiley face
	"""
	global results
	results = 0

	desc = desc_prep(desc, hero)
	number_of_colours = len(colours)
	total = len(iterable)
	bar_width = 56  
	step = bar_width // number_of_colours
	miniters = max(1, round(total/miniters))
	
	bars = fill_bars(bar_width=bar_width, placeholder=placeholder)
	
	start = time.perf_counter()
	for i, data in enumerate(iterable, 1):
		yield data

		if i % miniters == 0:
			
			end = time.perf_counter() - start
			filled = round(i / total * bar_width)
			current_colour = colours[(filled-1)//step]
			percent = (i / total) * 100  

			sys.stdout.write(
				f"\r{desc}{current_colour}{percent:03.0f}% {bars[filled]}{current_colour}[{i}/{total}] [{end:.2f}s, {i/end:.2f}it/s]  \033[m")
			sys.stdout.flush()
	
	sys.stdout.write("\n")