def func(*args):
	
	import math
	(n, m, z) = map(int, args[0].split())
	return((z // ((n * m) // math.gcd(n, m))))
