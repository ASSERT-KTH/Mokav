def original_func(*args):
	global_list = []
	
	x = args[0]
	m = len(''.join(set(x)))
	m = int(m)
	if ((m % 2) == 0):
	    global_list.append('CHAT WITH HER!')
	else:
	    global_list.append('IGNORE HIM')
	return global_list