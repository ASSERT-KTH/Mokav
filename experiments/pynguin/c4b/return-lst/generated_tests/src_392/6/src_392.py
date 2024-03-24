def func(*args):
	ret_values = []
	
	string = args[0]
	numbers = string.split(' ')
	problems = int(numbers[0])
	minutes = int(numbers[1])
	total = 0
	i = 0
	while ((total <= (240 - minutes)) and (i <= problems)):
	    i += 1
	    total += (i * 5)
	ret_values.append((i - 1))

	return ret_values
