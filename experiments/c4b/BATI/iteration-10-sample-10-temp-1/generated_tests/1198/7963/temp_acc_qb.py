def patched_func(*args):
	global_list = []
	
	s = list(args[0])
	L = ['Q', 'H', '9']
	q = 0
	for i in s:
	    if (i in L):
	        global_list.append('YES')
	        q = 1
	        break
	if (q == 0):
	    global_list.append('NO')
	return global_list