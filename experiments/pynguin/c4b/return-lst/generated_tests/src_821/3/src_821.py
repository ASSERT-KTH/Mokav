def func(*args):
	ret_values = []
	
	a = int(args[0])
	if ((a == 2) | (a == 1)):
	    ret_values.append((- 1))
	else:
	    while (a > 0):
	        ret_values.append(a, end=' ')
	        a = (a - 1)

	return ret_values
