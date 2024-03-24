def func(*args):
	
	from collections import Counter
	return(('CHAT WITH HER!' if ((len(Counter(args[0]).keys()) % 2) == 0) else 'IGNORE HIM!'))
