def func(*args):
	ret_values = []
	
	string = args[0]
	numbers = string.split(' ')
	a = int(numbers[0])
	b = int(numbers[1])
	c = int(numbers[2])
	condition = (((c - a) == 0) or ((c - a) >= b))
	if ((((c - a) % b) <= 1) and condition):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
