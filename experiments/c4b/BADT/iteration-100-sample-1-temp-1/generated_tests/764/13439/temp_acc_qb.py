def patched_func(*args):
	global_list = []
	
	a = list(map(int, args[0].split()))
	a.sort()
	afstand = (abs((a[0] - a[1])) + abs((a[2] - a[1])))
	global_list.append(afstand)
	return global_list