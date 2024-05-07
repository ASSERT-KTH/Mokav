def original_func(*args):
	global_list = []
	
	A = [int(i) for i in args[0].split()]
	z = sum(A)
	d = z
	for i in range(len(A)):
	    if (A.count(A[i]) >= 2):
	        h = (z - (A.count(A[i]) * A[i]))
	        if (h < d):
	            d = h
	global_list.append(d)
	return global_list