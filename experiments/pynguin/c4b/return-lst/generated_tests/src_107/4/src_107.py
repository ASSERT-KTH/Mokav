def func(*args):
	ret_values = []
	
	a = [int(x) for x in args[0].split(' ')]
	a.sort()
	dist = (a[2] - a[0])
	ret_values.append(dist)

	return ret_values
