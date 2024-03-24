def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	(c, d) = map(int, args[1].split())
	r = set(range(b, 10000, a))
	m = set(range(d, 10000, c))
	ans = (r & m)
	if ans:
	    ret_values.append(min(ans))
	else:
	    ret_values.append((- 1))

	return ret_values
