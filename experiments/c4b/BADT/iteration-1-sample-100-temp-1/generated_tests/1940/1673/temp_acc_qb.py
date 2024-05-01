def patched_func(*args):
	global_list = []
	
	n = int(args[0].strip())
	otvet = 0
	for i in range(6, (n + 1)):
	    l = []
	    for j in range(2, ((i // 2) + 1)):
	        if (i == 1):
	            break
	        else:
	            while ((i % j) == 0):
	                i = (i // j)
	                l.append(j)
	    if (len(set(l)) == 2):
	        otvet += 1
	global_list.append(otvet)
	return global_list