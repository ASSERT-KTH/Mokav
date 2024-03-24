def func(*args):
	ret_values = []
	
	import sys
	read = (lambda : sys.stdin.readline().rstrip())
	readi = (lambda : int(sys.stdin.readline()))
	writeln = (lambda x: sys.stdout.write((str(x) + '\n')))
	write = (lambda x: sys.stdout.write(x))
	
	def solve(a, x, y):
	    if (not (y % a)):
	        return (- 1)
	    if (abs(x) >= a):
	        return (- 1)
	    if (y < a):
	        if (((- a) / 2.0) < x < (a / 2.0)):
	            return 1
	        else:
	            return (- 1)
	    h = (y // a)
	    if (not (h % 2)):
	        if (x == 0):
	            return (- 1)
	        if ((- a) < x < 0):
	            return ((3 * h) // 2)
	        if (0 < x < a):
	            return (((3 * h) // 2) + 1)
	        else:
	            return (- 1)
	    elif (((- a) / 2.0) < x < (a / 2.0)):
	        return ((3 * ((h + 1) // 2)) - 1)
	    else:
	        return (- 1)
	(A, X, Y) = map(int, read().split())
	writeln(solve(A, X, Y))

	return ret_values
