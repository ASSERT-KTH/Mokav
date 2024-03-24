def func(*args):
	ret_values = []
	
	import sys
	(n, k) = args[0].strip().split()
	(n, k) = (int(n), int(k))
	k = (240 - k)
	i = 0
	for i in range(1, (n + 1)):
	    k = (k - (i * 5))
	    if (k < 0):
	        ret_values.append((i - 1))
	        break
	if ((i == n) and (k >= 0)):
	    ret_values.append(n)

	return ret_values
