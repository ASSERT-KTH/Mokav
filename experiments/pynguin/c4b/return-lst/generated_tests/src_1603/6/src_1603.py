def func(*args):
	ret_values = []
	
	import re
	s = args[0]
	success = re.search('h.*e.*l.*l.*o', s)
	if (success is None):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
