def func(*args):
	ret_values = []
	
	from math import log1p as ln
	(a, b) = map(int, args[0].split())
	years = (ln(((b / a) - 1)) / ln(((3 / 2) - 1)))
	ret_values.append((int(years) + 1))

	return ret_values
