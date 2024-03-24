def func(*args):
	ret_values = []
	
	(start, increment, check) = [int(x) for x in args[0].split(' ')]
	f = (((check - start) // increment) - 1)
	l = (((check - start) // increment) + 1)
	out = []
	for i in range(f, l):
	    out.append((start + (i * increment)))
	other = [(x + 1) for x in out if (x != start)]
	if (check < start):
	    ret_values.append('NO')
	elif ((check in out) or (check in other)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
