def patched_func(*args):
	global_list = []
	
	string = args[0]
	chars = 'abcdefghijklmnopqrstuvwxyz'
	total = len(string)
	for char in chars:
	    count = string.count(char)
	    if (count > 1):
	        total -= (count - 1)
	if ((total % 2) == 0):
	    global_list.append('CHAT WITH HER!')
	else:
	    global_list.append('IGNORE HIM!')
	return global_list