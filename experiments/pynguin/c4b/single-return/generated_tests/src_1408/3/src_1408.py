def func(*args):
	
	(l1, r1, l2, r2, k1) = map(int, args[0].split())
	k = 0
	if ((l1 <= l2) and (r2 <= r1)):
	    k = (abs((r2 - l2)) + 1)
	    if ((k1 >= l2) and (k1 <= r2)):
	        k = (k - 1)
	if ((l2 <= l1) and (r2 >= r1)):
	    k = (abs((r1 - l1)) + 1)
	    if ((k1 >= l1) and (k1 <= r1)):
	        k = (k - 1)
	if ((l2 <= l1) and (r1 >= r2) and (r2 >= l1)):
	    k = (abs((l1 - r2)) + 1)
	    if ((k1 >= l1) and (k1 <= r2)):
	        k = (k - 1)
	if ((l1 <= l2) and (r1 <= r2) and (r1 >= l2)):
	    k = (abs((l2 - r1)) + 1)
	    if ((k1 >= l2) and (k1 <= r1)):
	        k = (k - 1)
	return(k)
