def patched_func(*args):
	global_list = []
	
	a = [int(i) for i in args[0].split()]
	max = 0
	for i in a:
	    if (max < a.count(i)):
	        max = a.count(i)
	if (((a[0] == a[1]) and (a[2] == a[3])) or ((a[0] == a[2]) and (a[1] == a[3])) or ((a[0] == a[3]) and (a[1] == a[2]))):
	    max += 1
	if (a[0] == a[1] == a[2] == a[3]):
	    global_list.append((max - 2))
	else:
	    global_list.append((max - 1))
	return global_list