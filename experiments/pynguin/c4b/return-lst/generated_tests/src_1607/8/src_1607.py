def func(*args):
	ret_values = []
	
	m = int(args[0])
	if (m == 1):
	    ret_values.append('1')
	elif (m == 2):
	    ret_values.append('2')
	elif ((m % 2) == 0):
	    if ((m % 3) == 0):
	        ans = (((m - 1) * (m - 2)) * (m - 3))
	    else:
	        ans = ((m * (m - 1)) * (m - 3))
	    ret_values.append(round(ans))
	else:
	    ret_values.append(((m * (m - 1)) * (m - 2)))

	return ret_values
