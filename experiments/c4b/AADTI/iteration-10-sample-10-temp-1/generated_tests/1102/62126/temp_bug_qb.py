def original_func(*args):
	global_list = []
	
	string = args[0].lower()
	words = ['a', 'o', 'y', 'e', 'u', 'i']
	word = ''
	for i in string:
	    if (i not in words):
	        word += ('.' + i)
	return global_list