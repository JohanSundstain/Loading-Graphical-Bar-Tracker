PH = '█'
RESET ='\033[0m'
CLEAN = '\033[K'
COLOURS = {
		'RED':"\033[31m",
		'ORANGE':"\033[38;5;214m",
		'YELLOW':"\033[33m", 
		'GREEN':"\033[32m", 
		'BLUE':"\033[34m",
		'BRIGHT BLUE':"\033[36m", 
		'PURPLE':"\033[35m",
		'BLACK':"\033[30m",
		'WHITE':"\033[37m"}

BACHGROUND = {
		'RED':"\033[41m",
		'ORANGE':"\033[48;5;214m",
		'YELLOW':"\033[43m", 
		'GREEN':"\033[42m", 
		'BLUE':"\033[44m",
		'BRIGHT BLUE':"\033[48;5;39m", 
		'PURPLE':"\033[45m",
		'BLACK':"\033[40m",
		'WHITE':"\033[47m"}

HEROES = {
		'rainbow': '🌈',
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


def paint(str, color, count, background=None):
	"""
	Format string with color
	"""
	if background:
		return f"{COLOURS[color]}{BACHGROUND[background]}{str}{RESET}" * count
	
	return f"{COLOURS[color]}{str}{RESET}" * count


def rotate_left(s, n):
    n = n % len(s)  
    return s[n:] + s[:n]

def create_string_anim(str):
	ext_str = str + (" " * len(str))
	anim = []
	for i in range(len(ext_str)):
		anim.append(rotate_left(ext_str, i))
	
	return anim


def repeat(str, count):
	return str * count

# 63 length all strings
BIG_FLAGS =  {
			'default': paint(PH,'RED', 9) + paint(PH,'ORANGE', 9) + paint(PH,'YELLOW', 9) + paint(PH,'GREEN', 9) + paint(PH,'BRIGHT BLUE', 9) + paint(PH, 'BLUE', 9) + paint(PH, 'PURPLE', 9),
			'usa': repeat(paint(PH,'BLUE', 1) + paint('⋆','WHITE', 1, 'BLUE'), 10)  + paint(PH,'BLUE', 1) + repeat(paint(PH,'RED',1) + paint(PH,'WHITE',1), 21),
			'chn': paint(PH,'RED', 1) + paint('★ ','YELLOW', 1, 'RED') + repeat(paint(PH,'RED',1) + paint('⭑','YELLOW', 1,'RED'), 4) + paint(PH, 'RED', 52),

			'tur': paint(PH, 'RED', 9) + paint('☪ ','WHITE',  1, 'RED')  + paint(PH, 'RED', 52),
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
			'kaz': paint(PH,'BLUE', 30)             + paint(' ✹ ','YELLOW', 1, 'BLUE')  + paint(PH,'BLUE',  30),

			'mex': paint(PH,'GREEN', 21) + paint(PH,'WHITE', 9) + paint('🦅 ','WHITE', 1, 'WHITE') + paint(PH,'WHITE', 9) + paint(PH,'RED', 21),
			'ind': paint(PH,'ORANGE',21) + paint(PH,'WHITE', 9) + paint(' ☸ ','BLUE',  1,'WHITE')  + paint(PH,'WHITE', 9) + paint(PH,'GREEN',21),

			'esp': paint(PH,'RED', 17)   + paint(PH,'ORANGE', 13) + paint(' ♕ ','WHITE', 1, 'ORANGE') + paint(PH,'ORANGE', 13) + paint(PH,'RED', 17),
			'can': paint(PH,'RED', 17)   + paint(PH,'WHITE',  13)  + paint('🍁 ','WHITE', 1,'WHITE')   + paint(PH,'WHITE', 13)  + paint(PH,'RED', 17),

			'isr': paint(PH,'WHITE', 5) + paint(PH,'BLUE', 9)  + paint(PH,'WHITE', 16) + paint(' ✡ ','BLUE', 1, 'WHITE') + paint(PH,'WHITE', 16) + paint(PH,'BLUE', 9) + paint(PH,'WHITE', 5)
		}

ARROW_ANIM = ["".join(['<<', paint('<', 'GREEN', 1)]), 
					"".join(['<', paint('<', 'GREEN', 1),'<']),
			   		"".join([paint('<', 'GREEN', 1), '<<']),
					'<<<']


"""SHORT_FLAGS =
{

}"""