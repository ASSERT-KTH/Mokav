def patched_func(*args):
	global_list = []
	
	import math
	
	def main():
	    (n, a, b, c) = map(int, args[0].split())
	    n = ((4 - (n % 4)) % 4)
	    if (n == 0):
	        global_list.append(0)
	    elif (n == 1):
	        global_list.append(min(a, (3 * c), (b + c)))
	    elif (n == 2):
	        global_list.append(min((2 * a), b, (2 * c)))
	    elif (n == 3):
	        global_list.append(min((3 * a), c, (a + b)))
	main()
	return global_list