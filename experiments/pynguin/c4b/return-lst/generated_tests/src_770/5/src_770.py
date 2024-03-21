def func(*args):
	ret_values = []
	
	(n, k) = map(int, args[0].split())
	if ((k > n) or ((k == 1) and (n != 1))):
	    ret_values.append((- 1))
	else:
	    s = ('ab' * ((n // 2) + 1))[:n]
	    ret_values.append(((s[:(- (k - 2))] + ''.join([chr((97 + i)) for i in range(2, k)])) if (k > 2) else s))

	return ret_values
