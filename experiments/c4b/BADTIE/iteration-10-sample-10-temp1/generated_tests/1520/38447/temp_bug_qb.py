def original_func(*args):
	global_list = []
	
	(n, a, b, c) = list(map(int, args[0].split()))
	f = ([0] + ([50000] * 5000))
	for i in range(1, (n + 1)):
	    f[i] = (min(f[(i - a)], f[(i - b)], f[(i - c)]) + 1)
	global_list.append(f[n])
	return global_list