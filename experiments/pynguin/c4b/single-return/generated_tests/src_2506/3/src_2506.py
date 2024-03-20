def func(*args):
	
	from math import factorial
	return(factorial(min(map(int, args[0].split(' ')))))
