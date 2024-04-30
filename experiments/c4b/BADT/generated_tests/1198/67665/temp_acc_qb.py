def patched_func(*args):
	global_list = []
	
	word = []
	word = list(args[0])
	toggle = False
	if ('Q' in word):
	    toggle = True
	if ('9' in word):
	    toggle = True
	if ('H' in word):
	    toggle = True
	if (toggle == True):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list