def patched_func(*args):
	global_list = []
	
	name = args[0]
	length = len(name)
	list = set()
	for letter in name:
	    list.add(letter)
	if ((len(list) % 2) == 0):
	    global_list.append('CHAT WITH HER!')
	else:
	    global_list.append('IGNORE HIM!')
	return global_list