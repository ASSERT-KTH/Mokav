def original_func(*args):
	global_list = []
	
	(a, b, n) = map(int, args[0].split())
	if ((a == 1) and (b == 1)):
	    global_list.append(1)
	    exit(0)
	
	def gcd(a, b):
	    if (b != 0):
	        return gcd(b, (a % b))
	    else:
	        return a
	i = 0
	while 1:
	    if ((i % 2) == 0):
	        s = gcd(a, n)
	        n = (n - s)
	    else:
	        s = gcd(b, n)
	        n = (n - s)
	    i += 1
	    if (n == 0):
	        break
	if ((i % 2) == 0):
	    global_list.append(1)
	else:
	    global_list.append(0)
	return global_list