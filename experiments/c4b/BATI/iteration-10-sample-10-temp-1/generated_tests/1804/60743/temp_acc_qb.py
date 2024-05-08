def patched_func(*args):
	global_list = []
	
	word = args[0]
	jh = ''.join(set(word))
	if ((len(jh) % 2) == 0):
	    global_list.append('CHAT WITH HER!')
	else:
	    global_list.append('IGNORE HIM!')
	return global_list