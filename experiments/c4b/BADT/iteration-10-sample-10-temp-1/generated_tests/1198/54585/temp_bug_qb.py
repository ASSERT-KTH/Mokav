def original_func(*args):
	global_list = []
	
	import re
	char = str(args[0])
	cmd = ['H', 'Q', '9', '+']
	time = 0
	for c in cmd:
	    if (c in char):
	        time += 1
	if (time > 0):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list