def original_func(*args):
	global_list = []
	
	import re
	string = args[0]
	if re.match('\\w*h+e+l+l+o+', string):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list