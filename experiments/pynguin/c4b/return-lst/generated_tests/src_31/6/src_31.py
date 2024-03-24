def func(*args):
	ret_values = []
	
	(n, k) = map(int, args[0].split())
	while (k != (2 ** n)):
	    if (k < (2 ** n)):
	        k = k
	    else:
	        k -= (2 ** n)
	    n -= 1
	ret_values.append((n + 1))

	return ret_values
