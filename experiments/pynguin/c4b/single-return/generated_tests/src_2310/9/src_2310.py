def func(*args):
	
	import sys
	import re
	
	def out(in_string):
	    no_vowel = re.sub('[aoyeui]', '', in_string.lower())
	    consonant_transform = re.sub('(\\w)', '.\\g<1>', no_vowel)
	    return(consonant_transform)
	if (__name__ == '__main__'):
	    out(args[0])
