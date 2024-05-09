def patched_func(*args):
	global_list = []
	
	x = int(args[0])
	s = ''
	if ((x % 2) == 0):
	    for i in range((x // 2)):
	        s = (s + '1')
	    global_list.append(s)
	if ((x % 2) == 1):
	    for i in range(((x // 2) - 1)):
	        s = (s + '1')
	    s = ('7' + s)
	    global_list.append(s)
	return global_list