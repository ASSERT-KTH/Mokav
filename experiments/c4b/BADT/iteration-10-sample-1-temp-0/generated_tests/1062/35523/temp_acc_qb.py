def patched_func(*args):
	global_list = []
	
	t = args[0]
	res = 0
	for i in t:
	    if ((i == '4') or (i == '7')):
	        res += 1
	if ((res == 4) or (res == 7)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list