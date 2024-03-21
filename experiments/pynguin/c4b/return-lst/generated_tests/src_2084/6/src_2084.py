def func(*args):
	ret_values = []
	
	text = args[0]
	if text.isupper():
	    ret_values.append(text.lower())
	elif ((text[:1] == text[:1].lower()) and (text[1:] == text[1:].upper())):
	    text = text.lower()
	    big = text[:1].upper()
	    ret_values.append((big + text[1:]))
	else:
	    ret_values.append(text)

	return ret_values
