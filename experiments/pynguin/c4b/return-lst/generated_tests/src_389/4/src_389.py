def func(*args):
	ret_values = []
	
	digits = [2, 3, 5, 6]
	string = args[0]
	numbers = string.split(' ')
	for x in range(4):
	    numbers[x] = int(numbers[x])
	maximum = min([numbers[0], numbers[2], numbers[3]])
	numbers[0] -= maximum
	maximum *= 256
	maximum += (min([numbers[0], numbers[1]]) * 32)
	ret_values.append(maximum)

	return ret_values
