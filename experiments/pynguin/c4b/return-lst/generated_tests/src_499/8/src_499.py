def func(*args):
	ret_values = []
	
	x = args[0]
	if ((x[0] == 'a') and (x[1] == '8')):
	    ret_values.append(3)
	elif ((x[0] == 'a') and (x[1] == '1')):
	    ret_values.append(3)
	elif ((x[0] == 'h') and (x[1] == '8')):
	    ret_values.append(3)
	elif ((x[0] == 'h') and (x[1] == '1')):
	    ret_values.append(3)
	elif (x[0] == 'h'):
	    ret_values.append(5)
	elif (x[0] == 'a'):
	    ret_values.append(5)
	elif (x[1] == '1'):
	    ret_values.append(5)
	elif (x[1] == '8'):
	    ret_values.append(5)
	else:
	    ret_values.append(8)

	return ret_values
