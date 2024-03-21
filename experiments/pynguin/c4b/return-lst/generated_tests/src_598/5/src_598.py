def func(*args):
	ret_values = []
	
	from math import *
	(n, m, z) = map(int, args[0].split())
	ret_values.append((z // ((n * m) // gcd(n, m))))

	return ret_values
