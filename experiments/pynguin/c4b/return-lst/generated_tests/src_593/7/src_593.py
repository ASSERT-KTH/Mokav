def func(*args):
	ret_values = []
	
	string = args[0]
	if (('H' in string) or ('Q' in string) or ('9' in string)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
