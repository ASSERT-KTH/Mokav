def func(*args):
	ret_values = []
	
	string = args[0]
	numbers = string.split()
	a = int(numbers[0])
	b = int(numbers[1])
	if (a == b):
	    ret_values.append(a)
	else:
	    ret_values.append(2)

	return ret_values
