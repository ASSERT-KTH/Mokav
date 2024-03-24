def func(*args):
	ret_values = []
	
	(n, m, a) = map(int, args[0].split())
	h = (n // a)
	if ((n % a) != 0):
	    h += 1
	w = (m // a)
	if ((m % a) != 0):
	    w += 1
	ret_values.append((h * w))

	return ret_values
