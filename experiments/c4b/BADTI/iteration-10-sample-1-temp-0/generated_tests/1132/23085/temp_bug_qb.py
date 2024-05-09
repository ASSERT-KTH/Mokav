def original_func(*args):
	global_list = []
	
	ll = []
	for x in range(3, 1001):
	    l = list(str(x))
	    if (len(l) == (l.count('4') + l.count('7'))):
	        ll.append(x)
	tmp = int(args[0])
	t = 0
	for i in ll:
	    if ((tmp % i) == 0):
	        global_list.append('YES')
	        t = 1
	if (t == 0):
	    global_list.append('NO')
	return global_list