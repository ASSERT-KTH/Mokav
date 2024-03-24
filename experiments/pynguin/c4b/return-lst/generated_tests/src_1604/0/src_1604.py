def func(*args):
	ret_values = []
	
	import re
	s = args[0]
	upper = re.findall('[A-Z]', s)
	lower = re.findall('[a-z]', s)
	if (len(upper) > len(lower)):
	    ret_values.append(s.upper())
	else:
	    ret_values.append(s.lower())

	return ret_values
