def func(*args):
	
	import sys
	from math import *
	
	def solve():
	    n = int(args[0])
	    (aa, bb) = ((n // 3), (n % 3))
	    if (bb >= 2):
	        aa += 1
	    return((aa // 12), (aa % 12))
	solve()
