def func(*args):
	ret_values = []
	
	a = int(args[0])
	if (a < 13):
	    ret_values.append((2 ** a))
	else:
	    start = 8092
	    for _ in range((a - 13)):
	        start *= 2
	    ret_values.append(start)

	return ret_values
