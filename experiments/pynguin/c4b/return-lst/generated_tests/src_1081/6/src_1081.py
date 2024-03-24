def func(*args):
	ret_values = []
	
	(k, a, b) = map(int, args[0].split())
	if ((((a % k) > 0) and ((b // k) == 0)) or (((b % k) > 0) and ((a // k) == 0))):
	    ret_values.append((- 1))
	else:
	    ret_values.append(((a // k) + (b // k)))

	return ret_values
