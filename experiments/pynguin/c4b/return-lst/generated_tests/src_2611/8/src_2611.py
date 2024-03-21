def func(*args):
	ret_values = []
	
	(n, m) = map(int, args[0].rstrip().split())
	if (n <= m):
	    ret_values.append(n)
	else:
	    ans = m
	    n -= m
	    left = 0
	    right = (n + 1)
	    while ((right - left) > 1):
	        mid = (left + ((right - left) // 2))
	        if (n <= (((mid + 1) * mid) // 2)):
	            right = mid
	        else:
	            left = mid
	    ret_values.append((ans + right))

	return ret_values
