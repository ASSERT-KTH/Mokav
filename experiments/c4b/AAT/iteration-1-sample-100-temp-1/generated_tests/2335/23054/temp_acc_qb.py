def patched_func(*args):
	global_list = []
	
	import re
	x = args[0]
	x.lower()
	if re.search('h.*e.*l.*l.*o', x):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list