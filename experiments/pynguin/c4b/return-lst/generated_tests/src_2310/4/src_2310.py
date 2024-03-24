def func(*args):
	ret_values = []
	
	import sys
	import re
	
	def out(in_string):
	    no_vowel = re.sub('[aoyeui]', '', in_string.lower())
	    consonant_transform = re.sub('(\\w)', '.\\g<1>', no_vowel)
	    ret_values.append(consonant_transform)
	if (__name__ == '__main__'):
	    out(args[0])

	return ret_values
