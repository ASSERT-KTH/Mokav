def patched_func(*args):
	global_list = []
	
	s = int(args[0])
	x = str(s)
	count = 0
	for k in range(len(x)):
	    if ((x[k] == '4') or (x[k] == '7')):
	        count += 1
	if ((count == 4) or (count == 7)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list