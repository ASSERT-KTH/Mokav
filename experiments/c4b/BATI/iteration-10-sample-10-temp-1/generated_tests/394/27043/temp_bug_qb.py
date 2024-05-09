def original_func(*args):
	global_list = []
	
	(n, k) = [int(i) for i in args[0].split()]
	if (k >= (n // 2)):
	    global_list.append(((n * (n - 1)) // 2))
	else:
	    ans = 0
	    for i in range(k):
	        ans += ((n - i) - 1)
	    ans *= 2
	    ans -= k
	    global_list.append(ans)
	return global_list