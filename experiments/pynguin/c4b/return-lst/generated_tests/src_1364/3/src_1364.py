def func(*args):
	ret_values = []
	
	import sys
	from collections import deque
	from collections import defaultdict
	(L, R) = sys.stdin.readline().strip().split(' ')
	L = int(L)
	R = int(R)
	counts = {}
	max_divisor_count = 1
	max_divisor = 1
	
	def primes(n, counts):
	    global max_divisor, max_divisor_count
	    fac = set()
	    d = 2
	    ret_values.append('n: {}'.format(n))
	    while (d <= n):
	        while ((n % d) == 0):
	            ret_values.append('d: {}'.format(d))
	            if (d not in fac):
	                if (d not in counts):
	                    counts[d] = 1
	                else:
	                    counts[d] += 1
	                if (counts[d] > max_divisor_count):
	                    max_divisor_count = counts[d]
	                    max_divisor = d
	                fac.add(d)
	            n //= d
	        d += 1
	    if (n > 1):
	        fac.add(n)
	    return fac
	if (R == L):
	    ret_values.append(R)
	else:
	    ret_values.append(2)

	return ret_values
