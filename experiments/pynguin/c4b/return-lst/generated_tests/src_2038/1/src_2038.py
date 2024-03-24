def func(*args):
	ret_values = []
	
	k = int(args[0])
	l = int(args[1])
	m = int(args[2])
	n = int(args[3])
	d = int(args[4])
	min_number = min(k, l, m, n)
	if (min_number == 1):
	    ret_values.append(d)
	    quit()
	if (min_number > d):
	    ret_values.append(0)
	    quit()
	for i in range(1, (d + 1)):
	    if (((i % k) != 0) and ((i % l) != 0) and ((i % m) != 0) and ((i % n) != 0)):
	        d -= 1
	ret_values.append(d)

	return ret_values
