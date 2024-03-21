def func(*args):
	ret_values = []
	
	vasya = args[0]
	
	def removeLetter(name, letter):
	    number = name.find(letter)
	    if (number >= 0):
	        return name[(number + 1):]
	    else:
	        return '.'
	temp = vasya
	for letter in 'hello':
	    temp = removeLetter(temp, letter)
	if ((temp == '.') and (vasya != 'hello')):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
