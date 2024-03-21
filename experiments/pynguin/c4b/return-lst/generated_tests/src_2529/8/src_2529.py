def func(*args):
	ret_values = []
	
	import math
	n = int(args[0])
	names = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	
	def func1(n):
	    i = 1
	    j = 0
	    while (((i * 10) - 4) <= n):
	        j = ((i * 10) - 4)
	        i = (i * 2)
	    return (i, j)
	
	def func2(n):
	    if (n <= 5):
	        return (n - 1)
	    else:
	        a = func1(n)
	        b = math.floor(((n - a[1]) / a[0]))
	        return b
	name = func2(n)
	ret_values.append(names[name])

	return ret_values
