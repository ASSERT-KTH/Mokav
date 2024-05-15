def original_func(*args):
	global_list = []
	
	arr = [int(x) for x in args[0].split()]
	arr.sort()
	if (arr[0] == arr[1] == arr[2]):
	    global_list.append((3 * arr[0]))
	else:
	    global_list.append((2 * (arr[0] + arr[1])))
	return global_list