def func(*args):
	ret_values = []
	
	program = args[0]
	if (('H' in program) or ('Q' in program) or ('9' in program)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
