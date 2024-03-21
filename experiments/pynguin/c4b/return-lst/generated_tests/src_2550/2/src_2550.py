def func(*args):
	ret_values = []
	
	l = tuple((int(i) for i in args[0].split()))
	if (((l[0] * l[1]) + (2 * l[3])) == ((l[0] * l[2]) + (2 * l[4]))):
	    ret_values.append('Friendship')
	elif (((l[0] * l[1]) + (2 * l[3])) < ((l[0] * l[2]) + (2 * l[4]))):
	    ret_values.append('First')
	elif (((l[0] * l[1]) + (2 * l[3])) > ((l[0] * l[2]) + (2 * l[4]))):
	    ret_values.append('Second')

	return ret_values
