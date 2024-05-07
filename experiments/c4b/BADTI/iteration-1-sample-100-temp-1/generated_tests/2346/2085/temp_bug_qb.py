def original_func(*args):
	global_list = []
	
	a = list(map(int, args[0].split()))
	b = max(a)
	a.sort()
	d = a[(len(a) - 2)]
	c = a[(len(a) - 3)]
	if (b < (d + c)):
	    global_list.append('TRIANGLE')
	elif (((d + c) + a[0]) > b):
	    global_list.append('SEGMENT')
	else:
	    global_list.append('IMPOSSIBLE')
	return global_list