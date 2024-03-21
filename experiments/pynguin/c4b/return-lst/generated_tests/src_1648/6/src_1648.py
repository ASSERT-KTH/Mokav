def func(*args):
	ret_values = []
	
	word = args[0]
	ret_values.append(('YES' if ((word.find(chr(72)) > (- 1)) or (word.find(chr(81)) > (- 1)) or (word.find(chr(57)) > (- 1))) else 'NO'))

	return ret_values
