def patched_func(*args):
	global_list = []
	
	n = args[0]
	lucky = 0
	for x in n:
	    if (int(x) == 7):
	        lucky += 1
	    elif (int(x) == 4):
	        lucky += 1
	if (lucky == 4):
	    global_list.append('YES')
	elif (lucky == 7):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list