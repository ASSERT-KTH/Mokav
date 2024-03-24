def func(*args):
	ret_values = []
	
	w = 0
	w = int(args[0])
	res = (w % 2)
	if ((res != 0) or (w <= 2)):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
