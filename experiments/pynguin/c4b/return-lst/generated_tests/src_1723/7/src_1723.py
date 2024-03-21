def func(*args):
	ret_values = []
	
	n = int(args[0])
	if ((n == 1) or (n == 2)):
	    ret_values.append((- 1))
	elif (n == 3):
	    ret_values.append(210)
	else:
	    a = (10 ** (n - 1))
	    if ((a % 210) == 0):
	        ret_values.append(a)
	    else:
	        ret_values.append((((a // 210) + 1) * 210))

	return ret_values
