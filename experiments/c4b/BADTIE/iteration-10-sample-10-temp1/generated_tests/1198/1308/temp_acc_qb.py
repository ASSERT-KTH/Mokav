def patched_func(*args):
	global_list = []
	
	entered = args[0]
	list(entered)
	h = entered.count('H')
	q = entered.count('Q')
	nine = entered.count('9')
	if ((h > 0) or (q > 0) or (nine > 0)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list