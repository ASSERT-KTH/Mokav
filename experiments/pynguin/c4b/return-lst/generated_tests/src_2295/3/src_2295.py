def func(*args):
	ret_values = []
	
	from collections import Counter
	ret_values.append(('CHAT WITH HER!' if ((len(Counter(args[0]).keys()) % 2) == 0) else 'IGNORE HIM!'))

	return ret_values
