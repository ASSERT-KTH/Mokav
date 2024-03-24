def func(*args):
	ret_values = []
	
	import sys
	sys.setrecursionlimit(399603090)
	nmbrs = args[0]
	numbers = nmbrs.split(' ')
	var1 = int(numbers[0])
	var2 = int(numbers[1])
	alist = [0]
	
	def factorial(x):
	    if (x == 1):
	        return 1
	    else:
	        return (x * factorial((x - 1)))
	if (var2 >= var1):
	    ret_values.append(factorial(var1))
	if (var1 > var2):
	    ret_values.append(factorial(var2))

	return ret_values
