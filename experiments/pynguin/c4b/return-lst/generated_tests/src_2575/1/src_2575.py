def func(*args):
	ret_values = []
	
	s = args[0]
	c = s.count('VK')
	s = s.replace('VK', 'ms')
	if (('VV' in s) or ('KK' in s)):
	    c += 1
	ret_values.append(c)

	return ret_values
