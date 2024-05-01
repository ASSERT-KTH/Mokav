def patched_func(*args):
	global_list = []
	
	
	def gcd(a, b):
	    return (a if (b == 0) else gcd(b, (a % b)))
	(a, b) = map(int, args[0].split())
	(c, d) = map(int, args[1].split())
	g = gcd(a, c)
	dif = abs((b - d))
	if ((dif % g) == 0):
	    for t in range(max(b, d), 1000000):
	        if ((((t - b) % a) == 0) and (((t - d) % c) == 0)):
	            global_list.append(t)
	            break
	else:
	    global_list.append((- 1))
	return global_list