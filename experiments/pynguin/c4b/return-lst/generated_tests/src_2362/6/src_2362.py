def func(*args):
	ret_values = []
	
	s = args[0].lower()
	s2 = '.'
	v = 'aoyeui'
	i = 0
	while (i < len(s)):
	    if (not (s[i] in v)):
	        s2 += s[i]
	        s2 += '.'
	    i += 1
	i = 0
	s = ''
	while (i < (len(s2) - 1)):
	    s += s2[i]
	    i += 1
	ret_values.append(s)

	return ret_values
