def original_func(*args):
	global_list = []
	
	x = int(args[0])
	y = int(args[1])
	k = False
	u = 0
	for i in range(1, 32):
	    if (y == (x ** i)):
	        k = True
	        u = i
	        break
	if (k == False):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	    global_list.append('1')
	return global_list