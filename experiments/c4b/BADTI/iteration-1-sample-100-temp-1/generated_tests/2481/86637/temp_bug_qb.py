def original_func(*args):
	global_list = []
	
	import math
	n = int(args[0])
	names = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	
	def original_func1(n):
	    i = 1
	    j = 0
	    while (((i * 10) - 4) <= n):
	        j = ((i * 10) - 4)
	        i = (i * 2)
	    return (i, j)
	
	def original_func2(n):
	    a = original_func1(n)
	    b = math.floor(((n - a[1]) / a[0]))
	    return b
	name = original_func2(n)
	global_list.append(names[name])
	return global_list