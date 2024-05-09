def original_func(*args):
	global_list = []
	
	import re
	x = args[0]
	x.lower()
	if re.search('h.*e.*l.*l.*o', x):
	    global_list.append('YES')
	else:
	    'NO'
	return global_list