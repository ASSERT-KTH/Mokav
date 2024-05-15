def original_func(*args):
	global_list = []
	
	stri = args[0]
	b = []
	b = list(set(stri))
	if ((len(b) % 2) == 0):
	    global_list.append('CHAT WITH HER!')
	elif ((len(b) % 3) == 0):
	    global_list.append('IGNORE HIM!')
	return global_list