def original_func(*args):
	global_list = []
	
	import math
	
	def main():
	    (a, b) = map(int, args[0].split())
	    return ('YES' if ((a == b) or (abs((b - a)) == 1)) else 'NO')
	global_list.append(main())
	return global_list