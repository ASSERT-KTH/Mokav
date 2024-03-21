def func(*args):
	ret_values = []
	
	word = args[0]
	count = 0
	output = ''
	for x in word:
	    if ((count == 0) and x.islower()):
	        x = x.upper()
	    elif x.isupper():
	        x = x.lower()
	    else:
	        ret_values.append(word)
	        break
	    count += 1
	    output += x
	if (count == len(word)):
	    ret_values.append(output)

	return ret_values
