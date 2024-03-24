def func(*args):
	ret_values = []
	
	string = args[0]
	numbers = string.split(' ')
	n = int(numbers[0])
	a = int(numbers[1])
	b = int(numbers[2])
	x = abs((a + (b % n)))
	if ((x % n) == 0):
	    ret_values.append(n)
	else:
	    ret_values.append((x % n))

	return ret_values
