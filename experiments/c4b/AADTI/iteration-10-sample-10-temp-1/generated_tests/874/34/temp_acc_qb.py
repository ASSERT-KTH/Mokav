def patched_func(*args):
	global_list = []
	
	(n, k) = map(int, args[0].split())
	while (k != (2 ** n)):
	    if (k < (2 ** n)):
	        k = k
	    else:
	        k -= (2 ** n)
	    n -= 1
	global_list.append((n + 1))
	return global_list