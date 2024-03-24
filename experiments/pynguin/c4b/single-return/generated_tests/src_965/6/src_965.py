def func(*args):
	
	import math
	
	def main():
	    (a, b) = map(int, args[0].split())
	    return ('YES' if (((a + b) != 0) and ((a == b) or (abs((b - a)) == 1))) else 'NO')
	return(main())
