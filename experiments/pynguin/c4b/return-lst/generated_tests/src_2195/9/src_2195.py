def func(*args):
	ret_values = []
	
	import sys
	import collections
	sys.setrecursionlimit(30000)
	
	def main():
	    (a, b, c) = [int(i) for i in args[0].split()]
	    a = ((b * c) + (((b + c) - 1) * (a - 1)))
	    ret_values.append(a)
	if (__name__ == '__main__'):
	    main()

	return ret_values
