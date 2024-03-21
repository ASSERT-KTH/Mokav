def func(*args):
	ret_values = []
	
	(s, v1, v2, t1, t2) = [int(i) for i in args[0].split()]
	if (((s * v1) + (2 * t1)) < ((s * v2) + (2 * t2))):
	    ret_values.append('First')
	elif (((s * v1) + (2 * t1)) > ((s * v2) + (2 * t2))):
	    ret_values.append('Second')
	else:
	    ret_values.append('Friendship')

	return ret_values
