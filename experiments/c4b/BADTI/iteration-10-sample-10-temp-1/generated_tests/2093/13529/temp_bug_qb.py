def original_func(*args):
	global_list = []
	
	a = list(map(int, args[0].split()))
	if (a[1] > a[0]):
	    global_list.append((- 1))
	else:
	    global_list.append(((('ab' * (((a[0] + 2) - a[1]) // 2)) + ('a' * ((a[0] - a[1]) % 2))) + ''.join(map((lambda x: chr((ord('c') + x))), range((a[1] - 2))))))
	return global_list