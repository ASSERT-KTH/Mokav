def func(*args):
	ret_values = []
	
	from bisect import bisect_left
	arr = [(((((2 * i) + 1) ** 2) // 2) + 1) for i in range(7)]
	n = int(args[0])
	if (n == 3):
	    ret_values.append(5)
	else:
	    ret_values.append(((2 * bisect_left(arr, n)) + 1))

	return ret_values
