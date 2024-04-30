def original_func(*args):
	global_list = []
	
	plus = int(args[0])
	start = int(args[1])
	start = ((plus + (3 - start)) % 6)
	if (start <= 1):
	    global_list.append('2')
	elif ((start == 2) or (start == 5)):
	    global_list.append('1')
	else:
	    global_list.append('0')
	return global_list