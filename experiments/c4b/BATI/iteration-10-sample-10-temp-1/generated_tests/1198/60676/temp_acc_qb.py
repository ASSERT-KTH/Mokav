def patched_func(*args):
	global_list = []
	
	word = args[0]
	if ('H' in word):
	    global_list.append('YES')
	elif ('Q' in word):
	    global_list.append('YES')
	elif ('9' in word):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list