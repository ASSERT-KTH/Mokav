def func(*args):
	ret_values = []
	
	string = args[0]
	numbers = string.split(' ')
	a = int(numbers[0])
	b = int(numbers[1])
	if ((abs((a - b)) <= 1) and ((a + b) != 0)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
