def original_func(*args):
	global_list = []
	
	k = int(args[0])
	b = args[1].split()
	a = []
	for i in b:
	    a.append(int(i))
	sum = 0
	for i in a:
	    sum += i
	if (k > sum):
	    global_list.append('-1')
	else:
	    count = 0
	    while (k > 0):
	        k -= max(a)
	        count += 1
	    global_list.append(count)
	return global_list