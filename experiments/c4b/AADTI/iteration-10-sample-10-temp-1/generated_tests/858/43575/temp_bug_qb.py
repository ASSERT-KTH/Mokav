def original_func(*args):
	global_list = []
	
	import sys
	arr = list(map(int, args[0].split()))
	n = arr[0]
	a = arr[1]
	b = arr[2]
	c = arr[3]
	if ((n % 4) == 0):
	    global_list.append(0)
	elif ((n % 4) == 3):
	    global_list.append(a)
	elif ((n % 4) == 2):
	    global_list.append(min((a * 2), b))
	elif ((n % 4) == 1):
	    global_list.append(min((a * 3), (b + a), c))
	return global_list