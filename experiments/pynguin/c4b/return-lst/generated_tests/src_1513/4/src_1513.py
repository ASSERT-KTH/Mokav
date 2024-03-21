def func(*args):
	ret_values = []
	
	text = args[0]
	if (('H' in text) or ('Q' in text) or ('9' in text)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
