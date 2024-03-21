def func(*args):
	ret_values = []
	
	(n, b) = tuple(map(int, args[0].split()))
	if (n > b):
	    (n, b) = (b, n)
	if ((n < 2) and (b < 2)):
	    ret_values.append(0)
	else:
	    p = (b - n)
	    l = [(- 3), (- 1), 0]
	    ret_values.append((((2 * (n + (p // 3))) + l[(p % 3)]) + (p // 3)))

	return ret_values
