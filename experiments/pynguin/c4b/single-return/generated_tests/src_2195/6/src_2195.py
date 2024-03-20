def func(*args):
	
	import sys
	import collections
	sys.setrecursionlimit(30000)
	
	def main():
	    (a, b, c) = [int(i) for i in args[0].split()]
	    a = ((b * c) + (((b + c) - 1) * (a - 1)))
	    return(a)
	if (__name__ == '__main__'):
	    main()
