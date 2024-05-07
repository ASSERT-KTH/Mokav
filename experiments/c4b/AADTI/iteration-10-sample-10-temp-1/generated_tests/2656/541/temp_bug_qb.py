def original_func(*args):
	global_list = []
	
	(n, k) = args[0].split()
	k = int(k)
	n_z = 0
	d = 0
	for i in range(len(n)):
	    if (n[((len(n) - i) - 1)] == '0'):
	        n_z += 1
	        if (n_z == k):
	            global_list.append(d)
	            quit()
	    else:
	        d += 1
	        if (i == (len(n) - 1)):
	            global_list.append((len(n) - 1))
	            quit()
	return global_list