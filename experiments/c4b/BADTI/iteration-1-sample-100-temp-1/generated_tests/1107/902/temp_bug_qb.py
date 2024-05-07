def original_func(*args):
	global_list = []
	
	
	def bmm(n, m):
	    if (min(n, m) == 0):
	        return max(n, m)
	    return bmm((max(n, m) % min(n, m)), min(n, m))
	(a, b, n) = map(int, args[0].split())
	B = 0
	while True:
	    if (B == 0):
	        n -= bmm(n, a)
	        if (n < 0):
	            B = 1
	            break
	    else:
	        n -= bmm(b, a)
	        if (n < 0):
	            B = 0
	            break
	    B += 1
	    B = (B % 2)
	global_list.append(B)
	return global_list