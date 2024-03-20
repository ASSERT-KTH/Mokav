def func(*args):
	
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
	return(((ans + 1) % 2))
