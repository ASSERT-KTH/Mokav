def patched_func(*args):
	global_list = []
	
	
	def gcd(a, b):
	    if (b == 0):
	        return a
	    return gcd(b, (a % b))
	(a, b, n) = map(int, args[0].split())
	cur = a
	win = 1
	while True:
	    if (n < gcd(n, cur)):
	        break
	    else:
	        n = (n - gcd(n, cur))
	        cur = (b if (cur == a) else a)
	        win = (1 if (win == 0) else 0)
	global_list.append(win)
	return global_list