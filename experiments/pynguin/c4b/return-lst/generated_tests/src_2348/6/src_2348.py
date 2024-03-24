def func(*args):
	ret_values = []
	
	n = args[0]
	if ((('0' * 7) in n) or (('1' * 7) in n)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
