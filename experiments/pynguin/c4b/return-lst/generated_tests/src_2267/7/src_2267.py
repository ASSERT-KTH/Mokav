def func(*args):
	ret_values = []
	
	word = args[0]
	n = len(word)
	nword = ''
	b = 'true'
	if (n != 1):
	    for i in range(1, n):
	        if word[i].islower():
	            b = 'false'
	            break
	if (b == 'true'):
	    for i in range(0, n):
	        if word[i].islower():
	            nword += word[i].upper()
	        else:
	            nword += word[i].lower()
	else:
	    nword = word
	ret_values.append(nword)

	return ret_values
