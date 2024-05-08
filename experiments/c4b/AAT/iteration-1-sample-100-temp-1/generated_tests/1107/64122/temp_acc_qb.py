def patched_func(*args):
	global_list = []
	
	
	def gcd(a, b):
	    if ((a % b) == 0):
	        return b
	    else:
	        return gcd(b, (a % b))
	(a, b, n) = [int(i) for i in args[0].split()]
	i = 1
	if (n < gcd(n, a)):
	    i = 1
	while (n >= max(gcd(n, a), gcd(n, b))):
	    if ((i % 2) == 1):
	        n = (n - gcd(n, a))
	    elif ((i % 2) == 0):
	        n = (n - gcd(n, b))
	    i = (i + 1)
	if ((i % 2) == 1):
	    global_list.append(1)
	else:
	    global_list.append(0)
	return global_list