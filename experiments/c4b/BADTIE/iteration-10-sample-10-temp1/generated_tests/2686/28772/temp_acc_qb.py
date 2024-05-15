def patched_func(*args):
	global_list = []
	
	mirror = [8, (- 1), (- 1), 3, 6, 9, 4, 7, 0, 5]
	
	def dg(n):
	    if n:
	        res = []
	        while n:
	            res.append((n % 10))
	            n //= 10
	    else:
	        res = [0]
	    return res
	n = int(args[0])
	dg1 = dg(n)
	dg2 = [mirror[d] for d in reversed(dg1)]
	if (dg1 == dg2):
	    global_list.append('Yes')
	else:
	    global_list.append('No')
	return global_list