def func(*args):
	ret_values = []
	
	[h1, h2] = list(map(int, args[0].split()))
	[a, b] = list(map(int, args[1].split()))
	if ((h1 + (8 * a)) >= h2):
	    ret_values.append(0)
	    exit(0)
	elif (a <= b):
	    ret_values.append((- 1))
	    exit(0)
	d = (h1 + (8 * a))
	res = int(((((h2 - d) + (12 * (a - b))) - 1) / (12 * (a - b))))
	ret_values.append(res)

	return ret_values
