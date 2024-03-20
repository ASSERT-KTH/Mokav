def func(*args):
	
	'\nCreated on Fri Jul 21 11:25:33 2017\n\n@author: forgeguest\n'
	return(''.join(('.{}'.format(c) for c in [char for char in str(args[0]).lower() if (char not in 'aeiouy')])))
