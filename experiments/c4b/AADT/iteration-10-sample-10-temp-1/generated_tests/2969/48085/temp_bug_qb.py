def original_func(*args):
	global_list = []
	
	a = args[0].split(' ')
	s = int(a[0])
	v1 = int(a[1])
	v2 = int(a[2])
	t1 = int(a[3])
	t2 = int(a[4])
	first_time = ((s * v1) + (2 * t1))
	second_time = ((s * v2) + (2 * t2))
	if (first_time < second_time):
	    global_list.append('First')
	elif (second_time < first_time):
	    global_list.append('Second')
	else:
	    global_list.append('Freindship')
	return global_list