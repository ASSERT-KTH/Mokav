def func(*args):
	
	(l1, r1, l2, r2, k) = [int(x) for x in args[0].split()]
	return(max(0, ((min(r2, r1) - max(l2, l1)) if ((k >= max(l2, l1)) and (k <= min(r2, r1))) else ((min(r2, r1) - max(l2, l1)) + 1))))
