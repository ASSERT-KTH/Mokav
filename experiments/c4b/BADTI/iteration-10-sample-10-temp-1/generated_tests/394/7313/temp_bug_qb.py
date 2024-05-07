def original_func(*args):
	global_list = []
	
	(n, k) = args[0].split()
	n = int(n)
	k = int(k)
	sum = 0
	if (n == 1):
	    global_list.append(sum)
	elif (n == 2):
	    sum = 1
	    global_list.append(sum)
	else:
	    for i in range(k):
	        sum += ((2 * n) - 3)
	        n -= 2
	    global_list.append(sum)
	return global_list