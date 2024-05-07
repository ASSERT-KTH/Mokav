def patched_func(*args):
	global_list = []
	
	K = int(args[0])
	A = list(map(int, args[1].split()))
	A.sort(reverse=True)
	ans = 0
	now = 0
	for a in A:
	    if (now >= K):
	        break
	    now += a
	    ans += 1
	if (now >= K):
	    global_list.append(ans)
	else:
	    global_list.append((- 1))
	return global_list