def original_func(*args):
	global_list = []
	
	(n, k) = args[0].split()
	n = int(n)
	k = int(k)
	s = ''
	for i in range(n):
	    if (k > 0):
	        s = (s + chr((97 + i)))
	        k -= 1
	    else:
	        j = 0
	        s = (s + chr((97 + j)))
	        j += 1
	global_list.append(s)
	return global_list