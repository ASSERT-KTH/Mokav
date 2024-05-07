def patched_func(*args):
	global_list = []
	
	a = args[0]
	b = 'hello'
	p = 0
	for i in range(len(a)):
	    if (a[i] == b[p]):
	        p += 1
	    if (p == 5):
	        global_list.append('YES')
	        break
	if (p != 5):
	    global_list.append('NO')
	return global_list