def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
	flag = 0
	for i in lucky_numbers:
	    if ((n % i) == 0):
	        global_list.append('YES')
	        flag = 1
	        break
	if (flag == 0):
	    global_list.append('NO')
	return global_list