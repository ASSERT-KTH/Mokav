def func(*args):
	ret_values = []
	
	s = args[0]
	first_letter = 0
	next_letters = '1'
	if (s[0].isupper() is True):
	    first_letter = 1
	for i in range(1, len(s)):
	    if (s[i].isupper() is True):
	        next_letters = (next_letters + '1')
	    else:
	        next_letters = (next_letters + '0')
	if ((first_letter == 1) and ('0' not in next_letters)):
	    result = []
	    for i in range(0, len(s)):
	        result.append(s[i].lower())
	    ret_values.append(''.join(result))
	elif ((first_letter == 1) and ('0' in next_letters)):
	    ret_values.append(s)
	elif ((first_letter == 0) and ('0' not in next_letters)):
	    result = [s[0].upper()]
	    for i in range(1, len(s)):
	        result.append(s[i].lower())
	    ret_values.append(''.join(result))
	elif ((first_letter == 0) and ('0' in next_letters)):
	    ret_values.append(s)

	return ret_values
