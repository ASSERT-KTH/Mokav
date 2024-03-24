def func(*args):
	ret_values = []
	
	l = list(args[0])
	if ('H' in l):
	    ret_values.append('YES')
	elif ('Q' in l):
	    ret_values.append('YES')
	elif ('9' in l):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
