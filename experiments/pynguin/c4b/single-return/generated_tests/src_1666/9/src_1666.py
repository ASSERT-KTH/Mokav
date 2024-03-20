def func(*args):
	
	s = args[0]
	ans = s.count('VK')
	s = s.replace('VK', '--')
	if ((s.find('VV') > (- 1)) or (s.find('KK') > (- 1))):
	    ans += 1
	return(ans)
