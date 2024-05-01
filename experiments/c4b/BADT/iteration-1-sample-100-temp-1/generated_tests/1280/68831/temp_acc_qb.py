def patched_func(*args):
	global_list = []
	
	k = int(args[0])
	a = [int(i) for i in args[1].split()]
	if (k == 0):
	    global_list.append('0')
	else:
	    a.sort(reverse=True)
	    for i in range(12):
	        if (sum(a[0:(i + 1)]) >= k):
	            global_list.append((i + 1))
	            break
	    else:
	        global_list.append('-1')
	return global_list