def func(*args):
	ret_values = []
	
	'\nCreated on Fri Jul 21 11:25:33 2017\n\n@author: forgeguest\n'
	ret_values.append(''.join(('.{}'.format(c) for c in [char for char in str(args[0]).lower() if (char not in 'aeiouy')])))

	return ret_values
