def patched_func(*args):
	global_list = []
	
	import sys
	
	def gcd(a, b):
	    if (b == 0):
	        return a
	    return gcd(b, (a % b))
	(a, b, c) = tuple(map(int, args[0].split()))
	if ((b == c) or (a < min(b, c))):
	    global_list.append('1/1')
	    sys.exit(0)
	ans = (min(b, c) - 1)
	x = ((b * c) // gcd(b, c))
	ans += ((a // x) * min(b, c))
	y = max((((((a // x) * x) + min(b, c)) - 1) - a), 0)
	ans -= y
	y = gcd(ans, a)
	ans //= y
	a //= y
	global_list.append(((str(ans) + '/') + str(a)))
	return global_list