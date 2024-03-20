def func(*args):
	
	from math import *
	(n, m, z) = map(int, args[0].split())
	return((z // ((n * m) // gcd(n, m))))
