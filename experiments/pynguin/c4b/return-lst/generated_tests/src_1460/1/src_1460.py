def func(*args):
	ret_values = []
	
	import re
	x = args[0]
	x.lower()
	if re.search('h.*e.*l.*l.*o', x):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
