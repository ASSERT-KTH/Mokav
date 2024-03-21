def func(*args):
	ret_values = []
	
	from math import log, ceil
	(k, b, n, t) = map(int, args[0].split())
	if (k == 1):
	    ret_values.append(max(0, ceil((((1 + (b * n)) - t) / b))))
	else:
	    ret_values.append(max(0, ceil((n - log((((t - (t * k)) - b) / ((1 - k) - b)), k)))))

	return ret_values
