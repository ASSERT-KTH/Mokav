def func(*args):
	ret_values = []
	
	x = args[0]
	i = 0
	j = 1
	if ((x.find('9') != (- 1)) or (x.find('H') != (- 1)) or (x.find('Q') != (- 1))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
