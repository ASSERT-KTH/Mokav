def patched_func(*args):
	global_list = []
	
	k = int(args[0])
	a = list(map(int, args[1].split()))
	a.sort(reverse=True)
	c = 0
	f = 0
	for i in range(12):
	    if (c < k):
	        c += a[i]
	        f += 1
	    if (c >= k):
	        break
	if (c >= k):
	    global_list.append(f)
	else:
	    global_list.append((- 1))
	return global_list