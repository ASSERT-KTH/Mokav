def func(*args):
	ret_values = []
	
	(n, a, b, c) = map(int, args[0].split())
	lengths = {a, b, c}
	dp = ([(- 1)] * (n + 1))
	dp[0] = 0
	for i in range(1, (n + 1)):
	    options = [(- 1)]
	    for l in lengths:
	        if (((i - l) >= 0) and (dp[(i - l)] >= 0)):
	            options.append((dp[(i - l)] + 1))
	    dp[i] = max(options)
	ret_values.append(dp[(- 1)])

	return ret_values
