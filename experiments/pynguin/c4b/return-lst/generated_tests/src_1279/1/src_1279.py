def func(*args):
	ret_values = []
	
	(d1, d2, d3) = map(int, args[0].split())
	s = []
	if (d1 < d2):
	    s.append(((d1 + d3) + d2))
	    s.append(((d1 * 2) + (d2 * 2)))
	    s.append(((d1 * 2) + (d3 * 2)))
	else:
	    s.append(((d1 + d3) + d2))
	    s.append(((d1 * 2) + (d2 * 2)))
	    s.append(((d2 * 2) + (d3 * 2)))
	ret_values.append(min(s))

	return ret_values
