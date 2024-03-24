def func(*args):
	ret_values = []
	
	import re
	string = args[0]
	if re.match('\\w*h[a-z]*e[a-z]*l[a-z]*l[a-z]*o[a-z]*', string):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
