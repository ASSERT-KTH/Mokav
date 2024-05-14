def original_func(*args):
	global_list = []
	
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
	    result = [s[0]]
	    for i in range(1, len(s)):
	        result.append(s[i].lower())
	    global_list.append(''.join(result))
	elif ((first_letter == 1) and ('0' in next_letters)):
	    global_list.append(s)
	elif ((first_letter == 0) and ('0' not in next_letters)):
	    result = [s[0].upper()]
	    for i in range(1, len(s)):
	        result.append(s[i].lower())
	    global_list.append(''.join(result))
	elif ((first_letter == 0) and ('0' in next_letters)):
	    global_list.append(s)
	return global_list