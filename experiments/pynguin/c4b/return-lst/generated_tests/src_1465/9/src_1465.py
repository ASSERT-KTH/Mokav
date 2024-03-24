def func(*args):
	ret_values = []
	
	string = args[0]
	chars = 'abcdefghijklmnopqrstuvwxyz'
	total = len(string)
	for char in chars:
	    count = string.count(char)
	    if (count > 1):
	        total -= (count - 1)
	if ((total % 2) == 0):
	    ret_values.append('CHAT WITH HER!')
	else:
	    ret_values.append('IGNORE HIM!')

	return ret_values
