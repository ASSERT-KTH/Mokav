def original_func(*args):
	global_list = []
	
	n = int(args[0])
	y = n
	k = 2
	p = 0
	for q in range(0, (n - 2)):
	    n = y
	    while (n > 1):
	        a = (n % k)
	        n = (n // k)
	        p = (p + a)
	    p = (p + n)
	    k = (k + 1)
	t = (k - 2)
	global_list.append(((str(p) + '/') + str(t)))
	return global_list