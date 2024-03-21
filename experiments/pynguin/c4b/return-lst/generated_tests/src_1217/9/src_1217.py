def func(*args):
	ret_values = []
	
	a = list(map(int, args[0].split()))
	a.sort()
	afstand = (abs((a[0] - a[1])) + abs((a[2] - a[1])))
	ret_values.append(afstand)

	return ret_values
