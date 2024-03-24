def func(*args):
	ret_values = []
	
	(n, k) = args[0].split()
	n = int(n)
	k = int(k)
	nn = n
	arr = []
	for i in range(k):
	    arr.append(n)
	    n -= 1
	for i in range((nn - k)):
	    arr.append((i + 1))
	for i in range(nn):
	    ret_values.append(arr[i], end=' ')

	return ret_values
