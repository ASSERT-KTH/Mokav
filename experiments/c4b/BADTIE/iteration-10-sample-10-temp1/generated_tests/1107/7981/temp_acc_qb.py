def patched_func(*args):
	global_list = []
	
	(a, b, n) = list(map(int, args[0].split()))
	
	def gcd(x, y):
	    if (x == 0):
	        return y
	    if (y == 0):
	        return x
	    while (x != y):
	        (x, y) = (max(x, y), min(x, y))
	        x -= y
	    return y
	ans = 0
	while (n > 0):
	    if ((ans % 2) == 0):
	        n -= gcd(a, n)
	    else:
	        n -= gcd(b, n)
	    ans += 1
	global_list.append(((ans + 1) % 2))
	return global_list