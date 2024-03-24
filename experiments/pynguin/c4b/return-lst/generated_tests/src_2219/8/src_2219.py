def func(*args):
	ret_values = []
	
	s = list(args[0])
	i = ['H', 'Q', '9']
	if any([x for x in i if (x in s)]):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
