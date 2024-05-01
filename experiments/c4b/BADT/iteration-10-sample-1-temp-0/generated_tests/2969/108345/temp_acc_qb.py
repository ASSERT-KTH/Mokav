def patched_func(*args):
	global_list = []
	
	(s, v_1, v_2, t_1, t_2) = [int(num) for num in args[0].strip().split(' ')]
	
	def compute_time(time_for_char, delay, num_chars):
	    return ((2 * delay) + (time_for_char * num_chars))
	(time_1, time_2) = (compute_time(v_1, t_1, s), compute_time(v_2, t_2, s))
	if (time_1 < time_2):
	    global_list.append('First')
	elif (time_1 > time_2):
	    global_list.append('Second')
	else:
	    global_list.append('Friendship')
	return global_list