def patched_func(*args):
	global_list = []
	
	position = [int(i) for i in args[0].split()]
	position.sort()
	global_list.append(((position[2] - position[1]) + (position[1] - position[0])))
	return global_list