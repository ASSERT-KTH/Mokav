def func(*args):
	ret_values = []
	
	(n, a, b) = map(str, args[0].split())
	n = int(n)
	if (b == 'week'):
	    if ((n == 5) or (n == 6)):
	        ret_values.append(53)
	    else:
	        ret_values.append(52)
	elif (n == 31):
	    ret_values.append(7)
	elif (n == 30):
	    ret_values.append(11)
	else:
	    ret_values.append(12)

	return ret_values
