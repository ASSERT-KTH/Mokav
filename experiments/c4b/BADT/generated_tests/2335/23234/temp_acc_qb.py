def patched_func(*args):
	global_list = []
	
	s = list(args[0])
	h = list('hello')
	n = []
	j = 0
	for i in s:
	    if (i == h[j]):
	        n.append(i)
	        j += 1
	    if (j == 5):
	        break
	if (n == h):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list