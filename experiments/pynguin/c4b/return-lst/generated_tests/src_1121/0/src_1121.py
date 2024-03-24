def func(*args):
	ret_values = []
	
	from math import ceil
	n = int(args[0])
	if (n < 6):
	    ret_values.append(0)
	elif (n % 2):
	    ret_values.append(0)
	else:
	    x = (n // 2)
	    ret_values.append((ceil((x / 2)) - 1))

	return ret_values
