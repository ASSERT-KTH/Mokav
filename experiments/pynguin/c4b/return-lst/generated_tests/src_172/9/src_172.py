def func(*args):
	ret_values = []
	
	s = args[0].split()
	x = int(s[0])
	if (s[2][0] == 'w'):
	    if ((x >= 5) and (x < 7)):
	        ret_values.append((52 + 1))
	    else:
	        ret_values.append(52)
	elif (x <= 29):
	    ret_values.append(12)
	elif (x == 30):
	    ret_values.append(11)
	else:
	    ret_values.append(7)

	return ret_values
