def original_func(*args):
	global_list = []
	
	a = args[0]
	cnt = 0
	ans = 0
	t = a[0]
	for i in range(len(a)):
	    if (a[i] == t):
	        cnt += 1
	    else:
	        ans += 1
	        cnt = 1
	    if (cnt == 5):
	        ans += 1
	        cnt = 0
	    t = a[i]
	global_list.append(((ans + 1) if (cnt != 0) else ans))
	return global_list