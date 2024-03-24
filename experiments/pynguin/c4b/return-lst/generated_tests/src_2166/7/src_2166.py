def func(*args):
	ret_values = []
	
	(n, k) = map(int, args[0].split())
	if ((n < k) or (k > 26)):
	    ret_values.append((- 1))
	elif (k == 1):
	    ret_values.append(('a' if (n == 1) else (- 1)))
	else:
	    ret_values.append((('ab' * ((n // 2) + 1))[:((n - k) + 2)] + 'cdefghijklmnopqrstuvwxyz'[:(k - 2)]))

	return ret_values
