def func(*args):
	ret_values = []
	
	from math import floor, log
	rdi = (lambda : list(map(int, args[0].split())))
	(k, b, n, t) = rdi()
	if (k == 1):
	    ret_values.append(max(0, (((((1 + (n * b)) - t) + b) - 1) // b)))
	else:
	    ret_values.append(max(0, (n - floor(log((((t * (k - 1)) + b) / ((k - 1) + b)), k)))))

	return ret_values
