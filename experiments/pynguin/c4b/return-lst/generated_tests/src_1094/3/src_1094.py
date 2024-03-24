def func(*args):
	ret_values = []
	
	import math
	
	def main():
	    (n, a, b, c) = map(int, args[0].split())
	    n = ((4 - (n % 4)) % 4)
	    if (n == 0):
	        ret_values.append(0)
	    elif (n == 1):
	        ret_values.append(min(a, (3 * c), (b + c)))
	    elif (n == 2):
	        ret_values.append(min((2 * a), b, (2 * c)))
	    elif (n == 3):
	        ret_values.append(min((3 * a), c, (a + b)))
	main()

	return ret_values
