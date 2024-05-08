def original_func(*args):
	global_list = []
	
	(k, b, n, t) = map(int, args[0].split())
	z = int(1)
	res = int(n)
	for i in range(n):
	    z = ((k * z) + b)
	    if (z < t):
	        res -= 1
	    else:
	        break
	global_list.append(res)
	return global_list