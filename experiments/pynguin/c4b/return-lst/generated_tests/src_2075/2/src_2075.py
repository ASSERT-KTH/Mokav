def func(*args):
	ret_values = []
	
	peso_w = int(args[0])
	if (((peso_w % 2) == 0) and (peso_w != 0) and (peso_w > 2)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
