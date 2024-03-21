def func(*args):
	ret_values = []
	
	s = str(args[0])
	a = s.count('VK')
	s = s.replace('VK', 'TP')
	if ((s.find('VV') != (- 1)) or (s.find('KK') != (- 1))):
	    a += 1
	ret_values.append(a)

	return ret_values
