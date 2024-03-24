def func(*args):
	
	s = args[0]
	index = [(- 1)]
	for i in range(len(s)):
	    if (s[i] in 'AEIOUY'):
	        index.append(i)
	index.append(len(s))
	g = (- 2)
	for i in range(1, len(index)):
	    if ((index[i] - index[(i - 1)]) > g):
	        g = (index[i] - index[(i - 1)])
	return(g)
