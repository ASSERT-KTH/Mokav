def patched_func(*args):
	global_list = []
	
	k = int(args[0])
	a = sorted(map(int, args[1].split()))
	a.reverse()
	s = r = 0
	if (k > 0):
	    for i in a:
	        s += i
	        r += 1
	        if (s >= k):
	            global_list.append(r)
	            break
	    if (s < k):
	        global_list.append((- 1))
	else:
	    global_list.append(0)
	return global_list