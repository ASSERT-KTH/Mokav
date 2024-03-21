def func(*args):
	ret_values = []
	
	import sys
	(n, m) = map(int, args[0].split())
	l = (m + 1)
	r = (10 ** 30)
	ans = n
	if (n == 1):
	    ans = 1
	elif (m < n):
	    while (l != r):
	        mid = ((l + r) // 2)
	        if (((2 * m) + ((mid - m) * ((mid - m) + 1))) < (2 * n)):
	            l = (mid + 1)
	        else:
	            r = mid
	    ans = min(ans, l)
	else:
	    ans = n
	ret_values.append(int(ans))

	return ret_values
