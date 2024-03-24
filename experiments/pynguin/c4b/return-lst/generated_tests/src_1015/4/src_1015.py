def func(*args):
	ret_values = []
	
	n = args[0]
	m = n.count('VK')
	n = n.replace('VK', 'O')
	if (('VV' in n) or ('KK' in n)):
	    m = (m + 1)
	ret_values.append(m)

	return ret_values
