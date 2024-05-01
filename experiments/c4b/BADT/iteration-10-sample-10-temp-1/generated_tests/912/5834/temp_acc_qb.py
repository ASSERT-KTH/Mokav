def patched_func(*args):
	global_list = []
	
	numbers = [int(x) for x in args[0].split(' ')]
	limaks_spare_time = (240 - numbers[1])
	solving_time = 0
	for i in range(1, (numbers[0] + 1)):
	    solving_time += (5 * i)
	    if (solving_time > limaks_spare_time):
	        global_list.append((i - 1))
	        break
	if (solving_time <= limaks_spare_time):
	    global_list.append(numbers[0])
	return global_list