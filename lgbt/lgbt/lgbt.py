import time
import sys
import inspect

BAR_WIDTH = 63

RESET ='\033[0m'
CLEAN = '\033[K'
COLOURS = {'RED':"\033[31m",
		'ORANGE':"\033[38;5;214m",
		'YELLOW':"\033[33m", 
		'GREEN':"\033[32m", 
		'BLUE':"\033[34m",
		'BRIGHT BLUE':"\033[36m", 
		'PURPLE':"\033[35m",
		'BLACK':"\033[30m",
		'WHITE':"\033[37m"}

BACHGROUND = {'RED':"\033[41m",
		'ORANGE':"\033[48;5;214m",
		'YELLOW':"\033[43m", 
		'GREEN':"\033[42m", 
		'BLUE':"\033[44m",
		'BRIGHT BLUE':"\033[48;5;39m", 
		'PURPLE':"\033[45m",
		'BLACK':"\033[40m",
		'WHITE':"\033[47m"}

HEROES = {'rainbow': '🌈',
		'unicorn':'🦄',
		'teddy': '🧸',
		'bunny': '🐰',
		'kitten':'🐱',
		'sakura':'🌸',
		'heart':'💖',
		'gonechar':'🐝',
		'tralalero':'🦈',
		'crocodillo': '🐊',
		'tumtumtum': '🗿',
		'shimpanzini': '🍌',
		'trippi':'🦐',
		'goozinni':'🪿'
		}


def __c__(str, color, background=None):
	"""
	Format string with color
	"""
	if background:
		return f"{COLOURS[color]}{BACHGROUND[background]}{str}{RESET}"
	
	return f"{COLOURS[color]}{str}{RESET}"




class screenplay():
	def __init__(self, country='default'):
		self.placeholder = '█'
		self.country = country
		half = BAR_WIDTH // 2
		athird = BAR_WIDTH // 3
		onesixth = BAR_WIDTH // 6
		oneseventh = BAR_WIDTH // 7

		self.flags = {
			'default': __c__(self.placeholder,'RED')*	oneseventh + __c__(self.placeholder, 'ORANGE')*oneseventh+ __c__(self.placeholder, 'YELLOW')*oneseventh+ __c__(self.placeholder, 'GREEN')*oneseventh + __c__(self.placeholder, 'BRIGHT BLUE')*oneseventh+ __c__(self.placeholder,'BLUE')*oneseventh + __c__(self.placeholder, 'PURPLE')*oneseventh,
			'usa': (__c__(self.placeholder,'BLUE') + __c__('⋆','WHITE','BLUE')) * onesixth + __c__(self.placeholder,'BLUE') + (__c__(self.placeholder,'RED') + __c__(self.placeholder,'WHITE')) *(athird) , 
			'rus': __c__(self.placeholder,'WHITE') * athird + __c__(self.placeholder,'BLUE') * athird + __c__(self.placeholder,'RED') * athird, 
			'rue': __c__(self.placeholder,'BLACK' )* athird + __c__(self.placeholder,'YELLOW') * athird + __c__(self.placeholder,'WHITE') * athird,
			'ita': __c__(self.placeholder,'GREEN')* athird + __c__(self.placeholder,'WHITE') * athird + __c__(self.placeholder,'RED')*athird,
			'fra': __c__(self.placeholder,'BLUE')* athird + __c__(self.placeholder,'WHITE') * athird + __c__(self.placeholder,'RED')*athird,
			'deu': __c__(self.placeholder,'BLACK') * athird + __c__(self.placeholder,'RED') * athird + __c__(self.placeholder,'ORANGE')*athird,
			'chn': __c__(self.placeholder,'RED') + __c__('★ ','YELLOW','RED') + (__c__(self.placeholder,'RED') + __c__('⭑','YELLOW','RED'))*4 + __c__(self.placeholder,'RED') * (BAR_WIDTH-11), 
			'ussr':__c__(self.placeholder,'RED') * oneseventh + __c__('☭ ', 'YELLOW','RED') + __c__(self.placeholder,'RED') * (BAR_WIDTH-oneseventh-2), 
			'swe': __c__('━', 'YELLOW','BRIGHT BLUE') * oneseventh + __c__('╋','YELLOW', 'BRIGHT BLUE')  + __c__('━', 'YELLOW','BRIGHT BLUE') * (BAR_WIDTH-oneseventh - 1),
			'fin': __c__('━', 'BLUE','WHITE') * oneseventh + __c__('╋','BLUE', 'WHITE')  + __c__('━', 'BLUE','WHITE') * (BAR_WIDTH-oneseventh - 1),
			'nor': __c__('━', 'BLUE','RED') * oneseventh + __c__('╋','BLUE', 'RED')  + __c__('━', 'BLUE','RED') * (BAR_WIDTH-oneseventh - 1),
			'dnk': __c__('━', 'WHITE','RED') * oneseventh + __c__('╋','WHITE', 'RED')  + __c__('━', 'WHITE','RED') * (BAR_WIDTH-oneseventh - 1),
			'can': __c__(self.placeholder,'RED')* (athird-4) + __c__(self.placeholder,'WHITE') * 13 +__c__('🍁 ','WHITE', 'WHITE') + __c__(self.placeholder,'WHITE') * 13 + __c__(self.placeholder,'RED')*(athird-4),
			'jpn': __c__(self.placeholder,'WHITE') * half + __c__('●','RED','WHITE')+ __c__(self.placeholder,'WHITE') * half,
			'tur': __c__(self.placeholder, 'RED') * oneseventh + __c__('☪ ','WHITE', 'RED')  + __c__(self.placeholder, 'RED') * (BAR_WIDTH-oneseventh-2),
			'esp': __c__(self.placeholder,'RED')* (athird-4) + __c__(self.placeholder,'ORANGE') * 13 +__c__('♕ ','WHITE', 'ORANGE') + __c__(self.placeholder,'ORANGE') * 13 + __c__(self.placeholder,'RED')*(athird-4),
			'mex': __c__(self.placeholder,'GREEN') * athird + __c__(self.placeholder,'WHITE') * 9 +__c__('🦅 ','WHITE', 'WHITE') + __c__(self.placeholder,'WHITE') * 9 + __c__(self.placeholder,'RED')* athird,
			'kaz': __c__(self.placeholder,'BLUE') + __c__('ᝢ','YELLOW','BLUE') + __c__(self.placeholder,'BLUE') * 28 + __c__('✹ ','YELLOW','BLUE') + __c__(self.placeholder,'BLUE') * half,
			'isr': __c__(self.placeholder,'WHITE')*5 + __c__(self.placeholder,'BLUE')*9  +__c__(self.placeholder,'WHITE')*16 + __c__(' ✡ ','BLUE', 'WHITE') + __c__(self.placeholder,'WHITE')*16  + __c__(self.placeholder,'BLUE') * 9 + __c__(self.placeholder,'WHITE')*5,
			'ind': __c__(self.placeholder,'ORANGE') * athird + __c__(self.placeholder,'WHITE') * 9 +__c__(' ☸ ','BLUE', 'WHITE') + __c__(self.placeholder,'WHITE') * 9 + __c__(self.placeholder,'GREEN')* athird,
			'eng': __c__('━', 'RED','WHITE') * half + __c__('╋','RED', 'WHITE')  + __c__('━', 'RED','WHITE') * half}

		self.bar = self.flags[self.country].split(RESET)


	def get_screnplay(self):
		n = len(self.bar)
		curr_str = ""
		for i,simb in enumerate(self.bar, 1):
			curr_str += simb
			yield (curr_str + RESET) + (" " * (n-i))

	def __len__(self):
		return len(self.bar)
	
class lgbt():
	def __init__(self, iterable=None, desc=" ", miniters=2500, hero='rainbow', total=None, mode='default'):
		self.iterable = iterable
		self.total = total
		if inspect.isgenerator(self.iterable):
			if self.total == None:
				raise ValueError('The generator was received, but the total is not specified')
		
		if self.total == None:
			self.total = len(self.iterable)
		self.miniters = miniters
		self.hero = hero
		self.desc = desc
		self.screenplay = screenplay(country=mode)
		self.bars = []
		self.bar_width = len(self.screenplay)
		self.start = None
		self.iterations = 0
		self.is_end = False

		self.anim = ["".join(['<<', __c__('<', 'GREEN')]), 
					"".join(['<', __c__('<', 'GREEN'),'<']),
			   		"".join([__c__('<', 'GREEN'), '<<']),
					'<<<']
		self._fill_bars()
		self.desc = self._desc_prep()
		self.miniters = max(1, round(self.total/self.miniters))

	def update(self, n=1):
		self.iterations += n
		if self.is_end:
			return
		if self.iterations > self.total:
			self.is_end = True
			sys.stdout.write("\n")
			return
		if self.start == None:
			self.start = time.perf_counter()
		self._draw()

	def _fill_bars(self):
		for simb in self.screenplay.get_screnplay():
			self.bars.append(simb)
	
	def _draw(self):
		end = time.perf_counter() - self.start
		speed = self.iterations / end
		remaining = (self.total - self.iterations) / speed
		filled = round(self.iterations / self.total * (self.bar_width-1))
		percent = (self.iterations / self.total) * 100  

		sys.stdout.write(
			f"\r{self.desc}{percent:03.0f}% {self.bars[filled]} {self.iterations}/{self.total} [{end:03.2f}s{self.anim[filled%4]}{remaining:03.2f}s, {speed:.2f}it/s]{CLEAN}")
		sys.stdout.flush()

	def _desc_prep(self):
		"""
		Formating description string if it's too long
		"""
		length = len(self.desc)
		if length >= 11:
			new_desc = self.desc[:9] + "... " 
		else:
			new_desc = self.desc + (" " * (11-length))
		return HEROES[self.hero]+' ' + new_desc + ":"


	def __call__(self, iterable, **kwargs):
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
		#colection = iterable if not inspect.isgenerator(iterable) else range(total)

		self.start = time.perf_counter()

		for self.iterations, data in enumerate(self.iterable, 1):
			yield data

			if self.iterations % self.miniters == 0:
				self._draw()
		
		sys.stdout.write("\n")