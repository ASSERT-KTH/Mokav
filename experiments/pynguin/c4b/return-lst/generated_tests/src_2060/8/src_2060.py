def func(*args):
	ret_values = []
	
	(n, m, a) = map(int, args[0].split())
	s = (n / a)
	q = (m / a)
	if ((s % 1) > 0):
	    s = int((s + 1))
	if ((q % 1) > 0):
	    q = int((q + 1))
	ret_values.append(int((s * q)))

	return ret_values
