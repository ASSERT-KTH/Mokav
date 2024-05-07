def patched_func(*args):
	global_list = []
	
	lucks = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
	num = int(args[0])
	flag = False
	for luck in lucks:
	    if ((num % luck) == 0):
	        flag = True
	if flag:
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list