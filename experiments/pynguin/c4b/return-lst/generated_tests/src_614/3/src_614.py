def func(*args):
	ret_values = []
	
	(k, a, b) = map(int, args[0].split())
	if (((a < k) and (b % k)) or ((b < k) and (a % k))):
	    ret_values.append((- 1))
	else:
	    ret_values.append(((a // k) + (b // k)))

	return ret_values
