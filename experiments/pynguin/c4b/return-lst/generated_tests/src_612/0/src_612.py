def func(*args):
	ret_values = []
	
	(n, cur) = (int(args[0]), 0)
	for i in range(1, n):
	    cur = ((cur + i) % n)
	    ret_values.append((cur + 1), end=' ')

	return ret_values
