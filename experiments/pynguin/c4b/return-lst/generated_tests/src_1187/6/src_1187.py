def func(*args):
	ret_values = []
	
	s = args[0]
	if ((s.count('@') != 1) or (s.count('/') > 1)):
	    ret_values.append('NO')
	    exit(0)
	pos1 = s.find('@')
	pos2 = s.find('/')
	if (pos2 == (- 1)):
	    pos2 = len(s)
	import re
	username = re.compile('(\\w){1,16}$')
	hostname = re.compile('(\\w{1,16}\\.){0,8}\\w{1,16}$')
	ok1 = hostname.match(s[(pos1 + 1):pos2])
	ok2 = username.match(s[0:pos1])
	ok3 = username.match(s[(pos2 + 1):len(s)])
	if ((len(s[(pos1 + 1):pos2]) >= 1) and (len(s[(pos1 + 1):pos2]) <= 32) and ok1 and ok2 and ((pos2 == len(s)) or ok3)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
