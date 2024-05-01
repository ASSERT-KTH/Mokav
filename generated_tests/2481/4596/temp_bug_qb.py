def original_func(*args):
	global_list = []
	
	n = int(args[0])
	q = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	s = 1
	d = 1
	while (n > (5 * s)):
	    d += 1
	    s = (s * 5)
	n -= (5 * (d - 1))
	if (n <= (d * 1)):
	    global_list.append(q[0])
	elif (n <= (d * 2)):
	    global_list.append(q[1])
	elif (n <= (d * 3)):
	    global_list.append(q[2])
	elif (n <= (d * 4)):
	    global_list.append(q[3])
	else:
	    global_list.append(q[4])
	return global_list