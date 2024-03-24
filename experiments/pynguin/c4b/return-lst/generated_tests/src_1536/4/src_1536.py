def func(*args):
	ret_values = []
	
	x = int(args[0])
	if (x >= 6):
	    if ((x / 5) != (x // 5)):
	        i = ((x // 5) + 1)
	    else:
	        i = (x // 5)
	    ret_values.append(str(i))
	else:
	    ret_values.append('1')

	return ret_values
