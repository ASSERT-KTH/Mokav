def func(*args):
	ret_values = []
	
	s = args[0]
	s1 = ''
	kt2 = 0
	for i in range(len(s)):
	    if (ord(s[i]) <= 90):
	        kt2 += 1
	if (kt2 == len(s)):
	    ret_values.append(s.lower())
	elif ((kt2 == (len(s) - 1)) and (ord(s[0]) >= 97)):
	    s1 += s[0].upper()
	    s1 += s[1:].lower()
	    ret_values.append(s1)
	else:
	    ret_values.append(s)

	return ret_values
