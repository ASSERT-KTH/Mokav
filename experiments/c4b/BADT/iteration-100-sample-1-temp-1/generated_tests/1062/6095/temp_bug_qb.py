def original_func(*args):
	global_list = []
	
	x = [int(y) for y in args[0]]
	i = 0
	while (i < len(x)):
	    if ((x[i] != 7) and (x[i] != 4)):
	        global_list.append('NO')
	        break
	    i += 1
	else:
	    global_list.append('YES')
	return global_list