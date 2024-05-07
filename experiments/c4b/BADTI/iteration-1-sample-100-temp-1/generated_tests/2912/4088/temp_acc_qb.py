def patched_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	if (a > b):
	    (a, b) = (b, a)
	ans = 1
	for i in range(2, (a + 1)):
	    ans *= i
	global_list.append(ans)
	return global_list