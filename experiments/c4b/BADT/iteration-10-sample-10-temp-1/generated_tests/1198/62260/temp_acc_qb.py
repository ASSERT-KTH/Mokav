def patched_func(*args):
	global_list = []
	
	a = str(args[0])
	b = list(a)
	v = 0
	s = ['Q', 'H', '9']
	for c in b:
	    for i in s:
	        if (c == i):
	            v += 1
	            global_list.append('YES')
	            break
	    if (v != 0):
	        break
	if (v == 0):
	    global_list.append('NO')
	return global_list