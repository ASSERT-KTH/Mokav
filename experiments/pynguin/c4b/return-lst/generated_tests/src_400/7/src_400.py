def func(*args):
	ret_values = []
	
	code = args[0]
	if (('H' in code) or ('Q' in code) or ('9' in code)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
