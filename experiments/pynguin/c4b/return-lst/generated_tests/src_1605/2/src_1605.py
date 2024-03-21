def func(*args):
	ret_values = []
	
	import re
	s = args[0]
	is_seven = re.search('1{7}|0{7}', s)
	if (is_seven is None):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
