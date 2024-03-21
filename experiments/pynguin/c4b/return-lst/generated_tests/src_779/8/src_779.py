def func(*args):
	ret_values = []
	
	n = int(args[0])
	q = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	s = 5
	d = 1
	acc = 5
	while (n > acc):
	    d = (d * 2)
	    acc += (d * s)
	n -= (5 * (d - 1))
	if (n <= (d * 1)):
	    ret_values.append(q[0])
	elif (n <= (d * 2)):
	    ret_values.append(q[1])
	elif (n <= (d * 3)):
	    ret_values.append(q[2])
	elif (n <= (d * 4)):
	    ret_values.append(q[3])
	else:
	    ret_values.append(q[4])

	return ret_values
