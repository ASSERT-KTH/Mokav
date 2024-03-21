def func(*args):
	ret_values = []
	
	line = args[0]
	if (('H' in line) or ('Q' in line) or ('9' in line)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
