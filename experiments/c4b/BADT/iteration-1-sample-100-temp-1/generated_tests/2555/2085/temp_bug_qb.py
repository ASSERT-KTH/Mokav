def original_func(*args):
	global_list = []
	
	a = args[0]
	b = 0
	c = False
	for r in a:
	    if (r == '0'):
	        b += 1
	        if (b == 7):
	            c = True
	            break
	    else:
	        b = 0
	if c:
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list