def func(*args):
	ret_values = []
	
	'\nCreated on Wed Mar 22 17:45:02 2017\n\n@author: lawrenceylong\n'
	(a, b, c) = map(list(args[0]).count, ['H', 'Q', '9'])
	(ret_values.append('YES') if ((a > 0) or (b > 0) or (c > 0)) else ret_values.append('NO'))

	return ret_values
