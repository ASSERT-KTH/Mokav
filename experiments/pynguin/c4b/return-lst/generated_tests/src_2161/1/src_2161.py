def func(*args):
	ret_values = []
	
	from math import log
	(k, b, n, t) = map(int, args[0].split())
	if (k == 1):
	    ret_values.append(max(((((n * b) + b) - t) // b), 0))
	else:
	    ret_values.append(max(0, (n - int((log(((((k * t) - t) + b) / ((k - 1) + b))) / log(k))))))

	return ret_values
