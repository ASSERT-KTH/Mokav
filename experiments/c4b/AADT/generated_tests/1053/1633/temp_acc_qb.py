def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	a = (n // 7)
	for x in range(a, (- 1), (- 1)):
	    if (((n - (x * 7)) % 4) == 0):
	        global_list.append((('4' * ((n - (x * 7)) // 4)) + ('7' * x)))
	        break
	else:
	    global_list.append((- 1))
	return global_list