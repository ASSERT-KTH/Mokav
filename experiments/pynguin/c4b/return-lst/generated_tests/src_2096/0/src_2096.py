def func(*args):
	ret_values = []
	
	kilo = args[0]
	kgs = int(kilo)
	if (((kgs % 2) == 0) and (kgs != 2)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
