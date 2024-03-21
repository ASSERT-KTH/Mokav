def func(*args):
	ret_values = []
	
	from string import ascii_lowercase
	(n, k) = [int(x) for x in args[0].split()]
	if ((n == 1) and (k == 1)):
	    ret_values.append('a')
	    exit(0)
	if ((n < k) or (k == 1)):
	    ret_values.append((- 1))
	    exit(0)
	ret_values.append(((('ab' * (((n - k) + 2) // 2)) + ('a' if (((n + k) % 2) == 1) else '')) + ascii_lowercase[2:k]))

	return ret_values
