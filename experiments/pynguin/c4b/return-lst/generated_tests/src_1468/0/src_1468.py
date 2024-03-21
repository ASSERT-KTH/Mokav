def func(*args):
	ret_values = []
	
	l = list(args[0])
	if (((l.count('4') + l.count('7')) == 4) or ((l.count('4') + l.count('7')) == 7)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
