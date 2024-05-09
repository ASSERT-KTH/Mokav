def patched_func(*args):
	global_list = []
	
	(a, b, c) = map(int, args[0].split())
	(x, y, z) = map(int, args[1].split())
	a = (a - x)
	b = (b - y)
	c = (c - z)
	have = 0
	need = 0
	for i in (a, b, c):
	    if (i > 0):
	        have += (i // 2)
	    elif (i < 0):
	        need += i
	if (have >= abs(need)):
	    global_list.append('Yes')
	else:
	    global_list.append('No')
	return global_list