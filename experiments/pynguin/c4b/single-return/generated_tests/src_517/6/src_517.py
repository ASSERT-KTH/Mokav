def func(*args):
	
	nabcStr = args[0]
	n = int(nabcStr.split()[0])
	a = int(nabcStr.split()[1])
	b = int(nabcStr.split()[2])
	c = int(nabcStr.split()[3])
	dp = ([0] * (n + 1))
	if (a <= n):
	    dp[a] = 1
	if (b <= n):
	    dp[b] = 1
	if (c <= n):
	    dp[c] = 1
	for i in range((n + 1)):
	    backA = (- 1)
	    backB = (- 1)
	    backC = (- 1)
	    if (i >= a):
	        if (dp[(i - a)] != 0):
	            backA = dp[(i - a)]
	    if (i >= b):
	        if (dp[(i - b)] != 0):
	            backB = dp[(i - b)]
	    if (i >= c):
	        if (dp[(i - c)] != 0):
	            backC = dp[(i - c)]
	    dp[i] = max((backA + 1), (backB + 1), (backC + 1), dp[i])
	return(dp[n])
