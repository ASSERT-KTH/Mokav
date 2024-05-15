def original_func(*args):
	global_list = []
	
	string = args[0]
	numbers = string.split(' ')
	a = int(numbers[0])
	b = int(numbers[1])
	if (abs((a - b)) <= 1):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list