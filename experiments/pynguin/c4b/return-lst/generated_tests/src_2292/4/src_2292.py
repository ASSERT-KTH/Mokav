def func(*args):
	ret_values = []
	
	s = args[0]
	if (('H' in s) or ('Q' in s) or ('9' in s)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
