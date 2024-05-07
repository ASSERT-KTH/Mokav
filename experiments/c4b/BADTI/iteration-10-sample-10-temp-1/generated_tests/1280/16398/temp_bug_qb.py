def original_func(*args):
	global_list = []
	
	k = int(args[0])
	a = args[1]
	b = list(map(int, a.split()))
	b.sort()
	sum = 0
	if (k == 0):
	    global_list.append(0)
	else:
	    for i in range(12):
	        sum = (sum + b[((12 - i) - 1)])
	        if (sum >= k):
	            global_list.append((i + 1))
	            break
	        if ((sum < k) and (i == 12)):
	            global_list.append((- 1))
	return global_list