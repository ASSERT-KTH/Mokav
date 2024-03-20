def func(*args):
	
	
	def compatible(a, b):
	    return ((a <= (b + 1)) and ((2 * a) >= (b - 2)))
	a = [int(i) for i in args[0].split()]
	b = [int(i) for i in args[1].split()]
	return(['NO', 'YES'][(compatible(a[0], b[1]) or compatible(a[1], b[0]))])
