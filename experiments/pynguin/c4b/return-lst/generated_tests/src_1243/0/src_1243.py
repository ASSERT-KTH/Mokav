def func(*args):
	ret_values = []
	
	(k, a, b) = map(int, args[0].split())
	first = ((a // k) * k)
	if (first < a):
	    first += k
	last = ((b // k) * k)
	if (last > b):
	    last -= k
	if (last < first):
	    ret_values.append(0)
	elif (last == first):
	    ret_values.append(1)
	else:
	    ret_values.append((((last - first) // k) + 1))

	return ret_values
