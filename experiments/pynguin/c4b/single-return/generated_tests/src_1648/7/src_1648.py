def func(*args):
	
	word = args[0]
	return(('YES' if ((word.find(chr(72)) > (- 1)) or (word.find(chr(81)) > (- 1)) or (word.find(chr(57)) > (- 1))) else 'NO'))
