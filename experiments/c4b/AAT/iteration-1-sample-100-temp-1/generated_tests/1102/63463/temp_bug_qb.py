def original_func(*args):
	global_list = []
	
	word = args[0]
	word = word.lower()
	emp = ''
	for i in word:
	    if ((i == 'a') or (i == 'o') or (i == 'e') or (i == 'u') or (i == 'i')):
	        pass
	    else:
	        emp = ((emp + '.') + i)
	global_list.append(emp)
	return global_list