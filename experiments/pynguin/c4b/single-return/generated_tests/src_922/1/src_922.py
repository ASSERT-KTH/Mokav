def func(*args):
	
	import sys
	
	def prime(n):
	    for i in range(2, n):
	        if ((i * i) > n):
	            break
	        if (divmod(n, i)[1] == 0):
	            return False
	    if (n > 1):
	        return True
	    else:
	        return False
	
	def solve(n):
	    ans = 0
	    cnt = [0 for i in range((n + 1))]
	    for i in range(2, (n + 1)):
	        if prime(i):
	            for j in range(i, (n + 1), i):
	                cnt[j] += 1
	    for i in range((n + 1)):
	        if (cnt[i] == 2):
	            ans += 1
	    return ans
	n = int(args[0])
	return(solve(n))
