def func(*args):
	ret_values = []
	
	s = args[0].split()
	a = list(s)
	a[0] = int(a[0])
	if (a[2] == 'week'):
	    if ((a[0] > 4) and (a[0] < 7)):
	        ret_values.append(53)
	    else:
	        ret_values.append(52)
	elif (a[0] == 30):
	    ret_values.append(11)
	elif (a[0] == 31):
	    ret_values.append(7)
	else:
	    ret_values.append(12)

	return ret_values
