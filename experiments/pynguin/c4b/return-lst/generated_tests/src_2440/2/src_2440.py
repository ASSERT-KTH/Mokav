def func(*args):
	ret_values = []
	
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
	if (First_letter in upper_case):
	    if (counter == len(Rest)):
	        New_word = First_letter.lower()
	        for letter in Rest:
	            New_word += letter.lower()
	        ret_values.append(New_word)
	    else:
	        ' The rest of the letter is a combination of upper and lower case letter'
	        ret_values.append(word)
	elif (counter == len(Rest)):
	    New_word = First_letter.upper()
	    for letter in Rest:
	        New_word += letter.lower()
	    ret_values.append(New_word)
	else:
	    ' The rest of the letter is a combination of upper and lower case letter'
	    ret_values.append(word)

	return ret_values
