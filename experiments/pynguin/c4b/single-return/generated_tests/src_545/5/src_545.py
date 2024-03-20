def func(*args):
	
	n = int(args[0])
	x = [i for i in args[1]]
	the_stack = [x[0]]
	del x[0]
	while (x != []):
	    if (the_stack[(- 1)] == x[0]):
	        del x[0]
	    else:
	        the_stack.append(x[0])
	return((n - len(the_stack)))
