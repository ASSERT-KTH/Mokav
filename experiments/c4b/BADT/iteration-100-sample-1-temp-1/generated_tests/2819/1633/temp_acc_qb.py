def patched_func(*args):
	global_list = []
	
	string = args[0]
	numbers = string.split()
	a = int(numbers[0])
	b = int(numbers[1])
	if (a == b):
	    global_list.append(a)
	else:
	    global_list.append(2)
	return global_list