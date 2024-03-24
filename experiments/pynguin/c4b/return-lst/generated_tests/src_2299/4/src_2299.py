def func(*args):
	ret_values = []
	
	n = args[0]
	if (('1111111' in n) or ('0000000' in n)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
