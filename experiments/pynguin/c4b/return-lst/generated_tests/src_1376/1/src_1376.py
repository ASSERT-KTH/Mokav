def func(*args):
	ret_values = []
	
	n = int(args[0])
	if ((n % 2) == 0):
	    a = (n / 2)
	    i = (a // 2)
	    if ((a % 2) == 0):
	        i = (i - 1)
	    ret_values.append(int(i))
	else:
	    ret_values.append(0)

	return ret_values
