def func(*args):
	ret_values = []
	
	(s, v1, v2, t1, t2) = map(int, args[0].split())
	first = ((t1 + (v1 * s)) + t1)
	second = ((t2 + (v2 * s)) + t2)
	if (first < second):
	    ret_values.append('First')
	elif (first > second):
	    ret_values.append('Second')
	else:
	    ret_values.append('Friendship')

	return ret_values
