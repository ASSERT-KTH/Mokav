def original_func(*args):
	global_list = []
	
	n = args[0]
	global_list.append(((((n.count('0') + n.count('4')) + n.count('6')) + (n.count('8') * 2)) + n.count('9')))
	return global_list