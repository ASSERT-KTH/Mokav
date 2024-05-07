def patched_func(*args):
	global_list = []
	
	(n, a, b, c) = [int(x) for x in args[0].split()]
	dp_table = ([(- 1)] * (n + 1))
	dp_table[0] = 0
	for v in [a, b, c]:
	    for i in range((n + 1)):
	        if ((i >= v) and (dp_table[(i - v)] != (- 1))):
	            dp_table[i] = max(dp_table[i], (dp_table[(i - v)] + 1))
	global_list.append(dp_table[n])
	return global_list