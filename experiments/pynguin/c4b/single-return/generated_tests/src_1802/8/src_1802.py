def func(*args):
	
	import sys
	import string
	
	def main():
	    n = int(sys.stdin.readline())
	    return(''.join([str(i) for i in range(1, 1000)])[(n - 1)])
	if (__name__ == '__main__'):
	    main()
