def original_func(*args):
	global_list = []
	
	n = args[0]
	cont = 0
	for k in n:
	    if (n.count(k) == 1):
	        cont += 1
	if ((2 * cont) > len(n)):
	    global_list.append('CHAT WITH HER!')
	else:
	    global_list.append('IGNORE HIM!')
	return global_list