def func(*args):
	ret_values = []
	
	import sys
	n = int(args[0])
	if ((n < 5) or ((n % 2) != 0)):
	    ret_values.append('0')
	else:
	    d = int((n / 2))
	    if ((d % 2) == 0):
	        ret_values.append((int((d / 2)) - 1))
	    else:
	        ret_values.append(int((d / 2)))

	return ret_values
