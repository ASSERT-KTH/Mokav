def patched_func(*args):
	global_list = []
	
	l = []
	for x in range(0, 26):
	    l.append(0)
	a = args[0]
	a = list(a)
	for x in a:
	    l[(ord(x.lower()) - 97)] = 1
	t = 0
	for x in l:
	    t = (t + x)
	if ((t % 2) == 0):
	    global_list.append('CHAT WITH HER!')
	else:
	    global_list.append('IGNORE HIM!')
	return global_list