def func(*args):
	ret_values = []
	
	a = list(map(int, args[0].strip().split(' ')))
	a = sorted(a)
	d = (a[2] - a[0])
	ret_values.append(d)

	return ret_values
