def func(*args):
	ret_values = []
	
	coords = list(map(int, args[0].split()))
	coords.sort()
	ret_values.append((coords[2] - coords[0]))

	return ret_values
