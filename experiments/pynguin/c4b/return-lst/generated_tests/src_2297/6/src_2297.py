def func(*args):
	ret_values = []
	
	k = int(args[0])
	l = int(args[1])
	m = int(args[2])
	n = int(args[3])
	d = int(args[4])
	if (k == 1):
	    ret_values.append(d)
	else:
	    list_drag = []
	    for i in range(1, (d + 1)):
	        if ((i % k) == 0):
	            list_drag.append(i)
	        if ((i % l) == 0):
	            list_drag.append(i)
	        if ((i % m) == 0):
	            list_drag.append(i)
	        if ((i % n) == 0):
	            list_drag.append(i)
	    a = set(list_drag)
	    ret_values.append(len(a))

	return ret_values
