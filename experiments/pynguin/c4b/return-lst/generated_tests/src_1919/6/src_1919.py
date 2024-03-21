def func(*args):
	ret_values = []
	
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
	                ret_values.append(s)
	                sys.exit()
	ret_values.append(s)

	return ret_values
