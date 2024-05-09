def original_func(*args):
	global_list = []
	
	k = int(args[0])
	l = int(args[1])
	r = (- 1)
	while (l > 1):
	    if ((l % k) != 0):
	        global_list.append('NO')
	        break
	    else:
	        r += 1
	        l //= k
	else:
	    global_list.append(r)
	return global_list