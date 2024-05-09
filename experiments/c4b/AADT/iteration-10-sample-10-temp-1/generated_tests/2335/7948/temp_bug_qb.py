def original_func(*args):
	global_list = []
	
	vasya = args[0]
	
	def removeLetter(vasya, letter):
	    number = vasya.find(letter)
	    if (number >= 0):
	        return vasya[(number + 1):]
	    else:
	        return ''
	temp = vasya
	for letter in 'hello':
	    temp = removeLetter(temp, letter)
	if ((temp == '') and (vasya != 'hello')):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list