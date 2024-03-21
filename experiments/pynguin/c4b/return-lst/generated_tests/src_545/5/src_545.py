def func(*args):
	ret_values = []
	
	n = int(args[0])
	x = [i for i in args[1]]
	the_stack = [x[0]]
	del x[0]
	while (x != []):
	    if (the_stack[(- 1)] == x[0]):
	        del x[0]
	    else:
	        the_stack.append(x[0])
	ret_values.append((n - len(the_stack)))

	return ret_values
