def func(*args):
	ret_values = []
	
	s = args[0]
	ans = s.count('VK')
	s = s.replace('VK', '--')
	if ((s.find('VV') > (- 1)) or (s.find('KK') > (- 1))):
	    ans += 1
	ret_values.append(ans)

	return ret_values
