def func(*args):
	ret_values = []
	
	a = args[0]
	ret_values.append((a.upper() if ((sum((a.count(x) for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')) * 2) > len(a)) else a.lower()))

	return ret_values
