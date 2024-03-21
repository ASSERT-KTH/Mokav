def func(*args):
	ret_values = []
	
	n = args[0].split()
	if (n[(- 1)] == 'month'):
	    if (n[0] == '31'):
	        ret_values.append(7)
	    elif (n[0] == '30'):
	        ret_values.append(11)
	    else:
	        ret_values.append(12)
	elif (n[0] in ['1', '2', '3', '4', '7']):
	    ret_values.append(52)
	else:
	    ret_values.append(53)

	return ret_values
