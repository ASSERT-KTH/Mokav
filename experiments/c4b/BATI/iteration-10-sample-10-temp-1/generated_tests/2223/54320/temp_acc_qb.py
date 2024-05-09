def patched_func(*args):
	global_list = []
	
	w = int(args[0])
	x = (w - 1)
	n = 0
	for i in range(1, ((w // 2) + 2)):
	    if (((i % 2) == 0) and ((x % 2) == 0)):
	        global_list.append('YES')
	        n += 1
	        break
	    x -= 1
	    if (x == 0):
	        break
	if (n == 0):
	    global_list.append('NO')
	return global_list