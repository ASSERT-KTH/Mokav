def func(*args):
	
	from math import floor
	[a, b] = map(int, args[0].split())
	return(floor(((a * b) * (1 / 2))))
