def func(*args):
	ret_values = []
	
	s = args[0].split()
	s1 = int(s[0])
	if (s[2] == 'week'):
	    if ((s1 == 5) or (s1 == 6)):
	        ret_values.append(53)
	    else:
	        ret_values.append(52)
	elif (s1 == 31):
	    ret_values.append(7)
	elif (s1 == 30):
	    ret_values.append(11)
	else:
	    ret_values.append(12)

	return ret_values
