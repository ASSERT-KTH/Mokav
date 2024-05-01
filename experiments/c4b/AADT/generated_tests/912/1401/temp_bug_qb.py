def original_func(*args):
	global_list = []
	
	C = list(map(int, args[0].split()))
	if (sum(C) == 0):
	    global_list.append((- 1))
	elif ((sum(C) % 5) == 0):
	    global_list.append((sum(C) // 5))
	else:
	    global_list.append((- 1))
	return global_list