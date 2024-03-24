def func(*args):
	ret_values = []
	
	(k, x) = map(int, args[0].split())
	y = 0
	while True:
	    if (((y % k) == 0) and y):
	        ret_values.append((y // k))
	        break
	    if (((y + x) % k) == 0):
	        ret_values.append(((y + x) // k))
	        break
	    y += 10

	return ret_values
