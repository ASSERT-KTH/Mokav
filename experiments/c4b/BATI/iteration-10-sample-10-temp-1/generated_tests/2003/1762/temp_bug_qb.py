def original_func(*args):
	global_list = []
	
	global_list.append(next((a for a in range(int(args[0]), 12345) if (len(set(str(a))) == len(str(a))))))
	return global_list