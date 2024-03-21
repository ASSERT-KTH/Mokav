def func(*args):
	ret_values = []
	
	from math import sqrt
	
	def is_simple(a):
	    for i in range(2, (int(sqrt(a)) + 1)):
	        if ((a % i) == 0):
	            return False
	    else:
	        return True
	(n, k) = map(int, args[0].split())
	q = []
	w = 0
	for i in range(2, n):
	    if is_simple(i):
	        q.append(i)
	for i in range((len(q) - 1)):
	    if (is_simple(((q[i] + q[(i + 1)]) + 1)) and (((q[i] + q[(i + 1)]) + 1) <= n)):
	        w += 1
	if (w < k):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
