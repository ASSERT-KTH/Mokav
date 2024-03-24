def func(*args):
	
	s = args[0]
	count = s.count('VK')
	if (('VV' in s.replace('VK', '-')) or ('KK' in s.replace('VK', '-'))):
	    count += 1
	return(count)
