def patched_func(*args):
	global_list = []
	
	p = args[0]
	count = 0
	for x in p:
	    if ((x == 'H') or (x == 'Q') or (x == '9')):
	        global_list.append('YES')
	        break
	    if (count == (len(p) - 1)):
	        global_list.append('NO')
	    count += 1
	return global_list