def original_func(*args):
	global_list = []
	
	word = args[0]
	word = ''.join(set(word))
	if ((len(word) % 2) == 0):
	    global_list.append('CHAT WITH HER')
	else:
	    global_list.append('IGNORE HIM!')
	return global_list