def func(*args):
	
	return(('CHAT WITH HER!', 'IGNORE HIM!')[(len(set(args[0])) % 2)])
