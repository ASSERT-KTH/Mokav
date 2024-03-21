def func(*args):
	ret_values = []
	
	n = args[0]
	if (('H' in n) or ('Q' in n) or ('9' in n)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
