def patched_func(*args):
	global_list = []
	
	a = int(args[0])
	b = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
	for i in range(14):
	    if ((a % b[i]) == 0):
	        global_list.append('YES')
	        a = 0
	        break
	if (a != 0):
	    global_list.append('NO')
	return global_list