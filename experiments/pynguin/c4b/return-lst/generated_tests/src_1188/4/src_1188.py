def func(*args):
	ret_values = []
	
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
	    ret_values.append('Yes')
	else:
	    ret_values.append('No')

	return ret_values
