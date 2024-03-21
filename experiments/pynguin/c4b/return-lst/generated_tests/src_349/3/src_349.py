def func(*args):
	ret_values = []
	
	import math
	(N, M) = map(int, args[0].split())
	
	def check(n):
	    if (n == 1):
	        return False
	    if (n == 2):
	        return True
	    for i in range(2, (math.ceil(math.sqrt(n)) + 1)):
	        if ((n % i) == 0):
	            return False
	    return True
	if (not check(M)):
	    ret_values.append('NO')
	    exit()
	ans = []
	for i in range((N + 1), (M + 1)):
	    if check(i):
	        ans.append(i)
	if (len(ans) != 1):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
