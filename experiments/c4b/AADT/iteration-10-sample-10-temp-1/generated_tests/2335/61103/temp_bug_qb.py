def original_func(*args):
	global_list = []
	
	import re
	if re.search('h+e+l+l+o+', args[0]):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list