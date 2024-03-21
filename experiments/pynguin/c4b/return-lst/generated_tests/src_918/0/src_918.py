def func(*args):
	ret_values = []
	
	(n, k) = map(int, args[0].split())
	ans = 0
	for i in range(1, (round((n ** 0.5)) + 2)):
	    if ((n % i) == 0):
	        if (((((k * (k - 1)) // 2) * i) < n) and ((n - (((k * (k - 1)) // 2) * i)) > 0) and ((n - (((k * (k - 1)) // 2) * i)) > ((k - 1) * i))):
	            ans = max(ans, i)
	        i = (n // i)
	        if (((((k * (k - 1)) // 2) * i) < n) and ((n - (((k * (k - 1)) // 2) * i)) > 0) and ((n - (((k * (k - 1)) // 2) * i)) > ((k - 1) * i))):
	            ans = max(ans, i)
	            i = (n // i)
	if (((k * (k + 1)) // 2) > n):
	    ret_values.append((- 1))
	else:
	    ret_values.append(' '.join(([str((ans * i)) for i in range(1, k)] + [str((n - (((k * (k - 1)) // 2) * ans)))])))

	return ret_values
