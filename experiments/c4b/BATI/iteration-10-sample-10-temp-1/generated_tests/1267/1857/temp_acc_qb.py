def patched_func(*args):
	global_list = []
	
	args[0]
	inp = args[1]
	z = [(True if ((i == '4') or (i == '7')) else False) for i in inp]
	ans = list(map(int, inp))
	length = int((len(ans) / 2))
	if (all(z) and (sum(ans[0:length]) == sum(ans[length:]))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list