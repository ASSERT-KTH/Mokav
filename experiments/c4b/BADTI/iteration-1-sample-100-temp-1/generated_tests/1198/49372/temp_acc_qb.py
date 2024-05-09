def patched_func(*args):
	global_list = []
	
	program_language = 'HQ9+'
	n = args[0]
	yes = []
	for el in n:
	    if ((el in program_language) and (el != '+')):
	        yes.append('1')
	if yes:
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list