def func(*args):
	ret_values = []
	
	s = args[0]
	lowerCount = 0
	upperCount = 0
	for i in range(len(s)):
	    if ('a' <= s[i] <= 'z'):
	        lowerCount += 1
	    else:
	        upperCount += 1
	if (lowerCount >= upperCount):
	    ret_values.append(s.lower())
	else:
	    ret_values.append(s.upper())

	return ret_values
