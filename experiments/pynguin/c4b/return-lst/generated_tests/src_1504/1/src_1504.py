def func(*args):
	ret_values = []
	
	n = args[0]
	if (((n.count('4') + n.count('7')) == 7) or ((n.count('4') + n.count('7')) == 4)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
