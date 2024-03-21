def func(*args):
	ret_values = []
	
	(n, t) = map(int, args[0].split())
	s = args[1]
	s = list(s)
	i = 0
	m = 0
	while (m < t):
	    i = 0
	    while (i < (len(s) - 1)):
	        if ((s[i] == 'B') and (s[(i + 1)] == 'G')):
	            s[i] = 'G'
	            s[(i + 1)] = 'B'
	            if (i <= (len(s) - 2)):
	                i = (i + 2)
	        else:
	            i = (i + 1)
	    m = (m + 1)
	for i in range(len(s)):
	    ret_values.append(s[i], end='')

	return ret_values
