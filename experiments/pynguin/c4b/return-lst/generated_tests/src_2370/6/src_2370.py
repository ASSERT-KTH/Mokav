def func(*args):
	ret_values = []
	
	ret_values.append(('IGNORE HIM!' if (len(set(args[0])) % 2) else 'CHAT WITH HER!'))

	return ret_values
