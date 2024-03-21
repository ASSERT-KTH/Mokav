def func(*args):
	ret_values = []
	
	a = int(args[0])
	x = (a % 2)
	if (x == 1):
	    b = int((a / 2))
	    b = (b - 1)
	    str = '7'
	    for i in range(0, b):
	        str += '1'
	else:
	    b = int((a / 2))
	    str = '1'
	    b = (b - 1)
	    for i in range(0, b):
	        str += '1'
	ret_values.append(str)

	return ret_values
