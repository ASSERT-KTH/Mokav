def func(*args):
	ret_values = []
	
	(c, a, b) = map(int, args[0].split())
	if ((a % c) == 0):
	    d = ((int((b // c)) - int((a // c))) + 1)
	else:
	    d = (int((b // c)) - int((a // c)))
	ret_values.append(d)

	return ret_values
