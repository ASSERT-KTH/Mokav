def original_func(*args):
	global_list = []
	
	word = args[0]
	if (('H' in word) or ('Q' in word) or ('9' in word) or ('+' in word)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list