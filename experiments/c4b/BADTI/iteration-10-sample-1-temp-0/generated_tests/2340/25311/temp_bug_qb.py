def original_func(*args):
	global_list = []
	
	import re
	s = 'HoUse'
	upper = re.findall('[A-Z]', s)
	lower = re.findall('[a-z]', s)
	if (len(upper) > len(lower)):
	    global_list.append(s.upper())
	else:
	    global_list.append(s.lower())
	return global_list