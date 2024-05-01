def patched_func(*args):
	global_list = []
	
	numbers = [int(x) for x in args[0].split(' ')]
	a = numbers[0]
	b = numbers[1]
	for i in range(1, 100000):
	    if (((((a * i) - b) % 10) == 0) or (((a * i) % 10) == 0)):
	        global_list.append(i)
	        break
	return global_list