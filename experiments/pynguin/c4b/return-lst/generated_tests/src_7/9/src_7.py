def func(*args):
	ret_values = []
	
	(a, b, n) = map(int, args[0].split())
	if (((a % b) == 0) or (((a * 10) % b) == 0)):
	    ret_values.append(a, end='')
	    ret_values.append(('0' * n), end='')
	elif ((b - (((a % b) * 10) % b)) >= 10):
	    ret_values.append((- 1))
	else:
	    ret_values.append(a, end='')
	    ret_values.append((b - (((a % b) * 10) % b)), end='')
	    ret_values.append(('0' * (n - 1)))

	return ret_values
