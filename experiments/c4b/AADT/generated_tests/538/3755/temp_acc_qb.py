def patched_func(*args):
	global_list = []
	
	lst = list(map(int, args[0].split()))
	data = ([0] * 101)
	s = 0
	for i in lst:
	    data[i] += 1
	    s += i
	max_change = 0
	for i in range(101):
	    if (data[i] > 2):
	        max_change = max(max_change, (i * 3))
	    elif (data[i] > 1):
	        max_change = max(max_change, (i * 2))
	global_list.append((s - max_change))
	return global_list