def original_func(*args):
	global_list = []
	
	import math
	from collections import Counter
	from original_functools import reduce
	s = args[0]
	c = Counter(s).most_common()
	s1 = [v for (k, v) in c]
	c1 = Counter(s1).most_common()
	x = [k for (k, v) in c1]
	gcd = reduce(math.gcd, x)
	if ((gcd < sorted(x)[0]) and (gcd != 1)):
	    gcd = 1
	n = 0
	for (k, v) in c1:
	    n += ((k // gcd) * v)
	global_list.append(n)
	return global_list