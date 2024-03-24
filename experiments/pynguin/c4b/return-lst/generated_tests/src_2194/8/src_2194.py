def func(*args):
	ret_values = []
	
	import sys
	from math import *
	
	def solve():
	    n = int(args[0])
	    (aa, bb) = ((n // 3), (n % 3))
	    if (bb >= 2):
	        aa += 1
	    ret_values.append((aa // 12), (aa % 12))
	solve()

	return ret_values
