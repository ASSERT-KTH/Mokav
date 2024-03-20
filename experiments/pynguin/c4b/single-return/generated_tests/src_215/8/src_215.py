def func(*args):
	
	k = int(args[0])
	l = int(args[1])
	m = int(args[2])
	n = int(args[3])
	d = int(args[4])
	hurt = 0
	count = 1
	while (count <= d):
	    if (((count % k) == 0) or ((count % m) == 0) or ((count % n) == 0) or ((count % l) == 0)):
	        hurt += 1
	    count = (count + 1)
	return(hurt)
