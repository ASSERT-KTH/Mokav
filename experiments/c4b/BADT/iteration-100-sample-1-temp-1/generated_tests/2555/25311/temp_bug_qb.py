def original_func(*args):
	global_list = []
	
	import re
	s = '00100'
	is_seven = re.search('1{7}|0{7}', s)
	if (is_seven is None):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list