def func(*args):
	ret_values = []
	
	(a, b, c, d, e, f) = map(int, args[0].split())
	if ((((a * e) * c) < ((f * d) * b)) or ((c == 0) and d) or ((a == 0) and b and d)):
	    ret_values.append('Ron')
	else:
	    ret_values.append('Hermione')

	return ret_values
