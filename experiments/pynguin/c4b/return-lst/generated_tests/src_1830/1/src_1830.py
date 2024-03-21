def func(*args):
	ret_values = []
	
	from math import ceil
	(n, m, a) = [int(x) for x in args[0].split(' ')]
	ret_values.append((ceil((n / a)) * ceil((m / a))))

	return ret_values
