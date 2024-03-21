def func(*args):
	ret_values = []
	
	'\nCreated on Sun Apr  2 07:42:38 2017\n\n@author: lawrenceylong\n'
	(a, b) = map(list(args[0]).count, ['4', '7'])
	if (((a + b) == 4) or ((a + b) == 7)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
