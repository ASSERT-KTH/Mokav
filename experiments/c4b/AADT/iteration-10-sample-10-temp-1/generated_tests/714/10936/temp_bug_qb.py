def original_func(*args):
	global_list = []
	
	import sys
	arr = list(map(int, args[0].split()))
	l1 = arr[0]
	r1 = arr[1]
	l2 = arr[2]
	r2 = arr[3]
	k = arr[4]
	cnt = 0
	a = max(l1, l2)
	b = min(r1, r2)
	if ((a <= k) and (k <= b)):
	    global_list.append((b - a))
	else:
	    global_list.append(((b - a) + 1))
	return global_list