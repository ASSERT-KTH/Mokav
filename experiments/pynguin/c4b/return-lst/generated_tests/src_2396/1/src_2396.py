def func(*args):
	ret_values = []
	
	'\nCreated on Fri Jul 21 03:12:59 2017\n\n@author: omaroove\n'
	Word = args[0]
	word = Word.lower()
	
	def dot(word):
	    return '.'.join(list(word))
	(Namee, s) = ('', '')
	for i in range(len(word)):
	    if ((word[i] != 'o') and (word[i] != 'i') and (word[i] != 'u') and (word[i] != 'e') and (word[i] != 'a') and (word[i] != 'y')):
	        Namee += word[i]
	Res = dot(Namee)
	ret_values.append(('.' + Res))

	return ret_values
