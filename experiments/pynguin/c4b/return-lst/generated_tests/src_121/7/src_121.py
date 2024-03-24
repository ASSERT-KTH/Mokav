def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n == 0):
	    ret_values.append(1)
	else:
	    ans = 1
	    for i in range((n - 1)):
	        ans *= 3
	    ret_values.append((ans % 1000003))

	return ret_values
