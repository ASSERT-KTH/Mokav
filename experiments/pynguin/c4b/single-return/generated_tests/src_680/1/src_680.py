def func(*args):
	
	[n, a, b, c] = [int(x) for x in args[0].split()]
	dp = [(- 1) for x in range((n + 1))]
	dp[0] = 0
	for i in range((n + 1)):
	    if ((i >= a) and (dp[(i - a)] > (- 1))):
	        dp[i] = max(dp[i], (dp[(i - a)] + 1))
	    if ((i >= b) and (dp[(i - b)] > (- 1))):
	        dp[i] = max(dp[i], (dp[(i - b)] + 1))
	    if ((i >= c) and (dp[(i - c)] > (- 1))):
	        dp[i] = max(dp[i], (dp[(i - c)] + 1))
	return(dp[n])
