def original_func(*args):
	global_list = []
	
	a = int(args[0])
	b = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
	if (a in b):
	    global_list.append('YES')
	else:
	    for i in range(14):
	        if (((a % b[i]) == 0) and (a > b[i])):
	            global_list.append('YES')
	            break
	        else:
	            global_list.append('NO')
	            break
	return global_list