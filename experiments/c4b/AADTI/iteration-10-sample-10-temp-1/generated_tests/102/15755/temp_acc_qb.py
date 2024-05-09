def patched_func(*args):
	global_list = []
	
	a = args[0].split()
	for i in range(3):
	    a[i] = int(a[i])
	sum = ((a[0] + a[1]) + a[2])
	ans = sum
	for i in range(3):
	    if ((2 * (sum - a[i])) < ans):
	        ans = (2 * (sum - a[i]))
	global_list.append(ans)
	return global_list