def original_func(*args):
	global_list = []
	
	import re
	s = args[0]
	success = re.search('h.+e.+l.+l.+o', s)
	if (success is None):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list