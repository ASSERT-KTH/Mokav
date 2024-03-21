def func(*args):
	ret_values = []
	
	s = args[0]
	if (('1111111' in s) or ('0000000' in s)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
