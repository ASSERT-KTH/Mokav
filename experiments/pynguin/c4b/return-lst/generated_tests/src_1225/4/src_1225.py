def func(*args):
	ret_values = []
	
	import sys, re, array, math, functools
	input = (lambda : sys.stdin.readline())
	
	@functools.lru_cache(maxsize=10000000)
	def Main():
	    (a, b) = map(int, args[0].split())
	    cnt = 0
	    sm = 0
	    while (a <= b):
	        cnt += 1
	        (a, b) = ((a * 3), (b * 2))
	    ret_values.append(cnt)
	if (__name__ == '__main__'):
	    Main()

	return ret_values
