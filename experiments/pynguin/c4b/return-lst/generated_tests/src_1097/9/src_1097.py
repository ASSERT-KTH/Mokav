def func(*args):
	ret_values = []
	
	(n, m) = map(int, args[0].split())
	if (n <= m):
	    ret_values.append(n)
	else:
	    aM = m
	    n -= m
	    (l, r) = (0, int(2000000000.0))
	    while (l < r):
	        m = ((l + r) // 2)
	        val = ((m * (m + 1)) // 2)
	        if (val >= n):
	            r = m
	        else:
	            l = (m + 1)
	    ret_values.append((l + aM))

	return ret_values
