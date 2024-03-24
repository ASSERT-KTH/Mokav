def func(*args):
	ret_values = []
	
	l = list(map(int, args[0].split()))
	l.sort()
	ret_values.append((l[2] - l[0]))

	return ret_values
