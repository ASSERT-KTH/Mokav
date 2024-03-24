def func(*args):
	ret_values = []
	
	import math
	(n, m, z) = map(int, args[0].split())
	ret_values.append((z // ((n * m) // math.gcd(n, m))))

	return ret_values
