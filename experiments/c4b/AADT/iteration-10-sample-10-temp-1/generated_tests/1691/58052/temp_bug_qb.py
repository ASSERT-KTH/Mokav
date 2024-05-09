def original_func(*args):
	global_list = []
	
	import sys
	a = [int(i) for i in args[0].split()]
	a.sort()
	t = (a.count(a[0]) == len(a))
	count = ((sum(a) * 2) - 6)
	while (a[0] > 1):
	    a = [(i - 1) for i in a]
	    count += ((sum(a) * 2) - 6)
	if t:
	    global_list.append((count + 1))
	else:
	    global_list.append(count)
	return global_list