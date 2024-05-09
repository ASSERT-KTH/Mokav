def patched_func(*args):
	global_list = []
	
	import sys
	(n, k) = args[0].split()
	n = int(n)
	k = int(k)
	s = ''
	x = k
	for i in range(n):
	    if (k > 0):
	        s = (s + chr((97 + i)))
	        k -= 1
	    else:
	        for j in range(x):
	            s = (s + chr((97 + j)))
	            j += 1
	            if (len(s) == n):
	                global_list.append(s)
	                sys.exit()
	global_list.append(s)
	return global_list