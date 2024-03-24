def func(*args):
	ret_values = []
	
	a = args[0]
	if (('1111111' in a) or ('0000000' in a)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
