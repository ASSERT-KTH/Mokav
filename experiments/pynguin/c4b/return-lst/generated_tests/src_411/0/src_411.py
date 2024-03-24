def func(*args):
	ret_values = []
	
	string = args[0]
	(n, a, b) = map(int, string.split())
	
	def check(p, q):
	    return (((p % n) != 0) and (q < n))
	if (check(a, b) or check(b, a)):
	    ret_values.append((- 1))
	else:
	    ret_values.append(((a // n) + (b // n)))

	return ret_values
