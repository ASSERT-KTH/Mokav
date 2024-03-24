def func(*args):
	
	import math
	
	def main():
	    (a, b, c) = map(int, args[0].split())
	    if (a < b):
	        if (c <= 0):
	            return 'NO'
	        elif ((abs((b - a)) % c) == 0):
	            return 'YES'
	        else:
	            return 'NO'
	    else:
	        if (a == b):
	            return 'YES'
	        if (c >= 0):
	            return 'NO'
	        elif ((abs((b - a)) % c) == 0):
	            return 'YES'
	        else:
	            return 'NO'
	return(main())
