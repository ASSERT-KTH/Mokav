def patched_func(*args):
	global_list = []
	
	A = [int(i) for i in args[0].split()]
	z = sum(A)
	d = z
	for i in range(len(A)):
	    zz = A.count(A[i])
	    if (zz >= 2):
	        if (zz >= 3):
	            zz = 3
	        h = (z - (zz * A[i]))
	        if (h < d):
	            d = h
	global_list.append(d)
	return global_list