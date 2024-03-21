def func(*args):
	ret_values = []
	
	from math import ceil
	(m, n, a) = map(int, args[0].split())
	times = (ceil((m / a)) * ceil((n / a)))
	ret_values.append(times)

	return ret_values
