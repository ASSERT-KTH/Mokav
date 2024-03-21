def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n < 3):
	    ret_values.append((- 1))
	elif (n == 3):
	    ret_values.append(210)
	else:
	    x = (7 - [1, 3, 2, 6, 4, 5][((n - 1) % 6)])
	    if ((x % 2) == 1):
	        x += 7
	    while ((((x + 1) % 3) != 0) or ((x % 5) != 0)):
	        x += 14
	    ret_values.append(((10 ** (n - 1)) + x))

	return ret_values
