def original_func(*args):
	global_list = []
	
	(n, k) = map(int, args[0].split())
	if (k > n):
	    global_list.append((- 1))
	else:
	    s = ('ab' * ((n // 2) + 1))[:n]
	    global_list.append(((s[:(- (k - 2))] + ''.join([chr((97 + i)) for i in range(2, k)])) if (k > 2) else s))
	return global_list