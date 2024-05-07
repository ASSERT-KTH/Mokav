def patched_func(*args):
	global_list = []
	
	s = args[0]
	s1 = ''
	kt2 = 0
	for i in range(len(s)):
	    if (ord(s[i]) <= 90):
	        kt2 += 1
	if (kt2 == len(s)):
	    global_list.append(s.lower())
	elif ((kt2 == (len(s) - 1)) and (ord(s[0]) >= 97)):
	    s1 += s[0].upper()
	    s1 += s[1:].lower()
	    global_list.append(s1)
	else:
	    global_list.append(s)
	return global_list