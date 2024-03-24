def func(*args):
	ret_values = []
	
	i = sorted(list(map(int, args[0].split())))
	ret_values.append(min(((i[0] + i[1]) * 2), ((i[0] + i[2]) + i[1])))

	return ret_values
