def func(*args):
	ret_values = []
	
	p = args[0]
	if (('H' in p) or ('Q' in p) or ('9' in p)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
