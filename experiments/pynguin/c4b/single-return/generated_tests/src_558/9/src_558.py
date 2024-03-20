def func(*args):
	
	k = int(args[0])
	l = int(args[1])
	m = int(args[2])
	n = int(args[3])
	d = int(args[4])
	i = 1
	x = 0
	while (i <= d):
	    if ((i % k) == 0):
	        x += 1
	    elif ((i % l) == 0):
	        x += 1
	    elif ((i % m) == 0):
	        x += 1
	    elif ((i % n) == 0):
	        x += 1
	    i += 1
	return(x)
