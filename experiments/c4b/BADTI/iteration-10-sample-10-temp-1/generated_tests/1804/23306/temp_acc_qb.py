def patched_func(*args):
	global_list = []
	
	T = args[0]
	a = len(set(T))
	strq = ''
	for k in T:
	    if (not (k in T)):
	        strq += k
	if ((a % 2) == 0):
	    global_list.append('CHAT WITH HER!')
	else:
	    global_list.append('IGNORE HIM!')
	return global_list