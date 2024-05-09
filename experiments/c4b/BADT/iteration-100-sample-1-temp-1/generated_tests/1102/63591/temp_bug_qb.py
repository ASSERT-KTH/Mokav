def original_func(*args):
	global_list = []
	
	'\nCreated on Fri Jul 21 03:12:59 2017\n\n@author: omaroove\n'
	Word = args[0]
	word = Word.lower()
	
	def dot(word):
	    return '.'.join(list(word))
	(Namee, s) = ('', '')
	for i in range(len(word)):
	    if ((word[i] != 'O') and (word[i] != 'o') and (word[i] != 'I') and (word[i] != 'i') and (word[i] != 'U') and (word[i] != 'u') and (word[i] != 'E') and (word[i] != 'e') and (word[i] != 'A') and (word[i] != 'a')):
	        Namee += word[i]
	Res = dot(Namee)
	global_list.append(('.' + Res))
	return global_list