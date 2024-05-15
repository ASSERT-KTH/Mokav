def original_func(*args):
	global_list = []
	
	n = int(args[0])
	x = [i for i in args[1]]
	the_stack = [x[0]]
	del x[0]
	d_max = (n - 1)
	for i in range(1, n):
	    if (the_stack[(- 1)] == x[0]):
	        the_stack.append(x[0])
	        del x[0]
	        continue
	    elif (the_stack != x[0]):
	        l = len(the_stack)
	        if ((l - 1) < d_max):
	            d_max = (l - 1)
	        the_stack = [x[0]]
	        del x[0]
	        continue
	if ((len(the_stack) < d_max) and (len(the_stack) > 1)):
	    d_max = len(the_stack)
	global_list.append(d_max)
	return global_list