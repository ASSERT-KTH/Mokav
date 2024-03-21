def func(*args):
	ret_values = []
	
	s = args[0]
	n = int(args[1])
	a = ['v', '<', '^', '>']
	k = (n % 4)
	if ((k % 2) == 0):
	    ret_values.append('undefined')
	elif (((a.index(s[2]) - a.index(s[0])) % 4) == k):
	    ret_values.append('cw')
	else:
	    ret_values.append('ccw')

	return ret_values
