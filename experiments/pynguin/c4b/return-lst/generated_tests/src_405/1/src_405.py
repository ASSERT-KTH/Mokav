def func(*args):
	ret_values = []
	
	import math
	string = args[0]
	numbers = string.split(' ')
	a = int(numbers[0])
	b = int(numbers[1])
	solutions = 0
	for x in range((int(math.sqrt(a)) + 1)):
	    y = (a - (x ** 2))
	    if ((x + (y ** 2)) == b):
	        solutions += 1
	ret_values.append(solutions)

	return ret_values
