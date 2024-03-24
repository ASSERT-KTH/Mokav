def func(*args):
	ret_values = []
	
	n = int(args[0])
	if ((n % 2) > 0):
	    ret_values.append((- 1))
	else:
	    list = []
	    for i in range(1, (n + 1)):
	        if ((i % 2) > 0):
	            list.append((i + 1))
	        else:
	            list.append((i - 1))
	    ret_values.append(*list)

	return ret_values
