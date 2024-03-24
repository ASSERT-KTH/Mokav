def func(*args):
	ret_values = []
	
	input_data = int(args[0])
	if (input_data != 2):
	    if ((input_data % 2) == 0):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')
	else:
	    ret_values.append('NO')

	return ret_values
