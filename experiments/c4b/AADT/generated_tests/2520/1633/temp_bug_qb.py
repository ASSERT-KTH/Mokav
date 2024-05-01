def original_func(*args):
	global_list = []
	
	string = args[0]
	numbers = string.split()
	x = int(numbers[0])
	y = int(numbers[1])
	n = ((6 - max([x, y])) + 1)
	global_list.append((str(n) + '/6'))
	return global_list