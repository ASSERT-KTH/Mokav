def func(*args):
	ret_values = []
	
	n = hex(int(args[0]))[2:].upper()
	ret_values.append((((((((n.count('0') + n.count('4')) + n.count('6')) + (n.count('8') * 2)) + n.count('9')) + n.count('A')) + (n.count('B') * 2)) + n.count('D')))

	return ret_values
