def original_func(*args):
	global_list = []
	
	word = set(args[0])
	global_list.append(len(word))
	return global_list