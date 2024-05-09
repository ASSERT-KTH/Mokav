def original_func(*args):
	global_list = []
	
	(n, a, b, c) = (int(x) for x in args[0].split())
	(sum, k) = (0, ((4 - (n % 4)) % 4))
	if ((2 * a) > b):
	    sum = (((k // 2) * b) + ((k % 2) * a))
	elif (((3 * a) > c) and ((a + b) > c)):
	    sum = (((k // 3) * c) + ((k % 3) * a))
	else:
	    sum = (k * a)
	if ((k % 3) == 0):
	    sum = min(sum, (c * (k // 3)))
	if ((k % 2) == 0):
	    sum = min(sum, (b * (k // 2)))
	if (((n + 6) % 4) == 0):
	    sum = min((2 * c), sum)
	if (((n + 9) % 4) == 0):
	    sum = min(sum, (3 * c))
	global_list.append(min(sum, (a * k)))
	return global_list