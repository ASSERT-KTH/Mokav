def original_func(*args):
	global_list = []
	
	a = int(args[0])
	f = a
	c = 0
	for i in range(2, a):
	    a = f
	    while (a >= i):
	        b = (a % i)
	        a -= b
	        c += b
	        a = (a / i)
	    c += a
	d = (f - 2)
	global_list.append(('%d/%d' % (c, d)))
	return global_list