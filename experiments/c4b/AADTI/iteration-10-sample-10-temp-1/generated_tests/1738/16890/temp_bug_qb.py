def original_func(*args):
	global_list = []
	
	from math import gcd
	(a, b, c) = map(int, args[0].split())
	a = gcd(a, b)
	b //= a
	c = gcd(a, c)
	global_list.append((((a * 4) + (b * 4)) + (c * 4)))
	return global_list