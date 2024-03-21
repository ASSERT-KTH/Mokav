def func(*args):
	ret_values = []
	
	from math import ceil
	(n, m, a) = map(int, args[0].split())
	ret_values.append((ceil((n / a)) * ceil((m / a))))

	return ret_values
