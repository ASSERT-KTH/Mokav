def func(*args):
	ret_values = []
	
	import sys
	import string
	
	def main():
	    n = int(sys.stdin.readline())
	    ret_values.append(''.join([str(i) for i in range(1, 1000)])[(n - 1)])
	if (__name__ == '__main__'):
	    main()

	return ret_values
