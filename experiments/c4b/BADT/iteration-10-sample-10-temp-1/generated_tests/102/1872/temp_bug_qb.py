def original_func(*args):
	global_list = []
	
	(x, y, z) = list(map(int, args[0].split()))
	ans1 = ((2 * x) + (2 * y))
	ans2 = ((x + z) + y)
	ans3 = (((y + z) + y) + x)
	ans4 = (((y + z) + z) + y)
	global_list.append(min(ans1, ans2, ans3, ans4))
	return global_list