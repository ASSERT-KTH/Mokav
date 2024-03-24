def func(*args):
	ret_values = []
	
	lisa = args[0]
	if (('H' in lisa) or ('Q' in lisa) or ('9' in lisa)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
