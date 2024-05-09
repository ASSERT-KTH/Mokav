def original_func(*args):
	global_list = []
	
	(t, s, x) = map(int, args[0].split())
	(global_list.append('NO') if ((((((x - t) % s) == 0) or ((((x - t) - 1) % s) == 0)) and (x >= (t + s))) or (x == t)) else global_list.append('YES'))
	return global_list