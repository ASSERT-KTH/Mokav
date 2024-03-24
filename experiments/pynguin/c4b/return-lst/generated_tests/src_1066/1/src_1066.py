def func(*args):
	ret_values = []
	
	x = int(args[0])
	y = int(args[1])
	z = int(args[2])
	ret_values.append((min(x, (y // 2), (z // 4)) * 7))

	return ret_values
