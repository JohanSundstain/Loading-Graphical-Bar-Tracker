PH = '█'
BIG=63

# set column and row
def cursor(column, row):
	print(f"\033[{row};{column}H", end="")

def cursor_str(column, row):
	return f"\033[{row};{column}H"

def cursor_str(culumn, row):
	return "\033[{row};{column}H"

HAND_KEYS = {
	'BEGIN': '\033[H',
	'RESET': '\033[0m', 
	'CLEAN': '\033[0K', 
	'UP': '\033[A', 
	'DOWN': '\033[B', 
	'RIGHT': '\033[C', 
	'LEFT': '\033[D',
	'CLEAR':'\033[H\033[J'
	}


COLOURS = {
		'RED':"\033[31m",
		'ORANGE':"\033[38;5;214m",
		'YELLOW':"\033[33m", 
		'GREEN':"\033[32m", 
		'BLUE':"\033[34m",
		'BRIGHT BLUE':"\033[36m", 
		'PURPLE':"\033[35m",
		'BLACK':"\033[30m",
		'WHITE':"\033[37m",
		'BRIGHT GREEN' :'\033[1;32m'
		}

BACHGROUND = {
		'RED':"\033[41m",
		'ORANGE':"\033[48;5;214m",
		'YELLOW':"\033[43m", 
		'GREEN':"\033[42m", 
		'BLUE':"\033[44m",
		'BRIGHT BLUE':"\033[48;5;39m", 
		'PURPLE':"\033[45m",
		'BLACK':"\033[40m",
		'WHITE':"\033[47m"
		}

COLS = {0.0: ' ', 0.125: '▁', 0.25 : '▂', 0.375: '▃', 0.5: '▄', 0.625: '▅', 0.75 : '▆', 0.875: '▇' , 1.0: '█' }
COLS_KEYS = list(COLS.keys())

def paint(str, color, count, background=None):
	"""
	Format string with color
	"""
	if background:
		return f"{COLOURS[color]}{BACHGROUND[background]}{str}{HAND_KEYS['RESET']}" * count
	
	return f"{COLOURS[color]}{str}{HAND_KEYS['RESET']}" * count


def repeat(str, count):
	return str * count


def upper_bound(value):
	for i in range(len(COLS_KEYS)) :
		if COLS_KEYS[i] > value:
			return COLS[COLS_KEYS[i-1]]

# 63 length all strings
FLAGS =  {
			'white' : paint(PH, 'WHITE', 63),
			'rainbow': paint(PH,'RED', 9) + paint(PH,'ORANGE', 9) + paint(PH,'YELLOW', 9) + paint(PH,'GREEN', 9) + paint(PH,'BRIGHT BLUE', 9) + paint(PH, 'BLUE', 9) + paint(PH, 'PURPLE', 9),
			'usa': repeat(paint(PH,'BLUE', 1) + paint('⋆','WHITE', 1, 'BLUE'), 10)  + paint(PH,'BLUE', 1) + repeat(paint(PH,'RED',1) + paint(PH,'WHITE',1), 21),
			'chn': paint(PH,'RED', 1) + paint('★ ','YELLOW', 1, 'RED') + repeat(paint(PH,'RED',1) + paint('⭑','YELLOW', 1,'RED'), 4) + paint(PH, 'RED', 52),

			'ussr':paint(PH,'RED',  9) + paint('☭ ','YELLOW', 1, 'RED') + paint(PH,'RED', 52),

			'rus': paint(PH,'WHITE', 21) + paint(PH,'BLUE',   21) + paint(PH,'RED',    21), 
			'ita': paint(PH,'GREEN', 21) + paint(PH,'WHITE',  21) + paint(PH,'RED',    21), 
			'rue': paint(PH,'BLACK', 21) + paint(PH,'YELLOW', 21) + paint(PH,'WHITE',  21),
			'deu': paint(PH,'BLACK', 21) + paint(PH,'RED',    21) + paint(PH,'ORANGE', 21),
			'fra': paint(PH,'BLUE',  21) + paint(PH,'WHITE',  21) + paint(PH,'RED',    21),

			'swe': paint('━', 'YELLOW', 9,'BRIGHT BLUE') + paint('╋','YELLOW',1, 'BRIGHT BLUE') + paint('━', 'YELLOW', 53,'BRIGHT BLUE'),
			'fin': paint('━', 'BLUE',   9,'WHITE')       + paint('╋','BLUE',  1, 'WHITE')       + paint('━', 'BLUE',   53,'WHITE'),
			'nor': paint('━', 'BLUE',  9 ,'RED')         + paint('╋','BLUE',  1, 'RED')         + paint('━', 'BLUE',   53,'RED'),
			'dnk': paint('━', 'WHITE', 9,'RED')          + paint('╋','WHITE', 1, 'RED')         + paint('━', 'WHITE',  53,'RED'),

			'eng': paint('━', 'RED',   31, 'WHITE') + paint('╋','RED',     1, 'WHITE')  + paint('━', 'RED', 31,'WHITE'),
			'jpn': paint(PH,'WHITE', 31)            + paint('●','RED',     1, 'WHITE')  + paint(PH,'WHITE', 31),
			}