def patched_func(*args):
	global_list = []
	
	string = args[0]
	numbers = string.split(' ')
	n = int(numbers[0])
	a = int(numbers[1])
	b = int(numbers[2])
	x = abs((a + (b % n)))
	if ((x % n) == 0):
	    global_list.append(n)
	else:
	    global_list.append((x % n))
	return global_list