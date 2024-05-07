def patched_func(*args):
	global_list = []
	
	k = int(args[0])
	a = list(map(int, args[1].split()))
	a.sort(reverse=True)
	d = 0
	m = 0
	for i in range(12):
	    d += a[i]
	    m += 1
	    if (d >= k):
	        break
	if (k == 0):
	    global_list.append('0')
	elif (d < k):
	    global_list.append('-1')
	else:
	    global_list.append(m)
	return global_list