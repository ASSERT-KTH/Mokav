def original_func(*args):
	global_list = []
	
	
	def solution(word):
	    if word.isupper():
	        global_list.append(word.lower())
	    elif str(word[1:]).isupper():
	        global_list.append((str(word[0]).upper() + str(word[1:]).lower()))
	    else:
	        global_list.append(word)
	word = args[0]
	solution(word)
	return global_list