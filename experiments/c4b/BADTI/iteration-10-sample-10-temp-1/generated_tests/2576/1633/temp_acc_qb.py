def patched_func(*args):
	global_list = []
	
	string = args[0]
	(n, a, b) = map(int, string.split())
	
	def check(p, q):
	    return (((p % n) != 0) and (q < n))
	if (check(a, b) or check(b, a)):
	    global_list.append((- 1))
	else:
	    global_list.append(((a // n) + (b // n)))
	return global_list