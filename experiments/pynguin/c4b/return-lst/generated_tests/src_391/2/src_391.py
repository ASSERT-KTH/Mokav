def func(*args):
	ret_values = []
	
	string = args[0]
	numbers = string.split()
	a = int(numbers[1])
	n = 0
	while ((a % 2) == 0):
	    a /= 2
	    n += 1
	ret_values.append((n + 1))

	return ret_values
