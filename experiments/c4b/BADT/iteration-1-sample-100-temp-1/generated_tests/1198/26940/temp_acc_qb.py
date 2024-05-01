def patched_func(*args):
	global_list = []
	
	n = args[0]
	for i in n:
	    if (i in {'H', 'Q', '9'}):
	        global_list.append('YES')
	        break
	else:
	    global_list.append('NO')
	return global_list