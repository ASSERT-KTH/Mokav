def func(*args):
	ret_values = []
	
	import re
	s = args[0]
	if ('@' not in s):
	    ret_values.append('NO')
	    exit()
	(u, h) = s.split('@', 1)
	r = None
	if ('/' in h):
	    if ('/' in h[(h.index('/') + 1):]):
	        ret_values.append('NO')
	        exit()
	    (h, r) = h.split('/')
	if (not re.match('^\\w{1,16}$', u)):
	    ret_values.append('NO')
	elif ((r is not None) and (not re.match('^\\w{1,16}$', r))):
	    ret_values.append('NO')
	elif ((1 > len(h)) or (len(h) > 32)):
	    ret_values.append('NO')
	else:
	    h = h.split('.')
	    if any(((not re.match('^\\w{1,16}$', x)) for x in h)):
	        ret_values.append('NO')
	    else:
	        ret_values.append('YES')

	return ret_values
