def func(*args):
	ret_values = []
	
	num_turns = int(args[0])
	end_pos = int(args[1])
	zero_first_pos = [0, 1, 1, 2, 2, 0]
	one_first_pos = [1, 0, 2, 1, 0, 2]
	two_first_pos = [2, 2, 0, 0, 1, 1]
	if (end_pos == 0):
	    ret_values.append(zero_first_pos[(num_turns % 6)])
	elif (end_pos == 1):
	    ret_values.append(one_first_pos[(num_turns % 6)])
	else:
	    ret_values.append(two_first_pos[(num_turns % 6)])

	return ret_values
