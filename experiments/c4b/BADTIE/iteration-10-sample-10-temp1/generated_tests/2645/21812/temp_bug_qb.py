def original_func(*args):
	global_list = []
	
	num_turns = int(args[0])
	end_pos = int(args[1])
	zero_first_pos = [0, 1, 1, 2, 2, 1]
	one_first_pos = [1, 0, 2, 1, 0, 2]
	two_first_pos = [2, 2, 0, 0, 1, 1]
	if (end_pos == 0):
	    global_list.append(zero_first_pos[(num_turns % 6)])
	elif (end_pos == 1):
	    global_list.append(one_first_pos[(num_turns % 6)])
	else:
	    global_list.append(two_first_pos[(num_turns % 6)])
	return global_list