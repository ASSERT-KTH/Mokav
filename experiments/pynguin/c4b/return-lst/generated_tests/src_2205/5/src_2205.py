def func(*args):
	ret_values = []
	
	import string
	rd = (lambda : list(map(int, args[0].split())))
	(n, k) = rd()
	if ((k > 26) or (k > n) or ((k == 1) and (n > 1))):
	    ret_values.append((- 1))
	elif ((k == 1) and (n == 1)):
	    ret_values.append('a')
	else:
	    ret_values.append((('ab' * ((n + 1) >> 1))[:((n - k) + 2)] + string.ascii_lowercase[2:k]))

	return ret_values
