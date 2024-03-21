def func(*args):
	ret_values = []
	
	string = args[0].lower()
	words = ['a', 'o', 'y', 'e', 'u', 'i']
	word = ''
	for i in string:
	    if (i not in words):
	        word += ('.' + i)
	ret_values.append(word)

	return ret_values
