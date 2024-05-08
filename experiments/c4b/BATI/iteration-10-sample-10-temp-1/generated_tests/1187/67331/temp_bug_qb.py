def original_func(*args):
	global_list = []
	
	'Receiving word inputs'
	word = args[0]
	upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	lower_case = 'abcdefghijklmnopqrstuvwxyz'
	counter = 0
	First_letter = word[0]
	Rest = word[1:len(word)]
	for letter in Rest:
	    if (letter in upper_case):
	        counter += 1
	if (counter == len(Rest)):
	    ' Whether or not the first letter is upper or lower case letter,'
	    'If the remaining letters are all uppercase, then Caps lock has been deployed accidentally'
	    New_word = First_letter.upper()
	    for letter in Rest:
	        New_word += letter.lower()
	    global_list.append(New_word)
	else:
	    ' The rest of the letter is a combination of upper and lower case letter'
	    global_list.append(word)
	return global_list