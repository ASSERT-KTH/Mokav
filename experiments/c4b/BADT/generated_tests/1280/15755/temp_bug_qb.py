def original_func(*args):
	global_list = []
	
	k = int(args[0])
	a = args[1].split()
	ans = 0
	for i in range(len(a)):
	    a[i] = int(a[i])
	for i in reversed(sorted(a)):
	    if (k < 1):
	        global_list.append(ans)
	        break
	    k -= i
	    ans += 1
	else:
	    global_list.append((- 1))
	return global_list