def func(*args):
	ret_values = []
	
	import math
	
	def main():
	    (a, b) = map(int, args[0].split())
	    return ('YES' if (((a + b) != 0) and ((a == b) or (abs((b - a)) == 1))) else 'NO')
	ret_values.append(main())

	return ret_values
