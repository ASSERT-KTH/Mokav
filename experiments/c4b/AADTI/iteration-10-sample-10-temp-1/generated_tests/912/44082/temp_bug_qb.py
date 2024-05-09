def original_func(*args):
	global_list = []
	
	import sys
	(n, k) = args[0].strip().split()
	(n, k) = (int(n), int(k))
	k = (240 - k)
	i = 0
	for i in range(1, (n + 1)):
	    k = (k - (i * 5))
	    if (k < 0):
	        global_list.append((i - 1))
	        break
	if (i == n):
	    global_list.append(n)
	return global_list