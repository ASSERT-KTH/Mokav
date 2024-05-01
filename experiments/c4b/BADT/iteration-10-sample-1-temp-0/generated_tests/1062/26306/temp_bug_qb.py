def original_func(*args):
	global_list = []
	
	n = eval(args[0])
	while (n > 0):
	    k = (n % 10)
	    if ((k != 4) and (k != 7)):
	        global_list.append('NO')
	        break
	    n = (n // 10)
	else:
	    global_list.append('YES')
	return global_list