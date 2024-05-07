def patched_func(*args):
	global_list = []
	
	string = args[0]
	code = 'HQ9'
	for i in string:
	    if (i in code):
	        global_list.append('YES')
	        break
	else:
	    global_list.append('NO')
	return global_list