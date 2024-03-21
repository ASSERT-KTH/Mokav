def func(*args):
	ret_values = []
	
	import sys, threading, os.path
	import collections, heapq, math, bisect
	import string
	from platform import python_version
	import itertools
	sys.setrecursionlimit((10 ** 6))
	threading.stack_size((2 ** 27))
	
	def main():
	    if os.path.exists('input.txt'):
	        input = open('input.txt', 'r')
	    else:
	        input = sys.stdin
	    lis = list(map(int, input.readline().split()))
	    output = ((lis[0] - max((lis[1] + 1), (lis[0] - lis[2]))) + 1)
	    if os.path.exists('output.txt'):
	        open('output.txt', 'w').writelines(str(output))
	    else:
	        sys.stdout.write(str(output))
	if (__name__ == '__main__'):
	    main()

	return ret_values
