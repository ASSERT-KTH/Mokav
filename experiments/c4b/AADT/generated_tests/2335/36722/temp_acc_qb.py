def patched_func(*args):
	global_list = []
	
	import re
	string = args[0]
	if re.match('\\w*h[a-z]*e[a-z]*l[a-z]*l[a-z]*o[a-z]*', string):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list