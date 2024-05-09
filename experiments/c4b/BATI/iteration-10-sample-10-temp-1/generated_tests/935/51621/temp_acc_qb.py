def patched_func(*args):
	global_list = []
	
	n = args[0]
	N = int(n, 10)
	m = 1
	while (m > 0):
	    x = (int((m * N)) + 1)
	    i = 2
	    bool = False
	    while ((i * i) <= x):
	        if ((x % i) == 0):
	            global_list.append(m)
	            bool = True
	            break
	        i += 1
	    if bool:
	        break
	    m += 1
	return global_list