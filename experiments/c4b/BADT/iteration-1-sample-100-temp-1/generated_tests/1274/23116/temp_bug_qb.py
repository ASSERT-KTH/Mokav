def original_func(*args):
	global_list = []
	
	k = int(args[0])
	l = int(args[1])
	m = int(args[2])
	n = int(args[3])
	d = int(args[4])
	li = []
	for i in range(0, d, k):
	    li.append(i)
	for i in range(0, d, l):
	    li.append(i)
	for i in range(0, d, m):
	    li.append(i)
	for i in range(0, d, n):
	    li.append(i)
	li = set(li)
	if ((k > d) or (l > d) or (m > d) or (n > d)):
	    global_list.append('0')
	else:
	    global_list.append(len(li))
	return global_list