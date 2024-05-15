def original_func(*args):
	global_list = []
	
	(n, a, b, c) = map(int, args[0].split())
	dp = ([0] + ([(- 1000000000.0)] * 5000))
	for i in range(1, (n + 1)):
	    global_list.append(i)
	    dp[i] = (max(dp[(i - a)], dp[(i - b)], dp[(i - c)]) + 1)
	global_list.append(dp[n])
	return global_list