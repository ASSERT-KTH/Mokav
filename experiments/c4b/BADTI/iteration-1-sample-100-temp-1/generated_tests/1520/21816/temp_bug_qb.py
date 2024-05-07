def original_func(*args):
	global_list = []
	
	(n, a, b, c) = map(int, args[0].split())
	lengths = {a, b, c}
	dp = ([0] * n)
	for i in range(n):
	    options = [0]
	    for l in lengths:
	        if ((i - l) >= 0):
	            options.append((dp[(i - l)] + 1))
	    dp[i] = max(options)
	global_list.append(dp[(- 1)])
	return global_list