def func(*args):
	ret_values = []
	
	(_, t) = map(int, args[0].split())
	s = args[1]
	while (t > 0):
	    i = 0
	    s1 = ''
	    while (i < len(s)):
	        try:
	            if ((s[i] == 'B') and (s[(i + 1)] == 'G')):
	                s1 += (s[(i + 1)] + s[i])
	                i += 1
	            else:
	                s1 += s[i]
	        except:
	            s1 += s[i]
	        i += 1
	    s = s1
	    t -= 1
	ret_values.append(s)

	return ret_values
