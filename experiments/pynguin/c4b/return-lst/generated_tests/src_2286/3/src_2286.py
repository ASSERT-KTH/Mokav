def func(*args):
	ret_values = []
	
	import re
	ret_values.append(('YES' if re.match('.*h.*e.*l.*l.*o.*', str(args[0])) else 'NO'))

	return ret_values
