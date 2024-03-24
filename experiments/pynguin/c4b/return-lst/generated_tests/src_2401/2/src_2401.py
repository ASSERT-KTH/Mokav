def func(*args):
	ret_values = []
	
	name = args[0]
	length = len(name)
	list = set()
	for letter in name:
	    list.add(letter)
	if ((len(list) % 2) == 0):
	    ret_values.append('CHAT WITH HER!')
	else:
	    ret_values.append('IGNORE HIM!')

	return ret_values
