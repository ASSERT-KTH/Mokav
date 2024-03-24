def func(*args):
	ret_values = []
	
	from math import sqrt
	(n, k) = map(int, args[0].split())
	K = ((k * (k + 1)) // 2)
	if (n < K):
	    ret_values.append((- 1))
	else:
	    N = (n // K)
	    ret = (- 1)
	    for i in range(1, (min(N, int(sqrt(n))) + 1)):
	        if ((n % i) == 0):
	            if (i > ret):
	                ret = i
	            ni = (n // i)
	            if ((i < ni) and (ni <= N)):
	                if (ni > ret):
	                    ret = ni
	                    break
	    ans = [(ret * i) for i in range(1, k)]
	    ans.append((n - sum(ans)))
	    ret_values.append(' '.join(map(str, ans)))

	return ret_values
