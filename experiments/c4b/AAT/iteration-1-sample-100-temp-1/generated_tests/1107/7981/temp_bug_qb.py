def original_func(*args):
	global_list = []
	
	(a, b, n) = list(map(int, args[0].split()))
	
	def gcd(x, y):
	    while (x != y):
	        (x, y) = (max(x, y), min(x, y))
	        x -= y
	    return y
	x = gcd(a, b)
	global_list.append((((n // x) + 1) % 2))
	return global_list