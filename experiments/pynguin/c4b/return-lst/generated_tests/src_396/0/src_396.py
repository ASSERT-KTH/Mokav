def func(*args):
	ret_values = []
	
	n = int(args[0])
	a = (n // 7)
	for x in range(a, (- 1), (- 1)):
	    if (((n - (x * 7)) % 4) == 0):
	        ret_values.append((('4' * ((n - (x * 7)) // 4)) + ('7' * x)))
	        break
	else:
	    ret_values.append((- 1))

	return ret_values
