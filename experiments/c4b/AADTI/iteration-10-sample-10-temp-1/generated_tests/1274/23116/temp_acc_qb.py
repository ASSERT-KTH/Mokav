def patched_func(*args):
	global_list = []
	
	k = int(args[0])
	l = int(args[1])
	m = int(args[2])
	n = int(args[3])
	d = int(args[4])
	li = []
	for i in range((k - 1), d, k):
	    li.append(i)
	for i in range((l - 1), d, l):
	    li.append(i)
	for i in range((m - 1), d, m):
	    li.append(i)
	for i in range((n - 1), d, n):
	    li.append(i)
	li = set(li)
	global_list.append(len(li))
	return global_list