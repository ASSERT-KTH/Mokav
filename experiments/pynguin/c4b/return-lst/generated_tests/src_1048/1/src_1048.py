def func(*args):
	ret_values = []
	
	temp = args[0]
	(k, a, b) = map(int, temp.split(' '))
	if (((a < k) and (b < k)) or ((a < k) and ((b % k) != 0)) or ((b < k) and ((a % k) != 0))):
	    ret_values.append((- 1))
	else:
	    ret_values.append(((a // k) + (b // k)))

	return ret_values
