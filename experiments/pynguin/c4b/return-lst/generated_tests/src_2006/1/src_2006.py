def func(*args):
	ret_values = []
	
	nk = args[0].split(' ')
	(n, k) = [int(x) for x in nk]
	while (k != (2 ** (n - 1))):
	    if (k > (2 ** (n - 1))):
	        k -= (2 ** (n - 1))
	    n -= 1
	ret_values.append(n)

	return ret_values
