def original_func(*args):
	global_list = []
	
	import re
	if (re.compile('(\\w){1,16}@((\\w{1,16}\\.)*)\\w{1,16}(/){1}\\w*$').match(args[0]) != None):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list