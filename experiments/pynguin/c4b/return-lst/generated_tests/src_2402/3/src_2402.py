def func(*args):
	ret_values = []
	
	mass = eval(args[0])
	if (((mass % 2) == 0) and (mass != 2)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
