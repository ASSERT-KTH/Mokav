def func(*args):
	ret_values = []
	
	(n, a, b, c) = [int(i) for i in args[0].split()]
	p = [a, b, c]
	p.sort()
	dp = ((n + 1) * [(- 1)])
	dp[0] = 0
	dp[p[0]] = 1
	for i in range((p[0] + 1), (n + 1)):
	    k = []
	    z = dp[i]
	    for j in range(3):
	        if (((i - p[j]) >= 0) and (dp[(i - p[j])] != (- 1))):
	            k.append((dp[(i - p[j])] + 1))
	    if (len(k) == 0):
	        dp[i] = (- 1)
	    else:
	        dp[i] = max(k)
	ret_values.append(dp[(- 1)])

	return ret_values
