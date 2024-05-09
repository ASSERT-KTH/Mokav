def original_func(*args):
	global_list = []
	
	input = int(args[0])
	sum = 0
	temp = 0
	for i in range(input, 0, (- 1)):
	    sum += i
	for i in range(input, 0, (- 1)):
	    sum += ((i - 1) * temp)
	    temp += 1
	if (input == 2):
	    global_list.append(2)
	else:
	    global_list.append(sum)
	return global_list