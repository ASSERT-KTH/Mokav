def func(*args):
	ret_values = []
	
	k = int(args[0])
	l = int(args[1])
	m = int(args[2])
	n = int(args[3])
	d = int(args[4])
	dragons = 0
	for x in range(1, (d + 1)):
	    if ((x % k) == 0):
	        dragons += 1
	    elif ((x % l) == 0):
	        dragons += 1
	    elif ((x % m) == 0):
	        dragons += 1
	    elif ((x % n) == 0):
	        dragons += 1
	ret_values.append(dragons)

	return ret_values
