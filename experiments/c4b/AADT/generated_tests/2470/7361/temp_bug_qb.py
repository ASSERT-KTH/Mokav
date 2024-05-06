def original_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split())
	ans = True
	for i in range((n + 1), m):
	    if (((2 ** i) % i) == 2):
	        ans = False
	global_list.append(['NO', 'YES'][ans])
	return global_list