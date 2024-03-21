def func(*args):
	ret_values = []
	
	a = list(args[0])
	if (('H' in a) or ('Q' in a) or ('9' in a)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
