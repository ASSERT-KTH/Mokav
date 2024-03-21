def func(*args):
	ret_values = []
	
	n = int(args[0])
	a = (n // 4)
	b = (n % 4)
	if (((n % 2) == 0) and ((n // 4) >= 1)):
	    if (b == 2):
	        ret_values.append(a)
	    else:
	        ret_values.append((a - 1))
	else:
	    ret_values.append(0)

	return ret_values
