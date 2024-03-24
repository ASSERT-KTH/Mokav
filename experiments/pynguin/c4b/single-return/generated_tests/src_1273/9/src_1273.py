def func(*args):
	
	'\nCreated on Tue Apr 11 08:09:05 2017\n\n@author: lawrenceylong\n'
	(a, b, c) = map(int, args[0].split())
	return(min([(2 * (a + b)), ((a + b) + c), (2 * (b + c)), (2 * (a + c))]))
