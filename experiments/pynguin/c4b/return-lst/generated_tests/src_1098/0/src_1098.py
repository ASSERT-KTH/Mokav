def func(*args):
	ret_values = []
	
	n = int(args[0])
	m = 1
	M = (10 ** 8)
	mid = ((m + M) // 2)
	s = ((mid * (mid + 1)) // 2)
	s1 = ((s + mid) + 1)
	while (not ((s <= n) and (s1 > n))):
	    mid = ((m + M) // 2)
	    s = ((mid * (mid + 1)) // 2)
	    s1 = ((s + mid) + 1)
	    if ((s < n) and (s1 < n)):
	        m = mid
	    elif (s > n):
	        M = mid
	    else:
	        break
	if (s == n):
	    ret_values.append(mid)
	else:
	    ret_values.append((n - s))

	return ret_values
