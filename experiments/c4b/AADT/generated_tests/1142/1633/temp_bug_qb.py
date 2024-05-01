def original_func(*args):
	global_list = []
	
	string = args[0]
	numbers = string.split(' ')
	n = int(numbers[0])
	a = int(numbers[1])
	b = int(numbers[2])
	s = (n - a)
	if (((a - b) == 0) or ((a - b) == 1)):
	    s -= (a - b)
	global_list.append(s)
	return global_list