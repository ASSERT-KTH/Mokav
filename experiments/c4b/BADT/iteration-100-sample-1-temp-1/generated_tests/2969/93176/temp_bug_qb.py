def original_func(*args):
	global_list = []
	
	l = list((int(i) for i in args[0].split()))
	if (((l[0] / l[1]) + (2 * l[3])) == ((l[0] / l[2]) + (2 * l[4]))):
	    global_list.append('Friendship')
	elif (((l[0] / l[1]) + (2 * l[3])) > ((l[0] / l[2]) + (2 * l[4]))):
	    global_list.append('First')
	elif (((l[0] / l[1]) + (2 * l[3])) < ((l[0] / l[2]) + (2 * l[4]))):
	    global_list.append('Second')
	return global_list