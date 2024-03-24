def func(*args):
	ret_values = []
	
	a = int(args[0])
	if (a == 10):
	    ret_values.append(0, end='\n')
	elif ((a > 21) or (a < 10)):
	    ret_values.append(0)
	else:
	    a = (a % 10)
	    if (a == 0):
	        ret_values.append(15)
	    else:
	        ret_values.append(4)

	return ret_values
