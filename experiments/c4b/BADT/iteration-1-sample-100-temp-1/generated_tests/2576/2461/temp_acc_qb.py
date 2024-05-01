def patched_func(*args):
	global_list = []
	
	(k, a, b) = map(int, args[0].split())
	if (((a < k) and (b % k)) or ((b < k) and (a % k))):
	    global_list.append((- 1))
	else:
	    global_list.append(((a // k) + (b // k)))
	return global_list