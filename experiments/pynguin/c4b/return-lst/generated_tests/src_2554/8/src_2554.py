def func(*args):
	ret_values = []
	
	numb = int(args[0])
	if (((numb % 2) == 0) and (numb != 2) and (numb != 0)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
