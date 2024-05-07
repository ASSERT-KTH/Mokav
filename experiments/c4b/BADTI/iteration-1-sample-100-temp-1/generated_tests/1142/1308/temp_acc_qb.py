def patched_func(*args):
	global_list = []
	
	cont = 0
	(n, a, b) = map(int, args[0].split())
	if ((a == 0) and (b == 0)):
	    global_list.append(1)
	else:
	    for i in range(n):
	        if (((i - 1) <= b) and ((n - i) >= a)):
	            cont += 1
	    global_list.append((cont - 1))
	return global_list