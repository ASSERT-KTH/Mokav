def patched_func(*args):
	global_list = []
	
	haz = list(map(int, args[0].split()))
	want = list(map(int, args[1].split()))
	stash = 0
	for (x, y) in zip(haz, want):
	    if (x > y):
	        stash += ((x - y) // 2)
	need = 0
	for (x, y) in zip(haz, want):
	    if (x < y):
	        need += (y - x)
	if (stash >= need):
	    global_list.append('Yes')
	else:
	    global_list.append('No')
	return global_list