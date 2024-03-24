def func(*args):
	
	
	def drive(n, a):
	    if (a == n):
	        return 1
	    elif ((a % 2) != 0):
	        time = ((a // 2) + 1)
	    elif ((a % 2) == 0):
	        time = (((n - a) // 2) + 1)
	    return time
	(x, y) = map(int, args[0].split())
	return(drive(x, y))
