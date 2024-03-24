def func(*args):
	ret_values = []
	
	(k, a, b) = map(int, args[0].split())
	if (((a >= k) and (b >= k)) or (((a % k) == 0) and ((a // k) != 0)) or (((b % k) == 0) and ((b // k) != 0))):
	    exit(ret_values.append(((a // k) + (b // k))))
	exit(ret_values.append('-1'))

	return ret_values
