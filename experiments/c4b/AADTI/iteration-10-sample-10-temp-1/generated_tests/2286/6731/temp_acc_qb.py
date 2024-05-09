def patched_func(*args):
	global_list = []
	
	__author__ = 'runekri3'
	VOWELS = list('aeiouy')
	CONSONANTS = list('bcdefghjklmnpqrstvwxyz')
	question = args[0]
	for letter in reversed(question.lower()):
	    if (letter in VOWELS):
	        global_list.append('YES')
	        break
	    elif (letter in CONSONANTS):
	        global_list.append('NO')
	        break
	return global_list