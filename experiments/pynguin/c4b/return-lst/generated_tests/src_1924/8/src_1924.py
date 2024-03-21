def func(*args):
	ret_values = []
	
	(m, d) = map(int, args[0].split())
	if (m < 8):
	    if ((m % 2) != 0):
	        if (d < 6):
	            ret_values.append('5')
	        else:
	            ret_values.append('6')
	    elif (m == 2):
	        if (d == 1):
	            ret_values.append('4')
	        else:
	            ret_values.append('5')
	    elif (d < 7):
	        ret_values.append('5')
	    else:
	        ret_values.append('6')
	elif ((m % 2) != 0):
	    if (d < 7):
	        ret_values.append('5')
	    else:
	        ret_values.append('6')
	elif (d < 6):
	    ret_values.append('5')
	else:
	    ret_values.append('6')

	return ret_values
