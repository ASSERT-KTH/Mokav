def func(*args):
	
	from math import ceil
	(m, n, a) = map(int, args[0].split())
	times = (ceil((m / a)) * ceil((n / a)))
	return(times)
