def patched_func(*args):
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
	h = 1
	for i in range(1, d):
	    if (((c / i) == int((c / i))) and ((d / i) == int((d / i)))):
	        h = i
	global_list.append(('%d/%d' % ((c / h), (d / h))))
	return global_list