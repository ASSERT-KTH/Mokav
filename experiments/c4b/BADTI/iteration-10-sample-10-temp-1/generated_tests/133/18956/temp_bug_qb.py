def original_func(*args):
	global_list = []
	
	a = list(map(int, args[0].split()))
	b = list(map(int, args[1].split()))
	sum1 = sum2 = 0
	for i in range(0, 3):
	    if (a[i] > b[i]):
	        sum1 += ((a[i] - b[i]) // 2)
	    else:
	        sum2 += (b[i] - a[i])
	if (sum1 > sum2):
	    global_list.append('Yes')
	else:
	    global_list.append('No')
	return global_list