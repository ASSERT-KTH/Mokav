def func(*args):
	
	s = str(args[0])
	a = s.count('VK')
	s = s.replace('VK', 'TP')
	if ((s.find('VV') != (- 1)) or (s.find('KK') != (- 1))):
	    a += 1
	return(a)
