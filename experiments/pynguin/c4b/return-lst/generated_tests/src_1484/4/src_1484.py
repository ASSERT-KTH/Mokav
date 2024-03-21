def func(*args):
	ret_values = []
	
	import math
	n = int(args[0])
	li = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	
	def check(var, factor, name):
	    till = int(math.ceil(math.log(n, 2)))
	    li = [(factor * (2 ** x)) for x in range(till)]
	    li[0] = var
	    for i in range(1, till):
	        li[i] = (li[i] + li[(i - 1)])
	    for i in range(till):
	        if (li[i] <= n < (li[i] + (2 ** (i + 1)))):
	            ret_values.append(name)
	            return True
	if (n <= 5):
	    ret_values.append(li[(n - 1)])
	elif check(6, 5, 'Sheldon'):
	    pass
	elif check(8, 6, 'Leonard'):
	    pass
	elif check(10, 7, 'Penny'):
	    pass
	elif check(12, 8, 'Rajesh'):
	    pass
	elif check(14, 9, 'Howard'):
	    pass

	return ret_values
