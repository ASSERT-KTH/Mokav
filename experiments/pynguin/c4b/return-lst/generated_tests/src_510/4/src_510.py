def func(*args):
	ret_values = []
	
	n = int(args[0])
	ans = (n % 4)
	if (n == 0):
	    ret_values.append(1)
	elif (ans == 1):
	    ret_values.append(8)
	elif (ans == 2):
	    ret_values.append(4)
	elif (ans == 3):
	    ret_values.append(2)
	else:
	    ret_values.append(6)

	return ret_values
