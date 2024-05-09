def original_func(*args):
	global_list = []
	
	from math import factorial
	
	def calculate_combinations(n, r):
	    return ((factorial(n) // factorial(r)) // factorial((n - r)))
	(n, m, t) = args[0].split()
	n = int(n)
	m = int(m)
	t = int(t)
	if ((n + m) == t):
	    total = 1
	else:
	    countB = n
	    total = 0
	    while (countB >= 4):
	        if ((t - countB) >= 1):
	            total += (calculate_combinations(n, countB) * calculate_combinations(m, (t - countB)))
	        countB -= 1
	        if ((t - countB) == m):
	            break
	global_list.append(total)
	return global_list