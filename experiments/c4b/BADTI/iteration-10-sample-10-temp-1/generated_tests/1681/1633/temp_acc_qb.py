def patched_func(*args):
	global_list = []
	
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
	global_list.append(solutions)
	return global_list