def patched_func(*args):
	global_list = []
	
	(n, k) = map(int, args[0].split())
	if ((n < k) or (k > 26)):
	    global_list.append((- 1))
	elif (k == 1):
	    global_list.append(('a' if (n == 1) else (- 1)))
	else:
	    global_list.append((('ab' * ((n // 2) + 1))[:((n - k) + 2)] + 'cdefghijklmnopqrstuvwxyz'[:(k - 2)]))
	return global_list