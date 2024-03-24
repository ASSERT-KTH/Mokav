def func(*args):
	
	str = args[0]
	
	def accident(s):
	    if s.isupper():
	        return True
	    for i in range(1, len(s)):
	        if s[i].islower():
	            return False
	    return True
	
	def capslock(s):
	    result = ''
	    words = s.split(' ')
	    for word in words:
	        if accident(word):
	            result = ((result + word.swapcase()) + ' ')
	        else:
	            result = ((result + word) + ' ')
	    return result.strip(' ')
	return(capslock(str))
