def patched_func(*args):
	global_list = []
	
	k = int(args[0])
	a = list(map(int, args[1].split()))
	a.sort()
	count = 0
	pos = (len(a) - 1)
	while ((k > 0) and (pos >= 0)):
	    count = (count + 1)
	    k = (k - a[pos])
	    pos = (pos - 1)
	if ((count < 13) and (k <= 0)):
	    global_list.append(count)
	else:
	    global_list.append((- 1))
	return global_list