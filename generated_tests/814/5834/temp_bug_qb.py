def original_func(*args):
	global_list = []
	
	numbers = [int(x) for x in args[0].split(' ')]
	a = numbers[0]
	b = numbers[1]
	for i in range(100000):
	    if ((((a * i) - b) % 10) == 0):
	        global_list.append(i)
	        break
	return global_list