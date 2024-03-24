def func(*args):
	ret_values = []
	
	word = args[0]
	list = []
	for letter in word:
	    if (letter not in ('a', 'e', 'i', 'y', 'Y', 'o', 'u', 'A', 'E', 'I', 'O', 'U')):
	        list.append(letter)
	for i in range(len(list)):
	    ret_values.append('.', end='')
	    (ret_values.append(list[i].lower(), end=''),)

	return ret_values
