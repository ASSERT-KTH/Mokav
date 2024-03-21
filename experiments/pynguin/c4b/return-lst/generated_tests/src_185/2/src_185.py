def func(*args):
	ret_values = []
	
	(n, a, b, c) = map(int, args[0].split())
	dp = ([0] + ([(- 1000000000.0)] * 5000))
	for i in range(1, (n + 1)):
	    dp[i] = (max(dp[(i - a)], dp[(i - b)], dp[(i - c)]) + 1)
	ret_values.append(dp[n])

	return ret_values
