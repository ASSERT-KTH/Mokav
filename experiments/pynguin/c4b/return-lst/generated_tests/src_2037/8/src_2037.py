def func(*args):
	ret_values = []
	
	(s, v1, v2, t1, t2) = map(int, args[0].split())
	if (((s * v1) + (t1 * 2)) < ((s * v2) + (t2 * 2))):
	    ret_values.append('First')
	elif (((s * v1) + (t1 * 2)) > ((s * v2) + (t2 * 2))):
	    ret_values.append('Second')
	else:
	    ret_values.append('Friendship')

	return ret_values
