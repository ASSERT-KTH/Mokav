def patched_func(*args):
	global_list = []
	
	k = int(args[0])
	l = int(args[1])
	m = int(args[2])
	n = int(args[3])
	d = int(args[4])
	contador = (- 1)
	if ((k <= d) and (l <= d) and (m <= d) and (n <= d)):
	    for i in range((d + 1)):
	        if (((i % k) == 0) or ((i % l) == 0) or ((i % m) == 0) or ((i % n) == 0)):
	            contador += 1
	    global_list.append(contador)
	else:
	    global_list.append('0')
	return global_list