def func(*args):
	ret_values = []
	
	from math import floor
	[a, b] = map(int, args[0].split())
	ret_values.append(floor(((a * b) * (1 / 2))))

	return ret_values
