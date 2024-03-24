def func(*args):
	ret_values = []
	
	s = args[0]
	res = s.count('VK')
	s = s.split('VK')
	res += (sum([(('VV' in x) or ('KK' in x)) for x in s]) > 0)
	ret_values.append(res)

	return ret_values
