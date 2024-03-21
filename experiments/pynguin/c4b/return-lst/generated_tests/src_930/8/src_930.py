def func(*args):
	ret_values = []
	
	__author__ = 'runekri3'
	VOWELS = list('aeiouy')
	CONSONANTS = list('bcdefghjklmnpqrstvwxyz')
	question = args[0]
	for letter in reversed(question.lower()):
	    if (letter in VOWELS):
	        ret_values.append('YES')
	        break
	    elif (letter in CONSONANTS):
	        ret_values.append('NO')
	        break

	return ret_values
