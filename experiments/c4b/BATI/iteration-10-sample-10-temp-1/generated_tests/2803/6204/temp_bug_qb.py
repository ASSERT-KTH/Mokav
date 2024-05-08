def original_func(*args):
	global_list = []
	
	(n, k) = map(int, args[0].split())
	ans = 0
	for i in range(1, (round((n ** 0.5)) + 2)):
	    if (((n % i) == 0) and ((((k * (k - 1)) // 2) * i) < n) and ((n - (((k * (k - 1)) // 2) * i)) > 0) and ((n - (((k * (k - 1)) // 2) * i)) > ((k - 1) * i))):
	        ans = i
	if (((k * (k + 1)) // 2) > n):
	    global_list.append((- 1))
	else:
	    global_list.append(' '.join(([str((ans * i)) for i in range(1, k)] + [str((n - (((k * (k - 1)) // 2) * ans)))])))
	return global_list