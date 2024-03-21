def func(*args):
	ret_values = []
	
	import sys
	
	def nod(a, b):
	    if (b == 0):
	        return a
	    return nod(b, (a % b))
	
	def nok(a, b):
	    return int(((a * b) / nod(a, b)))
	(n, m, z) = map(int, sys.stdin.readline().split())
	ret_values.append((z // nok(m, n)))

	return ret_values
