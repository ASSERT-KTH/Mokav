def original_func(*args):
	global_list = []
	
	(l1, r1, l2, r2, k) = map(int, args[0].split())
	if ((l2 > r1) or (l1 > r2)):
	    global_list.append(0)
	elif ((l2 >= l1) and (r2 <= r1)):
	    global_list.append((((r2 - l2) + 1) - ((k >= l2) and (k <= r2))))
	elif (l2 >= l1):
	    global_list.append((((r1 - l2) + 1) - ((k >= l2) and (k <= r1))))
	elif (l1 >= l2):
	    global_list.append((((r2 - l1) + 1) - ((k >= l1) and (k <= r2))))
	return global_list