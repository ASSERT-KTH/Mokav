def patched_func(*args):
	global_list = []
	
	horseshoes_color = args[0].split()
	count = (len(horseshoes_color) - len(list(set(horseshoes_color))))
	global_list.append(count)
	return global_list