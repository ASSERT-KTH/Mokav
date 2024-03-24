def func(*args):
	ret_values = []
	
	(y, k, n) = args[0].split()
	check = False
	(y, k, n) = [int(y), int(k), int(n)]
	if (y >= k):
	    a = (k - (y % k))
	    for i in range(a, n, k):
	        if ((i + y) <= n):
	            ret_values.append(i, end=' ')
	            check = True
	        else:
	            break
	elif (y < k):
	    a = (k - y)
	    for i in range(a, n, k):
	        if ((i + y) <= n):
	            check = True
	            ret_values.append(i, end=' ')
	        else:
	            break
	if (check == False):
	    ret_values.append('-1')

	return ret_values
