def patched_func(*args):
	global_list = []
	
	a = args[0]
	b = ['h', 'e', 'l', 'l', 'o']
	c = 0
	d = 0
	for i in a:
	    if (b[c] == i):
	        c = (c + 1)
	        if (c == 5):
	            break
	if (c == 5):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list