def func(*args):
	
	import sys
	
	def nod(a, b):
	    if (b == 0):
	        return a
	    return nod(b, (a % b))
	
	def nok(a, b):
	    return int(((a * b) / nod(a, b)))
	(n, m, z) = map(int, sys.stdin.readline().split())
	return((z // nok(m, n)))
