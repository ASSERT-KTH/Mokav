def func(*args):
	
	(c, t) = map(int, args[0].split())
	s = args[1]
	newR = ''
	for i in range(t):
	    sl = 0
	    newR = ''
	    if (sl >= (c - 1)):
	        newR = s
	        break
	    while (sl < (c - 1)):
	        if ((s[sl] == 'B') and (s[(sl + 1)] == 'G')):
	            newR += 'GB'
	            sl += 2
	        else:
	            newR += s[sl]
	            sl += 1
	        if (sl == (c - 1)):
	            newR = (newR + s[(- 1)])
	    s = newR
	return(newR)
