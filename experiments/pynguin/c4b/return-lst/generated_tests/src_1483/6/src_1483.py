def func(*args):
	ret_values = []
	
	import re
	reg = re.compile('(h)+[a-z]*(e)+[a-z]*(l)+[a-z]*(l)+[a-z]*(o)+[a-z]*')
	s1 = args[0]
	li = reg.findall(s1)
	if (not li):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
