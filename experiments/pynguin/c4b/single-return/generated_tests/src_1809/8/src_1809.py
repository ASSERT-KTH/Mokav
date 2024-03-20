def func(*args):
	
	from math import log1p as ln
	(a, b) = map(int, args[0].split())
	years = (ln(((b / a) - 1)) / ln(((3 / 2) - 1)))
	return((int(years) + 1))
