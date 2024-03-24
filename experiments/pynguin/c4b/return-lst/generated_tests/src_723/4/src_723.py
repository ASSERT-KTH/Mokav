def func(*args):
	ret_values = []
	
	L = [int(s) for s in args[0].split()]
	(k, a, b) = (L[0], L[1], L[2])
	if (((b - a) % k) == 0):
	    if ((a % k) == 0):
	        ret_values.append((((b - a) + k) // k))
	    else:
	        ret_values.append(((b - a) // k))
	elif ((a % k) == 0):
	    ret_values.append((((b // k) - (a // k)) + 1))
	elif ((b % k) == 0):
	    ret_values.append(((b // k) - (a // k)))
	else:
	    ret_values.append(((b // k) - (a // k)))

	return ret_values
