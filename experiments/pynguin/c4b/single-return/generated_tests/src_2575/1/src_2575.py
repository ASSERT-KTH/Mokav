def func(*args):
	
	s = args[0]
	c = s.count('VK')
	s = s.replace('VK', 'ms')
	if (('VV' in s) or ('KK' in s)):
	    c += 1
	return(c)
