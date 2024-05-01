def patched_func(*args):
	global_list = []
	
	x = args[0]
	a = ['h', 'e', 'l', 'l', 'o']
	for i in x:
	    if (len(a) == 0):
	        break
	    if (i == a[0]):
	        del a[0]
	if (len(a) == 0):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list