def func(*args):
	ret_values = []
	
	s = args[0]
	if ((s.count('@') != 1) or (s.count('/') > 1)):
	    ret_values.append('NO')
	    exit()
	p1 = s.find('@')
	p2 = s.find('/')
	if (p2 == (- 1)):
	    p2 = len(s)
	import re
	u = re.compile('(\\w){1,16}$')
	h = re.compile('(\\w{1,16}\\.)*\\w{1,16}$')
	k1 = h.match(s[(p1 + 1):p2])
	k2 = u.match(s[0:p1])
	k3 = u.match(s[(p2 + 1):len(s)])
	if ((len(s[(p1 + 1):p2]) >= 1) and (len(s[(p1 + 1):p2]) <= 32) and k1 and k2 and ((p2 == len(s)) or k3)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
