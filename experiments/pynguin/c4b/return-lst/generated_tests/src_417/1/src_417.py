def func(*args):
	ret_values = []
	
	position = [int(i) for i in args[0].split()]
	position.sort()
	ret_values.append(((position[2] - position[1]) + (position[1] - position[0])))

	return ret_values
